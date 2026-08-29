# run this in new terminal
# py -3.11 app.py

from flask import Flask, render_template, request, redirect, url_for, send_file, flash
import tensorflow as tf
from ultralytics import YOLO
import json
import os
import io
import re
import uuid
import base64
import numpy as np
from PIL import Image, UnidentifiedImageError
from disease_info import DISEASE_INFO
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()  # reads GROQ_API_KEY from a local .env file (see .env.example)

app = Flask(__name__)
app.secret_key = "leaflens-ai-dev-secret-key"  # only needed for flash messages, fine for a local demo

# ---------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------
ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png", "webp"}
MAX_FILE_SIZE_MB = 16
CONFIDENCE_HIGH_THRESHOLD = 85     # >= this -> "high" confidence badge
CONFIDENCE_MEDIUM_THRESHOLD = 60   # >= this -> "medium" confidence badge, below -> "low"
UPLOAD_DIR = os.path.join("static", "uploads")
HISTORY_FILE = "history.json"
HISTORY_MAX_ENTRIES = 100

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
GROQ_VISION_MODEL = "qwen/qwen3.6-27b"
GROQ_MODEL_DISPLAY_NAME = "Groq — Qwen 3.6 27B"

app.config["MAX_CONTENT_LENGTH"] = MAX_FILE_SIZE_MB * 1024 * 1024
os.makedirs(UPLOAD_DIR, exist_ok=True)

# ---------------------------------------------------------------
# Load models once at startup
# ---------------------------------------------------------------
print("Loading CNN model...")
keras_model = tf.keras.models.load_model("plant_disease_best.keras")
print("Loading YOLO model...")
yolo_model = YOLO("yolo_plantvillage_best.pt")

with open("class_names.json", "r") as f:
    class_names = json.load(f)

print(f"LeafLens AI ready — {len(class_names)} classes loaded.")


# ---------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------
def normalize_class_name(name):
    """Normalize a raw class name to match DISEASE_INFO keys."""
    name = name.replace("___", " - ")
    name = name.replace("_", " ")
    return name


def confidence_level(conf):
    if conf >= CONFIDENCE_HIGH_THRESHOLD:
        return "high"
    elif conf >= CONFIDENCE_MEDIUM_THRESHOLD:
        return "medium"
    return "low"


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def load_history():
    if not os.path.exists(HISTORY_FILE):
        return []
    try:
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return []


def save_history(entries):
    with open(HISTORY_FILE, "w") as f:
        json.dump(entries, f, indent=2)


def add_history_entry(entry):
    entries = load_history()
    entries.insert(0, entry)
    entries = entries[:HISTORY_MAX_ENTRIES]
    save_history(entries)


def get_disease_info(result_name):
    return DISEASE_INFO.get(
        result_name,
        {
            "symptoms": ["Information not available for this class."],
            "treatment": ["Information not available for this class."],
            "prevention": ["Information not available for this class."],
            "severity": "Unknown",
            "organic": "Information not available.",
        },
    )


class GroqAnalysisError(Exception):
    """Raised when the Groq vision call fails or returns something unusable."""
    pass


def qualitative_confidence_level(label):
    """Maps Groq's text confidence ('High'/'Moderate'/'Low') to a CSS badge class."""
    label = (label or "").strip().lower()
    if label == "high":
        return "high"
    if label == "moderate":
        return "medium"
    return "low"


