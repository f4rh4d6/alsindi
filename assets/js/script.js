/* ============================================================
   THE SURVEY — Data Binding & Interaction Logic
   ============================================================ */

(function () {
  "use strict";

  // Load data immediately
  const siteData = typeof getSiteData === 'function' ? getSiteData() : {};

  // Simple nested key resolver (e.g., "identity.name" -> obj["identity"]["name"])
  function resolvePath(obj, path) {
    return path.split('.').reduce((prev, curr) => (prev ? prev[curr] : null), obj);
  }

  /* ---------- Data Binding ---------- */
  function applyDataBindings() {
    // Basic text bindings
    document.querySelectorAll('[data-bind]').forEach(el => {
      const path = el.getAttribute('data-bind');
      const val = resolvePath(siteData, path);
      if (val !== null && val !== undefined) {
        if (el.tagName === 'IMG') {
          el.src = val;
        } else {
          el.textContent = val;
        }
      }
    });

    // Page-specific specialized bindings

    // index.html
    const heroImg = document.getElementById('hero-img');
    if (heroImg && siteData.home) heroImg.src = siteData.home.heroImage;

    const statementParas = document.getElementById('statement-paras');
    if (statementParas && siteData.statement && siteData.statement.paragraphs) {
      statementParas.innerHTML = siteData.statement.paragraphs
        .map(p => `<p>${p}</p>`)
        .join('');
    }

    const galleryGrid = document.getElementById('gallery-grid');
    if (galleryGrid && siteData.photos) {
      galleryGrid.innerHTML = siteData.photos.map(photo => `
        <figure class="work" data-category="${photo.category}" data-title="${photo.title}" data-year="${photo.year}" data-caption="${photo.caption}">
          <div class="work-img">
            <img src="${photo.image}" alt="${photo.title}" width="1600" height="1200" loading="lazy" />
            <span class="work-num">${photo.num}</span>
          </div>
          <figcaption class="work-cap">
            <span class="title">${photo.title}</span>
            <span class="year">${photo.year}</span>
          </figcaption>
        </figure>
      `).join('');
    }

    // commentary.html
    const essayContainer = document.getElementById('essay-container');
    if (essayContainer && siteData.commentary && siteData.commentary.essay) {
      essayContainer.innerHTML = siteData.commentary.essay.map(section => `
        <h3 class="eyebrow" style="margin-top: 2rem; margin-bottom: 0.5rem; color: var(--ink)">${section.subhead}</h3>
        <p>${section.text}</p>
      `).join('');
    }

    // about.html
    const aboutImg = document.getElementById('about-img');
    if (aboutImg && siteData.about) aboutImg.src = siteData.about.portraitImage;

    const aboutParas = document.getElementById('about-paras');
    if (aboutParas && siteData.about && siteData.about.bioParagraphs) {
      aboutParas.innerHTML = siteData.about.bioParagraphs
        .map(p => `<p>${p}</p>`)
        .join('');
    }

    const aboutStats = document.getElementById('about-stats');
    if (aboutStats && siteData.about && siteData.about.stats) {
      aboutStats.innerHTML = siteData.about.stats.map(s => `
        <div class="stat">
          <b>${s.value}</b>
          <span>${s.label}</span>
        </div>
      `).join('');
    }

    const contactChannels = document.getElementById('contact-channels');
    if (contactChannels && siteData.contact && siteData.contact.channels) {
      contactChannels.innerHTML = siteData.contact.channels.map(c => `
        <li>
          <a href="${c.href}" ${c.href.startsWith('http') ? 'target="_blank" rel="noopener"' : ''}>
            <span>${c.value}</span>
            <span class="meta">${c.label} →</span>
          </a>
        </li>
      `).join('');
    }
  }

  // Run binding before continuing with interactivity
  applyDataBindings();

  /* ---------- Header scroll state ---------- */
  const header = document.getElementById('site-header');
  if (header && !header.classList.contains('scrolled')) {
    function updateHeader() {
      header.classList.toggle('scrolled', window.scrollY > 40);
    }
    window.addEventListener('scroll', updateHeader, { passive: true });
    updateHeader();
  }


  /* ---------- Gallery filtering ---------- */
  const filterButtons = document.querySelectorAll(".filter-btn");
  const works = document.querySelectorAll(".work");

  if (filterButtons.length && works.length) {
    function setFilter(category) {
      works.forEach((work) => {
        const match = category === "all" || work.dataset.category === category;
        work.classList.toggle("is-hidden", !match);
      });

      filterButtons.forEach((btn) => {
        const isActive = btn.dataset.filter === category;
        btn.setAttribute("aria-pressed", isActive ? "true" : "false");
      });
    }

    filterButtons.forEach((btn) => {
      btn.addEventListener("click", () => setFilter(btn.dataset.filter));
    });
  }

  /* ---------- Lightbox ---------- */
  const lightbox = document.getElementById("lightbox");
  if (lightbox && works.length) {
    const lightboxImg = document.getElementById("lightbox-img");
    const lightboxTitle = document.getElementById("lightbox-title");
    const lightboxCaption = document.getElementById("lightbox-caption");
    const closeBtn = document.getElementById("lightbox-close");
    const prevBtn = document.getElementById("lightbox-prev");
    const nextBtn = document.getElementById("lightbox-next");

    let visibleWorks = [];
    let currentIndex = 0;

    function openLightbox(work) {
      visibleWorks = Array.from(works).filter((w) => !w.classList.contains("is-hidden"));
      currentIndex = visibleWorks.indexOf(work);
      if (currentIndex === -1) currentIndex = 0;

      renderLightbox();
      lightbox.classList.add("is-open");
      document.body.style.overflow = "hidden";
      closeBtn.focus();
    }

    function renderLightbox() {
      const work = visibleWorks[currentIndex];
      if (!work) return;

      const img = work.querySelector("img");
      lightboxImg.src = img.src;
      lightboxImg.alt = img.alt;
      lightboxTitle.textContent = `${work.dataset.title} — ${work.dataset.year}`;
      lightboxCaption.textContent = work.dataset.caption || "";
    }

    function closeLightbox() {
      lightbox.classList.remove("is-open");
      document.body.style.overflow = "";
      if (visibleWorks[currentIndex]) visibleWorks[currentIndex].focus();
    }

    function step(dir) {
      if (!visibleWorks.length) return;
      currentIndex = (currentIndex + dir + visibleWorks.length) % visibleWorks.length;
      renderLightbox();
    }

    works.forEach((work) => {
      work.setAttribute("tabindex", "0");
      work.setAttribute("role", "button");
      work.setAttribute("aria-label", `View ${work.dataset.title}`);
      work.addEventListener("click", () => openLightbox(work));
      work.addEventListener("keydown", (e) => {
        if (e.key === "Enter" || e.key === " ") {
          e.preventDefault();
          openLightbox(work);
        }
      });
    });

    closeBtn.addEventListener("click", closeLightbox);
    prevBtn.addEventListener("click", () => step(-1));
    nextBtn.addEventListener("click", () => step(1));

    lightbox.addEventListener("click", (e) => {
      if (e.target === lightbox) closeLightbox();
    });

    document.addEventListener("keydown", (e) => {
      if (!lightbox.classList.contains("is-open")) return;
      if (e.key === "Escape") closeLightbox();
      if (e.key === "ArrowLeft") step(-1);
      if (e.key === "ArrowRight") step(1);
    });
  }
})();
