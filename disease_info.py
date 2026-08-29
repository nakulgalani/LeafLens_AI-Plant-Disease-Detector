"""
Disease information database for LeafLens AI.
Keys match the normalized output of app.py's normalize_class_name() function,
applied to the raw PlantVillage class names in class_names.json.
"""

DISEASE_INFO = {

    # ---------------- APPLE ----------------
    "Apple - Apple scab": {
        "symptoms": [
            "Olive-green to brown velvety spots on leaves, often with a fringed edge.",
            "Dark, scabby, corky lesions on the fruit surface.",
            "Premature yellowing and leaf drop in heavily infected trees.",
        ],
        "treatment": [
            "Remove and destroy fallen leaves and infected fruit to reduce fungal spores.",
            "Apply a protectant fungicide (e.g. captan or myclobutanil) starting at bud break.",
            "Prune to open the canopy and improve air circulation, which speeds leaf drying.",
        ],
        "prevention": [
            "Plant scab-resistant apple varieties where possible.",
            "Rake and dispose of leaf litter every autumn to break the infection cycle.",
            "Avoid overhead irrigation that keeps foliage wet for long periods.",
        ],
        "severity": "High",
        "organic": "Sulfur or copper-based sprays applied before bud break can suppress early infection organically.",
    },
    "Apple - Black rot": {
        "symptoms": [
            "Purple-bordered circular spots on leaves ('frog-eye leaf spot').",
            "Firm, brown, concentrically ringed rot on fruit, often starting at the calyx end.",
            "Cankers with reddish-brown, sunken bark on branches.",
        ],
        "treatment": [
            "Prune out and destroy cankered branches and mummified fruit.",
            "Apply fungicides labeled for black rot during the growing season, especially after wounds occur.",
            "Remove infected fruit promptly to prevent spore spread to healthy fruit.",
        ],
        "prevention": [
            "Sanitize pruning tools between cuts to avoid spreading the fungus.",
            "Avoid mechanical injury to bark and fruit, which creates infection sites.",
            "Remove nearby dead wood and mummified fruit before the growing season starts.",
        ],
        "severity": "High",
        "organic": "Copper-based fungicide applications in early spring can help slow spread in organic orchards.",
    },
    "Apple - Cedar apple rust": {
        "symptoms": [
            "Small yellow-orange spots on upper leaf surfaces that enlarge over the season.",
            "Orange, tube-like structures (aecia) forming on the underside of infected leaves.",
            "Requires a nearby juniper/cedar host to complete its life cycle.",
        ],
        "treatment": [
            "Apply fungicide sprays starting at pink bud stage through early summer.",
            "Remove galls from nearby juniper or cedar trees if present within a few hundred meters.",
            "Rake and destroy fallen infected leaves at season's end.",
        ],
        "prevention": [
            "Plant rust-resistant apple cultivars if cedar/juniper trees are common nearby.",
            "Avoid planting apples near ornamental junipers where practical.",
            "Monitor junipers in spring for orange gelatinous galls and remove them.",
        ],
        "severity": "Medium",
        "organic": "Sulfur sprays applied preventatively from pink bud stage can reduce infection organically.",
    },
    "Apple - healthy": {
        "symptoms": ["No disease symptoms observed.", "Leaves are uniformly green with no spotting or discoloration.", "Normal, vigorous growth pattern."],
        "treatment": ["No treatment needed.", "Continue standard watering and fertilization schedule.", "Monitor periodically for early signs of common apple diseases."],
        "prevention": ["Maintain good orchard sanitation and pruning practices.", "Water at the base rather than overhead to keep foliage dry.", "Schedule routine inspection during humid or wet growing seasons."],
        "severity": "None",
        "organic": "No intervention necessary — healthy foliage detected.",
    },

    # ---------------- BLUEBERRY ----------------
    "Blueberry - healthy": {
        "symptoms": ["No disease symptoms observed.", "Foliage shows normal color and texture.", "Growth pattern appears typical for the season."],
        "treatment": ["No treatment needed.", "Maintain consistent, well-drained, acidic soil moisture.", "Continue regular nutrient monitoring."],
        "prevention": ["Keep soil pH between 4.5–5.5, which blueberries require to thrive.", "Prune out old or crowded canes to maintain airflow.", "Watch for early signs of mummy berry or leaf spot during wet weather."],
        "severity": "None",
        "organic": "No intervention necessary — healthy foliage detected.",
    },

    # ---------------- CHERRY ----------------
    "Cherry (including sour) - Powdery mildew": {
        "symptoms": [
            "White, powdery fungal growth on leaf surfaces and shoot tips.",
            "Leaves may curl, pucker, or become distorted.",
            "Reduced fruit quality and delayed ripening in severe cases.",
        ],
        "treatment": [
            "Apply sulfur or a labeled fungicide at first sign of white powdery patches.",
            "Prune infected shoot tips to reduce the source of spores.",
            "Improve air circulation by thinning dense canopy growth.",
        ],
        "prevention": [
            "Avoid excess nitrogen fertilization, which promotes susceptible new growth.",
            "Space trees adequately to allow airflow and faster leaf drying.",
            "Choose mildew-resistant cherry varieties where available.",
        ],
        "severity": "Medium",
        "organic": "Potassium bicarbonate or sulfur sprays are effective organic options against powdery mildew.",
    },
    "Cherry (including sour) - healthy": {
        "symptoms": ["No disease symptoms observed.", "Leaves are healthy green with no powdery coating or spotting.", "Normal seasonal growth."],
        "treatment": ["No treatment needed.", "Continue regular irrigation and feeding.", "Monitor during humid periods for early mildew signs."],
        "prevention": ["Prune annually to keep the canopy open.", "Avoid overhead watering late in the day.", "Inspect new growth regularly during spring."],
        "severity": "None",
        "organic": "No intervention necessary — healthy foliage detected.",
    },

    # ---------------- CORN / MAIZE ----------------
    "Corn (maize) - Cercospora leaf spot Gray leaf spot": {
        "symptoms": [
            "Small, tan to gray rectangular lesions bound by leaf veins.",
            "Lesions can merge, causing large areas of leaf blight and dieback.",
            "Disease progresses from lower to upper leaves as the season advances.",
        ],
        "treatment": [
            "Apply a foliar fungicide when lesions first appear, especially in susceptible hybrids.",
            "Rotate with a non-host crop such as soybean for at least one season.",
            "Remove and bury or destroy heavily infected crop residue after harvest.",
        ],
        "prevention": [
            "Plant resistant or tolerant corn hybrids where available.",
            "Practice crop rotation and residue management to reduce overwintering spores.",
            "Avoid dense planting that limits airflow and prolongs leaf wetness.",
        ],
        "severity": "Medium",
        "organic": "Crop rotation and residue destruction are the primary organic controls; biofungicides offer limited suppression.",
    },
    "Corn (maize) - Common rust ": {
        "symptoms": [
            "Small, reddish-brown, powdery pustules scattered on both leaf surfaces.",
            "Pustules can turn dark brown to black as the season progresses.",
            "Severe infections cause leaves to yellow and senesce early.",
        ],
        "treatment": [
            "Apply fungicide if rust develops before tasseling on susceptible hybrids.",
            "Monitor fields closely during cool, humid weather when rust spreads fastest.",
            "Remove volunteer corn plants that can carry the fungus between seasons.",
        ],
        "prevention": [
            "Plant rust-resistant hybrids, which greatly reduce risk.",
            "Avoid late planting that exposes young plants to peak rust pressure.",
            "Scout fields regularly during the growing season, especially in humid climates.",
        ],
        "severity": "Medium",
        "organic": "Resistant hybrids are the most effective organic-compatible defense; sulfur has limited field efficacy.",
    },
    "Corn (maize) - Northern Leaf Blight": {
        "symptoms": [
            "Long, elliptical, grayish-green to tan lesions running parallel to leaf veins.",
            "Lesions can reach several centimeters long and merge to blight entire leaves.",
            "Severe cases significantly reduce photosynthetic leaf area and yield.",
        ],
        "treatment": [
            "Apply a foliar fungicide at early lesion onset, particularly around silking.",
            "Rotate crops and till under residue to reduce fungal carryover.",
            "Select resistant hybrids for future plantings in high-pressure fields.",
        ],
        "prevention": [
            "Use resistant hybrids, the most reliable long-term control.",
            "Rotate away from corn for at least one season in heavily infected fields.",
            "Manage crop residue through tillage to speed decomposition of infected debris.",
        ],
        "severity": "High",
        "organic": "Resistant hybrids plus residue management are the main organic-compatible strategies.",
    },
    "Corn (maize) - healthy": {
        "symptoms": ["No disease symptoms observed.", "Leaves show uniform green color with no lesions or spotting.", "Normal stalk and leaf development."],
        "treatment": ["No treatment needed.", "Maintain balanced nitrogen and irrigation schedule.", "Continue routine field scouting."],
        "prevention": ["Rotate crops each season to limit disease buildup.", "Scout regularly during humid weather.", "Manage residue from previous corn crops."],
        "severity": "None",
        "organic": "No intervention necessary — healthy foliage detected.",
    },

    # ---------------- GRAPE ----------------
    "Grape - Black rot": {
        "symptoms": [
            "Small tan spots with dark borders on leaves, often circular.",
            "Fruit shrivels into hard, black 'mummies' as rot progresses.",
            "Black pycnidia (fungal fruiting bodies) visible on lesions.",
        ],
        "treatment": [
            "Remove and destroy mummified berries and infected leaves promptly.",
            "Apply fungicide sprays from bud break through fruit set during wet seasons.",
            "Prune to open the canopy and reduce prolonged leaf wetness.",
        ],
        "prevention": [
            "Practice thorough sanitation — remove all mummies from the vineyard floor and vines.",
            "Train vines for good airflow and sun exposure.",
            "Monitor closely during warm, humid weather when infection risk peaks.",
        ],
        "severity": "High",
        "organic": "Copper or sulfur-based sprays combined with strict sanitation are the main organic controls.",
    },
    "Grape - Esca (Black Measles)": {
        "symptoms": [
            "Tiger-stripe pattern of yellow and brown streaks between leaf veins.",
            "Small dark spots on berries, sometimes called 'black measles'.",
            "Vines may show sudden wilting (apoplexy) in severe cases.",
        ],
        "treatment": [
            "No curative fungicide exists; focus on removing and destroying severely affected wood.",
            "Prune out and burn dead or diseased cordons to slow internal spread.",
            "Apply wound protectants to pruning cuts to limit new infections.",
        ],
        "prevention": [
            "Avoid pruning during wet weather, when infection risk is highest.",
            "Use clean, sterilized tools between vines.",
            "Consider trunk renewal on severely infected old vines.",
        ],
        "severity": "High",
        "organic": "Sanitation and wound protection are the only organic-compatible measures; there is no organic cure once established.",
    },
    "Grape - Leaf blight (Isariopsis Leaf Spot)": {
        "symptoms": [
            "Dark brown, angular spots on leaves that can merge into larger blighted areas.",
            "Premature yellowing and defoliation in severe infections.",
            "Reduced vine vigor and photosynthetic capacity over the season.",
        ],
        "treatment": [
            "Apply fungicide sprays during periods of high humidity or rainfall.",
            "Remove fallen infected leaves at the end of the season.",
            "Improve canopy airflow through selective pruning.",
        ],
        "prevention": [
            "Maintain good vineyard sanitation and residue management.",
            "Avoid excessive canopy density that traps moisture.",
            "Monitor closely in humid climates or during rainy growing seasons.",
        ],
        "severity": "Medium",
        "organic": "Copper-based fungicides applied preventatively can help manage this disease organically.",
    },
    "Grape - healthy": {
        "symptoms": ["No disease symptoms observed.", "Leaves show normal green color and shape.", "Vine growth appears vigorous and typical."],
        "treatment": ["No treatment needed.", "Maintain regular irrigation and canopy management.", "Continue routine monitoring through the growing season."],
        "prevention": ["Prune annually for good airflow.", "Remove fallen leaves and debris each season.", "Scout during humid weather for early disease signs."],
        "severity": "None",
        "organic": "No intervention necessary — healthy foliage detected.",
    },

    # ---------------- ORANGE ----------------
    "Orange - Haunglongbing (Citrus greening)": {
        "symptoms": [
            "Blotchy, asymmetric yellow mottling on leaves (unlike symmetric nutrient deficiency patterns).",
            "Small, lopsided, bitter-tasting fruit that stays partially green.",
            "Progressive twig dieback and gradual tree decline.",
        ],
        "treatment": [
            "There is no cure — infected trees should be removed to prevent further spread.",
            "Control the Asian citrus psyllid, the insect vector, using recommended insecticide programs.",
            "Report suspected cases to local agricultural authorities, as this is a regulated disease in many regions.",
        ],
        "prevention": [
            "Buy certified disease-free nursery stock only.",
            "Monitor and manage psyllid populations proactively.",
            "Remove and destroy confirmed infected trees quickly to protect neighboring healthy trees.",
        ],
        "severity": "Critical",
        "organic": "No organic cure exists; organic psyllid control (e.g. horticultural oils) can slow spread but not stop it.",
    },

    # ---------------- PEACH ----------------
    "Peach - Bacterial spot": {
        "symptoms": [
            "Small, dark, water-soaked spots on leaves that may drop out, leaving a 'shot-hole' appearance.",
            "Sunken, dark lesions on fruit surface, sometimes cracking.",
            "Defoliation can occur in severe, wet-weather outbreaks.",
        ],
        "treatment": [
            "Apply copper-based bactericides during dormant and early growing season.",
            "Avoid overhead irrigation, which spreads bacteria via water splash.",
            "Prune out and destroy severely infected twigs and shoots.",
        ],
        "prevention": [
            "Plant bacterial spot-resistant peach varieties where available.",
            "Avoid working in orchards when foliage is wet.",
            "Maintain balanced fertility — excess nitrogen increases susceptibility.",
        ],
        "severity": "High",
        "organic": "Copper sprays are an accepted organic control, best applied preventatively before bud break.",
    },
    "Peach - healthy": {
        "symptoms": ["No disease symptoms observed.", "Leaves are uniformly green with no spotting.", "Normal shoot and fruit development."],
        "treatment": ["No treatment needed.", "Continue regular watering and fertilization.", "Monitor during wet spring weather for early bacterial spot signs."],
        "prevention": ["Prune for airflow and sunlight penetration.", "Avoid overhead watering.", "Choose resistant varieties for future plantings."],
        "severity": "None",
        "organic": "No intervention necessary — healthy foliage detected.",
    },

    # ---------------- BELL PEPPER ----------------
    "Pepper, bell - Bacterial spot": {
        "symptoms": [
            "Small, water-soaked spots on leaves that turn brown with a yellow halo.",
            "Raised, scabby lesions on fruit surface.",
            "Leaf drop and reduced yield in severe infections.",
        ],
        "treatment": [
            "Apply copper-based bactericides at first sign of spotting.",
            "Remove and destroy infected plant debris after harvest.",
            "Avoid handling plants when wet to reduce bacterial spread.",
        ],
        "prevention": [
            "Use certified disease-free seed and transplants.",
            "Practice crop rotation with non-host plants for at least two years.",
            "Avoid overhead irrigation and dense planting.",
        ],
        "severity": "High",
        "organic": "Copper-based sprays combined with crop rotation are the standard organic approach.",
    },
    "Pepper, bell - healthy": {
        "symptoms": ["No disease symptoms observed.", "Leaves show uniform green color and healthy texture.", "Normal plant vigor and fruit set."],
        "treatment": ["No treatment needed.", "Maintain consistent watering and balanced fertilization.", "Continue periodic scouting for early symptoms."],
        "prevention": ["Rotate crops each season.", "Use disease-free seed sources.", "Avoid working with wet foliage."],
        "severity": "None",
        "organic": "No intervention necessary — healthy foliage detected.",
    },

    # ---------------- POTATO ----------------
    "Potato - Early blight": {
        "symptoms": [
            "Dark brown spots with concentric 'target board' rings, usually on older/lower leaves first.",
            "Yellowing of tissue surrounding the lesions.",
            "Can spread upward, reducing overall plant vigor and tuber yield.",
        ],
        "treatment": [
            "Apply a labeled fungicide at first symptom appearance and repeat per label interval.",
            "Remove severely infected lower leaves to slow upward spread.",
            "Ensure adequate plant nutrition, as stressed plants are more susceptible.",
        ],
        "prevention": [
            "Rotate with non-solanaceous crops for at least two seasons.",
            "Avoid overhead irrigation late in the day.",
            "Space plants adequately for good airflow.",
        ],
        "severity": "High",
        "organic": "Copper-based fungicides and strict crop rotation are effective organic controls.",
    },
    "Potato - Late blight": {
        "symptoms": [
            "Dark, water-soaked lesions on leaves that expand rapidly, often with white fungal growth on the underside in humid conditions.",
            "Blackened, collapsing foliage that can destroy a field within days under favorable weather.",
            "Brown, granular rot on tubers that can continue in storage.",
        ],
        "treatment": [
            "Apply fungicide immediately at first sign — this disease spreads extremely fast.",
            "Destroy infected plants and volunteer potatoes to remove inoculum sources.",
            "Harvest tubers only after foliage is fully dead to reduce tuber infection.",
        ],
        "prevention": [
            "Plant certified disease-free seed potatoes only.",
            "Monitor weather forecasts — cool, wet conditions favor rapid outbreaks.",
            "Destroy cull piles and volunteer plants that can harbor the pathogen between seasons.",
        ],
        "severity": "Critical",
        "organic": "Copper-based fungicides can help but are far less effective than synthetic options once late blight is established — early prevention is critical.",
    },
    "Potato - healthy": {
        "symptoms": ["No disease symptoms observed.", "Leaves are healthy green with no lesions or spotting.", "Normal foliage and tuber development."],
        "treatment": ["No treatment needed.", "Maintain balanced watering and fertility.", "Continue scouting, especially during cool, wet weather."],
        "prevention": ["Rotate crops away from potato/tomato family plants.", "Use certified disease-free seed potatoes.", "Monitor closely during humid conditions."],
        "severity": "None",
        "organic": "No intervention necessary — healthy foliage detected.",
    },

    # ---------------- RASPBERRY ----------------
    "Raspberry - healthy": {
        "symptoms": ["No disease symptoms observed.", "Canes and leaves show normal healthy growth.", "No spotting, wilting, or discoloration present."],
        "treatment": ["No treatment needed.", "Maintain regular watering and pruning schedule.", "Continue periodic monitoring."],
        "prevention": ["Prune out old canes after fruiting to improve airflow.", "Avoid overhead irrigation.", "Space canes adequately to reduce humidity buildup."],
        "severity": "None",
        "organic": "No intervention necessary — healthy foliage detected.",
    },

    # ---------------- SOYBEAN ----------------
    "Soybean - healthy": {
        "symptoms": ["No disease symptoms observed.", "Leaves show uniform green color and healthy trifoliate structure.", "Normal plant height and pod development."],
        "treatment": ["No treatment needed.", "Maintain standard irrigation and nutrient program.", "Continue field scouting through the season."],
        "prevention": ["Rotate crops to reduce disease pressure.", "Use certified, disease-free seed.", "Scout regularly, especially during humid conditions."],
        "severity": "None",
        "organic": "No intervention necessary — healthy foliage detected.",
    },

    # ---------------- SQUASH ----------------
    "Squash - Powdery mildew": {
        "symptoms": [
            "White, powdery fungal patches on upper and lower leaf surfaces.",
            "Leaves may yellow, curl, and die prematurely as infection spreads.",
            "Reduced fruit size and quality due to loss of photosynthetic leaf area.",
        ],
        "treatment": [
            "Apply sulfur, potassium bicarbonate, or a labeled fungicide at first sign of white patches.",
            "Remove and destroy heavily infected leaves to slow spread.",
            "Improve airflow by thinning dense foliage.",
        ],
        "prevention": [
            "Choose powdery mildew-resistant squash varieties.",
            "Avoid overhead watering, especially late in the day.",
            "Space plants adequately to reduce humidity around foliage.",
        ],
        "severity": "Medium",
        "organic": "Potassium bicarbonate, sulfur, or neem oil sprays are effective organic treatments for powdery mildew.",
    },

    # ---------------- STRAWBERRY ----------------
    "Strawberry - Leaf scorch": {
        "symptoms": [
            "Small, irregular purple to dark red blotches on leaves.",
            "Blotches enlarge and merge, giving leaves a scorched, dried appearance.",
            "Reduced plant vigor and fruit yield in severe infections.",
        ],
        "treatment": [
            "Remove and destroy infected leaves, especially after harvest.",
            "Apply a labeled fungicide if the disease is widespread in the planting.",
            "Renovate beds after fruiting by mowing and removing old foliage.",
        ],
        "prevention": [
            "Choose leaf scorch-resistant strawberry varieties.",
            "Avoid overhead irrigation; use drip irrigation where possible.",
            "Space plants for good airflow and sunlight penetration.",
        ],
        "severity": "Medium",
        "organic": "Copper-based fungicides and prompt removal of infected leaves are the primary organic controls.",
    },
    "Strawberry - healthy": {
        "symptoms": ["No disease symptoms observed.", "Leaves show healthy green color with no blotching.", "Normal runner and fruit development."],
        "treatment": ["No treatment needed.", "Maintain consistent watering and fertility.", "Continue routine monitoring through the season."],
        "prevention": ["Renovate beds after harvest each year.", "Use drip irrigation instead of overhead watering.", "Space plants to maintain good airflow."],
        "severity": "None",
        "organic": "No intervention necessary — healthy foliage detected.",
    },

    # ---------------- TOMATO ----------------
    "Tomato - Bacterial spot": {
        "symptoms": [
            "Small, dark, greasy-looking spots on leaves, often with a yellow halo.",
            "Raised, scabby spots on fruit surface.",
            "Leaf drop can occur under warm, humid, and rainy conditions.",
        ],
        "treatment": [
            "Apply copper-based bactericides at first sign of spotting.",
            "Remove and destroy severely infected plant material.",
            "Avoid working with plants when foliage is wet.",
        ],
        "prevention": [
            "Use certified disease-free seed and transplants.",
            "Rotate crops away from tomato/pepper family for at least two years.",
            "Avoid overhead irrigation and excessive plant crowding.",
        ],
        "severity": "High",
        "organic": "Copper sprays combined with strict sanitation are the standard organic-compatible approach.",
    },
    "Tomato - Early blight": {
        "symptoms": [
            "Dark brown spots with concentric target-like rings, typically starting on lower/older leaves.",
            "Yellowing around lesions, leading to leaf drop as infection progresses.",
            "Can also cause dark, sunken lesions on stems and fruit.",
        ],
        "treatment": [
            "Apply a labeled fungicide at first symptom appearance, repeating per label interval.",
            "Remove infected lower leaves to slow upward spread.",
            "Stake or cage plants to keep foliage off the ground and improve airflow.",
        ],
        "prevention": [
            "Rotate crops with non-solanaceous plants for at least two seasons.",
            "Mulch around plants to reduce soil splash onto lower leaves.",
            "Avoid overhead watering; water at the base instead.",
        ],
        "severity": "High",
        "organic": "Copper-based fungicides and consistent crop rotation are the main organic-compatible strategies.",
    },
    "Tomato - Late blight": {
        "symptoms": [
            "Large, water-soaked, dark green to brown lesions on leaves that expand rapidly.",
            "White fungal growth visible on the underside of lesions in humid conditions.",
            "Firm, brown, greasy-looking rot on fruit that can spread quickly.",
        ],
        "treatment": [
            "Apply fungicide immediately upon detection — this disease can destroy a crop within days.",
            "Remove and destroy infected plants promptly to limit spread.",
            "Avoid working in wet fields, which can spread spores between plants.",
        ],
        "prevention": [
            "Plant certified disease-free transplants.",
            "Monitor local blight forecasts, since cool, wet weather greatly increases risk.",
            "Ensure good airflow through proper plant spacing and staking.",
        ],
        "severity": "Critical",
        "organic": "Copper-based fungicides applied preventatively can help but are less effective once infection is established — early detection is essential.",
    },
    "Tomato - Leaf Mold": {
        "symptoms": [
            "Pale green to yellow spots on the upper leaf surface.",
            "Olive-green to grayish-purple fuzzy mold visible on the underside of leaves.",
            "Most common in humid greenhouse or high-tunnel conditions.",
        ],
        "treatment": [
            "Improve ventilation to reduce humidity around plants.",
            "Apply a labeled fungicide if the infection is spreading rapidly.",
            "Remove and destroy heavily infected leaves.",
        ],
        "prevention": [
            "Space plants well and prune lower leaves to increase airflow.",
            "Avoid overhead watering and reduce greenhouse humidity where possible.",
            "Choose leaf mold-resistant tomato varieties for enclosed growing.",
        ],
        "severity": "Medium",
        "organic": "Improving airflow and humidity control is the primary organic control; copper sprays offer additional suppression.",
    },
    "Tomato - Septoria leaf spot": {
        "symptoms": [
            "Small, circular spots with dark borders and light gray or tan centers, often with tiny black specks inside.",
            "Lesions typically appear on lower leaves first and spread upward.",
            "Severe infections cause significant leaf yellowing and drop.",
        ],
        "treatment": [
            "Apply a labeled fungicide at first symptom appearance.",
            "Remove and destroy infected lower leaves as they appear.",
            "Mulch soil to reduce spore splash onto foliage.",
        ],
        "prevention": [
            "Rotate crops away from tomato family plants for at least one to two years.",
            "Avoid overhead watering; water at the soil level instead.",
            "Stake plants to keep foliage off the ground.",
        ],
        "severity": "Medium",
        "organic": "Copper-based fungicides and consistent mulching/sanitation are effective organic measures.",
    },
    "Tomato - Spider mites Two-spotted spider mite": {
        "symptoms": [
            "Fine yellow stippling or speckling on leaves, giving a dusty, bronzed appearance.",
            "Fine webbing visible on the underside of leaves or between stems in heavy infestations.",
            "Leaves may curl, dry out, and drop under severe infestation.",
        ],
        "treatment": [
            "Spray plants with a strong stream of water to physically dislodge mites.",
            "Apply insecticidal soap or horticultural oil, targeting the undersides of leaves.",
            "Introduce natural predators such as predatory mites in greenhouse settings.",
        ],
        "prevention": [
            "Avoid drought-stressing plants, since mites thrive in hot, dry conditions.",
            "Monitor regularly during hot weather, checking leaf undersides for early stippling.",
            "Avoid excessive use of broad-spectrum insecticides that kill natural mite predators.",
        ],
        "severity": "Medium",
        "organic": "Insecticidal soap, horticultural oil, and predatory mites are all accepted organic controls.",
    },
    "Tomato - Target Spot": {
        "symptoms": [
            "Brown lesions with concentric rings, similar in appearance to early blight, on leaves, stems, and fruit.",
            "Lesions can merge, causing significant leaf blight and defoliation.",
            "Fruit lesions appear as sunken, dark spots that can enlarge over time.",
        ],
        "treatment": [
            "Apply a labeled fungicide at first symptom appearance.",
            "Remove and destroy heavily infected plant debris.",
            "Improve airflow through proper staking and pruning.",
        ],
        "prevention": [
            "Rotate crops with non-host plants each season.",
            "Avoid overhead irrigation and dense plant spacing.",
            "Remove crop residue thoroughly after harvest.",
        ],
        "severity": "Medium",
        "organic": "Copper-based fungicides combined with good sanitation practices help manage target spot organically.",
    },
    "Tomato - Tomato Yellow Leaf Curl Virus": {
        "symptoms": [
            "Upward curling and yellowing of leaf margins, giving a cupped appearance.",
            "Stunted plant growth and reduced fruit set.",
            "Spread primarily by whitefly insect vectors.",
        ],
        "treatment": [
            "There is no cure — remove and destroy infected plants to prevent further spread.",
            "Control whitefly populations using insecticidal soap, sticky traps, or approved insecticides.",
            "Avoid planting new tomatoes near heavily infected fields.",
        ],
        "prevention": [
            "Plant virus-resistant tomato varieties where available.",
            "Use reflective mulches or row covers to deter whiteflies.",
            "Control whitefly populations proactively throughout the season.",
        ],
        "severity": "Critical",
        "organic": "No organic cure exists; managing the whitefly vector with insecticidal soaps and row covers is the main organic-compatible defense.",
    },
    "Tomato - Tomato mosaic virus": {
        "symptoms": [
            "Mottled light and dark green mosaic patterning on leaves.",
            "Leaf distortion, curling, and stunted plant growth.",
            "Fruit may show uneven ripening or internal browning.",
        ],
        "treatment": [
            "There is no cure — remove and destroy infected plants to prevent spread.",
            "Disinfect tools and hands after handling infected plants, since the virus spreads easily by contact.",
            "Avoid using tobacco products near plants, as the virus can be tobacco-transmitted.",
        ],
        "prevention": [
            "Use certified virus-free seed and resistant varieties where available.",
            "Wash hands and sanitize tools between handling different plants.",
            "Control aphids and other insects that can spread the virus.",
        ],
        "severity": "Critical",
        "organic": "No organic cure exists; strict sanitation and resistant varieties are the only effective organic-compatible prevention.",
    },
    "Tomato - healthy": {
        "symptoms": ["No disease symptoms observed.", "Leaves show uniform green color and healthy structure.", "Normal plant vigor and fruit development."],
        "treatment": ["No treatment needed.", "Maintain consistent watering and balanced fertilization.", "Continue routine scouting through the growing season."],
        "prevention": ["Rotate crops each season to reduce disease buildup.", "Water at the base to keep foliage dry.", "Stake or cage plants for good airflow."],
        "severity": "None",
        "organic": "No intervention necessary — healthy foliage detected.",
    },
}