def analyze_with_groq_vision(image_path):
    """
    Sends an image to Groq's vision-capable model and returns
    a structured dict.
    """

    from groq import Groq

    with open(image_path, "rb") as f:
        b64_image = base64.b64encode(f.read()).decode("utf-8")

    client = Groq(api_key=GROQ_API_KEY)

    prompt = """
Analyze the plant leaf shown in the image.

Return ONLY one valid JSON object.
Do not return Markdown.
Do not return ```json.
Do not include explanations outside the JSON.

Use exactly this structure:

{
  "is_leaf": true,
  "plant": "Unknown",
  "likely_disease": "Unable to determine",
  "confidence": "Low",
  "severity": "Unknown",
  "symptoms": [],
  "recommendation": [],
  "notes": ""
}

Rules:

- is_leaf: true or false.
- plant: plant/crop name if identifiable, otherwise "Unknown".
- likely_disease: most likely disease if visible, otherwise "Healthy" or "Unable to determine".
- When symptoms are visible, name the most specific plausible disease category you can reasonably support (for example "Bacterial Spot", "Powdery Mildew", "Rust", "Blight", "Anthracnose", "Black Rot", "Scab", or "Mosaic Virus") rather than defaulting to a generic label like "Leaf Spot" unless the visible pattern genuinely does not match any more specific known disease.
- If image quality (glare, blur, photographed off a screen) limits certainty, reflect that through a lower confidence value rather than through a vaguer disease name.
- confidence: exactly "High", "Moderate", or "Low".
- severity: exactly "None", "Low", "Medium", "High", or "Critical".
- symptoms: 2 to 4 short strings describing visible symptoms.
- recommendation: 2 to 4 short strings with practical next steps.
- notes: one short sentence.
- Never provide numeric confidence.
- If this is not clearly a plant leaf, set is_leaf to false.
- Do not invent a disease when the image is unclear.
"""

    try:
        completion = client.chat.completions.create(
            model=GROQ_VISION_MODEL,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": prompt
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{b64_image}"
                            }
                        }
                    ]
                }
            ],
            temperature=0.2,
            max_tokens=1200,
        )

    except Exception as e:
        print("========== GROQ ERROR ==========")
        print("Error type:", type(e).__name__)
        print("Error:", str(e))
        print("================================")

        raise GroqAnalysisError(
            f"The AI camera service couldn't be reached right now "
            f"({type(e).__name__}). Please try again in a moment."
        )

    raw_text = completion.choices[0].message.content if completion.choices else None

    if not raw_text:
        raise GroqAnalysisError(
            "The AI camera service returned an empty response. Please try again."
        )

    print("========== GROQ RAW RESPONSE ==========")
    print(raw_text)
    print("========================================")

    # ---------------------------------------------------------
    # Clean Groq response
    # ---------------------------------------------------------

    raw_text = raw_text.strip()

    # Remove Qwen reasoning block if present
    if "<think>" in raw_text:
        think_end = raw_text.find("</think>")

        if think_end != -1:
            raw_text = raw_text[think_end + len("</think>"):].strip()

    # Remove accidental Markdown code fences
    if raw_text.startswith("```"):
        raw_text = raw_text.replace("```json", "", 1)
        raw_text = raw_text.replace("```", "", 1)
        raw_text = raw_text.strip()

    # ---------------------------------------------------------
    # Extract JSON object
    # ---------------------------------------------------------

    json_start = raw_text.find("{")
    json_end = raw_text.rfind("}")

    if json_start == -1 or json_end == -1 or json_end <= json_start:
        raise GroqAnalysisError(
            "The AI camera service returned an unexpected response. Please try again."
        )

    json_text = raw_text[json_start:json_end + 1]

    try:
        data = json.loads(json_text)

    except (json.JSONDecodeError, TypeError):
        print("========== INVALID GROQ JSON ==========")
        print(json_text)
        print("=======================================")

        raise GroqAnalysisError(
            "The AI camera service returned an invalid response. Please try again."
        )

    # ---------------------------------------------------------
    # Basic response validation
    # ---------------------------------------------------------

    if not isinstance(data, dict):
        raise GroqAnalysisError(
            "The AI camera service returned an invalid response. Please try again."
        )

    data.setdefault("is_leaf", True)
    data.setdefault("plant", "Unknown")
    data.setdefault("likely_disease", "Unable to determine")
    data.setdefault("confidence", "Low")
    data.setdefault("severity", "Unknown")
    data.setdefault("symptoms", [])
    data.setdefault("recommendation", [])
    data.setdefault("notes", "")

    # Validate confidence
    if data["confidence"] not in ["High", "Moderate", "Low"]:
        data["confidence"] = "Low"

    # Validate severity
    if data["severity"] not in [
        "None",
        "Low",
        "Medium",
        "High",
        "Critical",
        "Unknown"
    ]:
        data["severity"] = "Unknown"

    # Validate list fields
    if not isinstance(data["symptoms"], list):
        data["symptoms"] = []

    if not isinstance(data["recommendation"], list):
        data["recommendation"] = []

    # Make sure is_leaf is actually boolean
    if not isinstance(data["is_leaf"], bool):
        data["is_leaf"] = True

    return data


# ---------------------------------------------------------------
# Routes
# ---------------------------------------------------------------
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/about-model")
def about_model():
    return render_template("about_model.html", num_classes=len(class_names))


@app.route("/history")
def history():
    entries = load_history()
    return render_template("history.html", entries=entries)


@app.route("/history/clear", methods=["POST"])
def clear_history():
    save_history([])
    flash("History cleared.", "success")
    return redirect(url_for("history"))


