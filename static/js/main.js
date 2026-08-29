// =================================================================
// LeafLens AI — shared front-end behavior (theme, toasts, nav, transitions)
// =================================================================

(function () {
  // ---------------- Dark mode ----------------
  const root = document.documentElement;
  const themeToggle = document.getElementById("themeToggle");
  const savedTheme = localStorage.getItem("leaflens-theme") || "light";
  root.setAttribute("data-theme", savedTheme);

  if (themeToggle) {
    themeToggle.addEventListener("click", () => {
      const current = root.getAttribute("data-theme");
      const next = current === "dark" ? "light" : "dark";
      root.setAttribute("data-theme", next);
      localStorage.setItem("leaflens-theme", next);
    });
  }

  // ---------------- Mobile nav ----------------
  const navToggle = document.getElementById("navToggle");
  const navLinks = document.getElementById("navLinks");
  if (navToggle && navLinks) {
    navToggle.addEventListener("click", () => {
      navLinks.classList.toggle("open");
    });
    navLinks.querySelectorAll("a").forEach((link) => {
      link.addEventListener("click", () => navLinks.classList.remove("open"));
    });
  }

  // ---------------- Toasts (rendered from server-side flash messages) ----------------
  function showToast(message, category) {
    const container = document.getElementById("toastContainer");
    if (!container) return;

    const toast = document.createElement("div");
    toast.className = `toast ${category === "error" ? "error" : "success"}`;
    const icon = category === "error" ? "⚠️" : "✅";
    toast.innerHTML = `<span>${icon}</span><span>${message}</span>`;
    container.appendChild(toast);

    setTimeout(() => {
      toast.classList.add("leaving");
      setTimeout(() => toast.remove(), 300);
    }, 4500);
  }

  const flashInit = document.querySelector(".flash-init");
  if (flashInit) {
    flashInit.querySelectorAll("[data-category]").forEach((el) => {
      showToast(el.textContent, el.getAttribute("data-category"));
    });
  }

  window.LeafLens = window.LeafLens || {};
  window.LeafLens.showToast = showToast;

  // ---------------- Smooth internal page transitions ----------------
  const pageContent = document.getElementById("pageContent");
  document.querySelectorAll('a[href^="/"]').forEach((link) => {
    link.addEventListener("click", (e) => {
      const href = link.getAttribute("href");
      if (!href || href.startsWith("#") || link.target === "_blank") return;
      e.preventDefault();
      if (pageContent) pageContent.classList.add("leaving");
      setTimeout(() => { window.location.href = href; }, 150);
    });
  });
})();