@app.route("/predict", methods=["POST"])
def predict():
    if "image" not in request.files or request.files["image"].filename == "":
        flash("Please select an image before analyzing.", "error")
        return redirect(url_for("home"))

    image = request.files["image"]

    if not allowed_file(image.filename):
        flash("Unsupported file type. Please upload a JPG, PNG, or WEBP image.", "error")
        return redirect(url_for("home"))

    unique_name = f"{uuid.uuid4().hex[:10]}_{image.filename}"
    image_path = os.path.join(UPLOAD_DIR, unique_name)

    # Save, then validate it's actually a readable image (catches corrupt/fake files)
    try:
        image.save(image_path)
        with Image.open(image_path) as check_img:
            check_img.verify()
        img = Image.open(image_path).convert("RGB")
    except (UnidentifiedImageError, OSError):
        if os.path.exists(image_path):
            os.remove(image_path)
        flash("That file couldn't be read as an image. Please try a different file.", "error")
        return redirect(url_for("home"))
    
    # =============================================
    # STEP 1: CNN Classification (Keras)
    # =============================================
    img_resized = img.resize((128, 128))
    img_array = np.expand_dims(np.array(img_resized), axis=0)

    cnn_prediction = keras_model.predict(img_array, verbose=0)
    cnn_class_idx = int(np.argmax(cnn_prediction))
    cnn_confidence = float(np.max(cnn_prediction)) * 100
    cnn_raw_name = class_names[cnn_class_idx]
    cnn_result = normalize_class_name(cnn_raw_name)

    # =============================================
    # STEP 2: YOLO Lesion Detection
    # =============================================
    yolo_results = yolo_model.predict(source=image_path, save=False, verbose=False)
    r = yolo_results[0]

    annotated_file = None
    yolo_result = None
    yolo_confidence = 0.0
    yolo_detections = 0

    if r.probs is not None:
        yolo_class_idx = int(r.probs.top1)
        yolo_confidence = float(r.probs.top1conf) * 100
        yolo_raw_name = yolo_model.names[yolo_class_idx]
        yolo_result = normalize_class_name(yolo_raw_name)
    elif len(r.boxes) > 0:
        best = r.boxes.conf.argmax()
        yolo_class_idx = int(r.boxes.cls[best])
        yolo_confidence = float(r.boxes.conf[best]) * 100
        yolo_raw_name = yolo_model.names[yolo_class_idx]
        yolo_result = normalize_class_name(yolo_raw_name)
        yolo_detections = len(r.boxes)

        annotated = r.plot()
        annotated_img = Image.fromarray(annotated[..., ::-1])  # BGR to RGB
        annotated_file = f"annotated_{unique_name}"
        annotated_img.save(os.path.join(UPLOAD_DIR, annotated_file))
    else:
        yolo_result = "No lesions detected"

    # Heuristic: if both models are very unconfident, this probably isn't
    # a leaf image at all (or is an unfamiliar/out-of-distribution one)
    no_leaf_detected = cnn_confidence < 40 and yolo_confidence < 40

    # =============================================
    # STEP 3: Combine Results
    # =============================================
    final_result = cnn_result

    if yolo_result and yolo_result != "No lesions detected":
        if cnn_result.lower() == yolo_result.lower():
            combined_confidence = min((cnn_confidence + yolo_confidence) / 2 + 5, 100.0)
            agreement = "agree"
        else:
            if cnn_confidence >= yolo_confidence:
                final_result, combined_confidence = cnn_result, cnn_confidence
            else:
                final_result, combined_confidence = yolo_result, yolo_confidence
            agreement = "disagree"
    else:
        combined_confidence = cnn_confidence
        agreement = "cnn_only"

    info = get_disease_info(final_result)

    # Log to history (skip logging clearly-invalid uploads)
    if not no_leaf_detected:
        add_history_entry({
            "id": uuid.uuid4().hex[:8],
            "timestamp": datetime.now().strftime("%d %b %Y, %I:%M %p"),
            "image_file": unique_name,
            "prediction": final_result,
            "confidence": round(combined_confidence, 1),
            "confidence_level": confidence_level(combined_confidence),
            "is_healthy": "healthy" in final_result.lower(),
        })

    return render_template(
        "index.html",
        prediction=final_result,
        confidence=combined_confidence,
        confidence_level=confidence_level(combined_confidence),
        image_file=unique_name,
        annotated_file=annotated_file,
        no_leaf_detected=no_leaf_detected,
        # Individual model details
        cnn_result=cnn_result,
        cnn_confidence=cnn_confidence,
        yolo_result=yolo_result,
        yolo_confidence=yolo_confidence,
        yolo_detections=yolo_detections,
        agreement=agreement,
        # Disease info
        symptoms=info["symptoms"],
        treatment=info["treatment"],
        prevention=info["prevention"],
        severity=info["severity"],
        organic=info["organic"],
    )


@app.route("/camera-analyze", methods=["POST"])
def camera_analyze():
    if not GROQ_API_KEY:
        flash("Live Camera Scan isn't configured yet — GROQ_API_KEY is missing from .env.", "error")
        return redirect(url_for("home"))

    if "image" not in request.files or request.files["image"].filename == "":
        flash("No image was captured. Please try again.", "error")
        return redirect(url_for("home"))

    image = request.files["image"]
    unique_name = f"cam_{uuid.uuid4().hex[:10]}.jpg"
    image_path = os.path.join(UPLOAD_DIR, unique_name)

    try:
        image.save(image_path)
        with Image.open(image_path) as check_img:
            check_img.verify()
        img = Image.open(image_path).convert("RGB")
        img.save(image_path, "JPEG", quality=90)  # normalize captured frame to a clean JPEG
    except (UnidentifiedImageError, OSError):
        if os.path.exists(image_path):
            os.remove(image_path)
        flash("That capture couldn't be read as an image. Please try again.", "error")
        return redirect(url_for("home"))

    try:
        result = analyze_with_groq_vision(image_path)
    except GroqAnalysisError as e:
        if os.path.exists(image_path):
            os.remove(image_path)
        flash(str(e), "error")
        return redirect(url_for("home"))

    confidence_text = result["confidence"]
    cam_confidence_level = qualitative_confidence_level(confidence_text)
    disease_display = result["likely_disease"]
    is_healthy = "healthy" in disease_display.lower()

    add_history_entry({
        "id": uuid.uuid4().hex[:8],
        "timestamp": datetime.now().strftime("%d %b %Y, %I:%M %p"),
        "image_file": unique_name,
        "prediction": disease_display,
        "confidence": confidence_text,          # text label, not a number, for camera-source entries
        "confidence_level": cam_confidence_level,
        "is_healthy": is_healthy,
        "source": "camera",
        "plant": result["plant"],
        "severity": result["severity"],
        "symptoms": result["symptoms"],
        "recommendation": result["recommendation"],
        "notes": result["notes"],
        "model_used": GROQ_MODEL_DISPLAY_NAME,
    })

    return render_template(
        "index.html",
        camera_result=True,
        cam_image_file=unique_name,
        cam_is_leaf=result["is_leaf"],
        cam_plant=result["plant"],
        cam_disease=disease_display,
        cam_confidence_text=confidence_text,
        cam_confidence_level=cam_confidence_level,
        cam_severity=result["severity"],
        cam_symptoms=result["symptoms"],
        cam_recommendation=result["recommendation"],
        cam_notes=result["notes"],
        model_display_name=GROQ_MODEL_DISPLAY_NAME,
    )


@app.route("/report/<image_file>")
def download_report(image_file):
    entries = load_history()
    entry = next((e for e in entries if e["image_file"] == image_file), None)

    if not entry:
        flash("No report data found for that analysis — it may have been cleared from history.", "error")
        return redirect(url_for("home"))

    if entry.get("source") == "camera":
        info = {
            "symptoms": entry.get("symptoms", []),
            "treatment": entry.get("recommendation", []),
            "prevention": [],
            "severity": entry.get("severity", "Unknown"),
            "organic": entry.get("notes", "Not available."),
        }
    else:
        info = get_disease_info(entry["prediction"])

    pdf_buffer = build_pdf_report(entry, info)

    return send_file(
        pdf_buffer,
        as_attachment=True,
        download_name=f"LeafLens_Report_{entry['id']}.pdf",
        mimetype="application/pdf",
    )


def build_pdf_report(entry, info):
    """Generates a PDF report in memory using reportlab."""
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.units import mm
    from reportlab.lib import colors
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image as RLImage, HRFlowable
    )

    buffer = io.BytesIO()
    doc = SimpleDocTemplate(
        buffer, pagesize=A4,
        topMargin=20 * mm, bottomMargin=20 * mm,
        leftMargin=20 * mm, rightMargin=20 * mm,
    )

    styles = getSampleStyleSheet()
    green_dark = colors.HexColor("#166534")
    green = colors.HexColor("#16A34A")

    title_style = ParagraphStyle("LLTitle", parent=styles["Title"], textColor=green_dark, fontSize=22)
    subtitle_style = ParagraphStyle("LLSubtitle", parent=styles["Normal"], textColor=colors.HexColor("#4B5563"))
    heading_style = ParagraphStyle("LLHeading", parent=styles["Heading2"], textColor=green, spaceBefore=10)
    body_style = ParagraphStyle("LLBody", parent=styles["Normal"], leading=15)

    story = [
        Paragraph("LeafLens AI", title_style),
        Paragraph("Plant Disease Analysis Report", subtitle_style),
        Spacer(1, 4),
        HRFlowable(width="100%", color=colors.HexColor("#DCFCE7"), thickness=2),
        Spacer(1, 12),
        Paragraph(f"<b>Analysis Date:</b> {entry['timestamp']}", body_style),
        Paragraph(f"<b>Report ID:</b> {entry['id']}", body_style),
        Spacer(1, 14),
        Paragraph(f"Detected: {entry['prediction']}", heading_style),
    ]

    is_camera_entry = entry.get("source") == "camera"
    confidence_display = entry["confidence"] if is_camera_entry else f"{entry['confidence']}%"
    story.append(Paragraph(f"<b>Confidence:</b> {confidence_display}", body_style))
    story.append(Paragraph(f"<b>Severity:</b> {info.get('severity', 'Unknown')}", body_style))
    if is_camera_entry:
        story.append(Paragraph(f"<b>Analysis Method:</b> AI Camera Scan", body_style))
        story.append(Paragraph(f"<b>Multimodal API Used:</b> {entry.get('model_used', 'N/A')}", body_style))
    else:
        story.append(Paragraph(f"<b>Analysis Method:</b> CNN + YOLO", body_style))
    story.append(Spacer(1, 14))

    img_path = os.path.join(UPLOAD_DIR, entry["image_file"])
    if os.path.exists(img_path):
        try:
            with Image.open(img_path) as im:
                w, h = im.size
            max_w = 120 * mm
            display_h = max_w * (h / w)
            story.append(RLImage(img_path, width=max_w, height=display_h))
            story.append(Spacer(1, 14))
        except Exception:
            pass

    section_key = "Recommendation" if is_camera_entry else "Treatment"
    sections = [("Symptoms", "symptoms"), (section_key, "treatment")]
    if not is_camera_entry:
        sections.append(("Prevention", "prevention"))

    for section_title, key in sections:
        items = info.get(key, [])
        if not items:
            continue
        story.append(Paragraph(section_title, heading_style))
        for item in items:
            story.append(Paragraph(f"• {item}", body_style))
        story.append(Spacer(1, 8))

    if is_camera_entry:
        story.append(Paragraph("Notes", heading_style))
        story.append(Paragraph(info.get("organic") or "None.", body_style))
    else:
        story.append(Paragraph("Organic Remedy", heading_style))
        story.append(Paragraph(info.get("organic", "Not available."), body_style))
    story.append(Spacer(1, 20))
    story.append(HRFlowable(width="100%", color=colors.HexColor("#DCFCE7"), thickness=1))
    story.append(Spacer(1, 6))
    disclaimer_text = (
        f"Generated by LeafLens AI — analyzed using {entry.get('model_used', 'a multimodal AI vision model')} "
        "via live camera scan. This is a general-purpose AI vision analysis, not LeafLens' custom-trained "
        "CNN/YOLO models, and should be treated as an approximate, exploratory reading."
        if is_camera_entry else
        "Generated by LeafLens AI — CNN + YOLO powered plant disease detection. "
        "This report is generated by an automated model and should be used as a supporting "
        "reference alongside expert agronomic advice."
    )
    story.append(Paragraph(
        disclaimer_text,
        ParagraphStyle("Disclaimer", parent=styles["Normal"], fontSize=8, textColor=colors.HexColor("#9CA3AF")),
    ))

    doc.build(story)
    buffer.seek(0)
    return buffer


# ---------------------------------------------------------------
# Error handlers
# ---------------------------------------------------------------
@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(413)
def file_too_large(e):
    flash(f"That file is too large. Please upload an image under {MAX_FILE_SIZE_MB} MB.", "error")
    return redirect(url_for("home"))


@app.errorhandler(500)
def server_error(e):
    flash("Something went wrong while processing that image. Please try again.", "error")
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(
    debug=True,
    host="0.0.0.0",
    port=5000,
    ssl_context="adhoc"
    )
