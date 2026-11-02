/* Whitmore & Hale LLP — local interaction layer.
   Uses only the vendored Bootstrap, GSAP and ScrollTrigger files. */
(function () {
  "use strict";

  const $ = (selector, scope) => (scope || document).querySelector(selector);
  const $$ = (selector, scope) => Array.from((scope || document).querySelectorAll(selector));
  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  const practiceAreas = {
    corporate: {
      title: "Corporate & Transactions",
      icon: "ph-buildings",
      intro: "Practical counsel for formations, governance, financings, acquisitions and the decisions that change a company's trajectory.",
      overview: "We advise founders, boards, private companies and institutional investors through ordinary-course decisions and consequential transactions. Our approach is deliberately senior-led: the lawyer who scopes the matter stays with the file through signing and closing.",
      services: ["Mergers, acquisitions and divestitures", "Private placements and venture financings", "Corporate governance and board advice", "Commercial contracts and joint ventures", "Shareholder and partnership agreements", "Cross-border structuring"],
      approach: "A transaction is only as sound as its assumptions. We begin with the commercial objective, identify regulatory and tax touchpoints early, and keep a disciplined issues list so that business teams can make decisions without losing momentum.",
      experience: "Represented a New York middle-market technology group in a $180 million acquisition and simultaneous credit-facility refinancing, coordinating diligence across three jurisdictions."
    },
    litigation: {
      title: "Commercial Litigation",
      icon: "ph-gavel",
      intro: "Trial-ready representation in contract, business-tort, fiduciary and appellate disputes in New York and Massachusetts courts.",
      overview: "Our litigators are engaged early, often while a dispute can still be resolved quietly. When a negotiated resolution is not in the client's interest, we build a record designed for motion practice, trial and appeal from the first day.",
      services: ["Complex contract and partnership disputes", "Business torts and fraud claims", "Fiduciary-duty and governance litigation", "Emergency injunctive relief", "Arbitration and mediation", "Appellate advocacy"],
      approach: "We align the litigation plan with a defined business outcome, budget the work in phases, and give clients a candid view of risk at each decision point. Associates handle research and discovery under close partner supervision.",
      experience: "Obtained dismissal with prejudice of a $45 million fraud claim after targeted motion practice, then defended the judgment on appeal."
    },
    tax: {
      title: "Tax Planning & Controversy",
      icon: "ph-currency-dollar",
      intro: "Federal, state and international tax planning for closely held companies, executives, funds and private clients.",
      overview: "Tax advice works best when it is integrated with the transaction rather than appended to it. We model consequences before documents are drafted and coordinate with accountants to keep implementation precise.",
      services: ["Transactional tax structuring", "State and local tax nexus", "Executive compensation and equity", "IRS and New York State audits", "Private-client and estate planning", "Voluntary disclosure and penalties"],
      approach: "Our memos are written for decision-makers: a clear conclusion, the assumptions behind it, quantified alternatives, and a practical implementation checklist for the client's finance team.",
      experience: "Restructured a multi-state operating group before sale, resolving open audit questions and preserving a favorable allocation of purchase price."
    },
    realestate: {
      title: "Real Estate & Finance",
      icon: "ph-city",
      intro: "Acquisitions, leasing, development and secured lending for owners, operators, lenders and institutional investors.",
      overview: "From Manhattan commercial leases to portfolio financings, we manage the legal detail that determines whether a real-estate transaction closes on time and performs after closing.",
      services: ["Commercial acquisitions and dispositions", "Office, retail and industrial leasing", "Construction and development agreements", "Mortgage and mezzanine lending", "Land-use and zoning diligence", "Workouts and distressed assets"],
      approach: "We coordinate title, survey, zoning, environmental and lending workstreams through one issues matrix, so the business team sees dependencies before they become closing conditions.",
      experience: "Counseled a regional lender on a $260 million secured credit facility secured by a mixed-use portfolio across New York and Massachusetts."
    },
    family: {
      title: "Family & Private Client",
      icon: "ph-users-three",
      intro: "Discreet, careful counsel for business owners and families on succession, marital agreements and private wealth matters.",
      overview: "Private-client work often intersects with a operating business, real property and multigenerational planning. We work alongside the client's accountant and investment adviser to keep every document consistent.",
      services: ["Prenuptial and postnuptial agreements", "Estate and trust planning", "Business succession", "Family governance", "Probate and fiduciary disputes", "Charitable giving"],
      approach: "Sensitivity and precision matter equally. We keep the circle of communication small, explain trade-offs plainly, and produce documents that fiduciaries can administer without avoidable ambiguity.",
      experience: "Designed a succession structure for a second-generation family business, aligning voting control, liquidity and charitable objectives."
    },
    intellectualproperty: {
      title: "Intellectual Property",
      icon: "ph-lightbulb",
      intro: "Protection and commercialization of brands, software, creative assets and proprietary data across traditional and emerging markets.",
      overview: "We treat intellectual property as a business asset, not a standalone filing exercise. The work includes clearance, ownership discipline, licensing, enforcement and diligence in financing or exit transactions.",
      services: ["Trademark clearance and prosecution", "Software and content licensing", "Trade-secret programs", "IP due diligence", "Brand enforcement and opposition", "Data, privacy and AI-use policies"],
      approach: "We start with an inventory of what the client actually owns, close assignment and contractor gaps, then build a protection program proportionate to the commercial value of each asset.",
      experience: "Completed IP diligence for a venture financing and remediated contractor-assignment gaps before closing."
    },
    employment: {
      title: "Employment & Investigations",
      icon: "ph-briefcase",
      intro: "Counsel on the hiring, management, separation and investigation issues that carry legal and reputational consequences.",
      overview: "Our team advises boards, executives and human-resources leaders on compliance, sensitive workplace investigations, restrictive covenants and disputes before they become litigation.",
      services: ["Workplace investigations", "Executive employment agreements", "Restrictive covenants", "Wage-and-hour compliance", "Reductions in force", "Discrimination and retaliation defense"],
      approach: "We establish a defensible process at the outset: a clear scope, privilege protocol, document-preservation plan and a report that answers the questions the decision-maker actually asked.",
      experience: "Conducted an independent board-level investigation and advised on remediation without interrupting a live financing."
    },
    banking: {
      title: "Banking & Regulatory",
      icon: "ph-bank",
      intro: "Regulatory, lending and enforcement counsel for financial institutions, fintech companies and corporate borrowers.",
      overview: "We help clients navigate examination findings, licensing questions, product launches and complex credit documentation with advice that accounts for both legal text and supervisory expectations.",
      services: ["Bank regulatory examinations", "Fintech licensing and partnerships", "Secured and unsecured lending", "AML and sanctions programs", "Enforcement responses", "Consumer-finance compliance"],
      approach: "Regulatory advice must be operational. We translate requirements into owners, controls and evidence, and we coordinate with compliance teams so an answer can be implemented and tested.",
      experience: "Guided a payments business through a multi-state licensing review and a bank-partner agreement renegotiation."
    }
  };

  const attorneys = {
    eleanor: {
      name: "Eleanor Whitmore",
      role: "Managing Partner · Corporate & Transactions",
      image: "assets/images/partner-eleanor.jpg",
      practice: "Corporate & Transactions",
      admissions: "New York · Massachusetts",
      education: "J.D., Columbia Law School · B.A., Wellesley College",
      email: "ewhitmore@whitmore-hale.com",
      bio: [
        "Eleanor advises boards, founders and investors on acquisitions, governance and growth financings. She is known for taking complex, multi-party transactions apart early, agreeing a realistic timetable, and keeping the negotiating team focused on the provisions that will matter after closing.",
        "Before founding the firm's corporate group, she spent a decade in the New York office of a national firm and served as outside general counsel to a family-owned manufacturing group. She now chairs the firm's conflicts and client-service committees and leads transaction teams across the New York and Boston offices."
      ],
      focus: ["Mergers & acquisitions", "Private capital", "Board governance", "Cross-border transactions"],
      note: "Selected by Best Lawyers for corporate law, 2021–2026."
    },
    arthur: {
      name: "Arthur Hale",
      role: "Founding Partner · Commercial Litigation",
      image: "assets/images/partner-arthur.jpg",
      practice: "Commercial Litigation",
      admissions: "New York · Massachusetts · U.S. Supreme Court",
      education: "J.D., Harvard Law School · B.A., Amherst College",
      email: "ahale@whitmore-hale.com",
      bio: [
        "Arthur has tried commercial disputes in state and federal courts for more than three decades. His practice centers on contract, fiduciary-duty and business-tort matters, frequently under compressed injunction schedules or in parallel with arbitration.",
        "He founded Whitmore & Hale in 1998 around a straightforward principle: clients should have a partner who understands both the record and the business objective. He continues to supervise every litigation matter accepted by the firm."
      ],
      focus: ["Trial practice", "Appellate advocacy", "Fiduciary disputes", "Arbitration"],
      note: "Martindale-Hubbell AV Preeminent rating."
    },
    marcus: {
      name: "Marcus Bennett",
      role: "Partner · Employment & Investigations",
      image: "assets/images/partner-marcus.jpg",
      practice: "Employment & Investigations",
      admissions: "New York · District of Columbia",
      education: "J.D., New York University School of Law · B.S., Howard University",
      email: "mbennett@whitmore-hale.com",
      bio: [
        "Marcus counsels boards and executive teams on sensitive workplace matters, from independent investigations to restrictive-covenant disputes. His work is shaped by a belief that process quality and clear communication are the best safeguards for an organization and the people in it.",
        "He also advises clients on compliance training, executive agreements and reductions in force, and regularly works with in-house employment counsel on multi-jurisdictional responses."
      ],
      focus: ["Investigations", "Executive agreements", "Compliance", "Employment defense"],
      note: "Frequent speaker on workplace investigation procedure."
    },
    claire: {
      name: "Claire Donovan",
      role: "Partner · Real Estate & Finance",
      image: "assets/images/partner-claire.jpg",
      practice: "Real Estate & Finance",
      admissions: "New York · Massachusetts",
      education: "J.D., Boston College Law School · B.A., Georgetown University",
      email: "cdonovan@whitmore-hale.com",
      bio: [
        "Claire represents owners, lenders and institutional investors in commercial real-estate transactions throughout the Northeast. Her work spans portfolio acquisitions, complex leasing, construction documentation and secured lending.",
        "Clients value her disciplined closing management and her ability to coordinate title, zoning, environmental and credit teams without losing sight of the commercial deal."
      ],
      focus: ["Commercial leasing", "Secured lending", "Development", "Portfolio transactions"],
      note: "Recognized by Super Lawyers in real-estate law."
    },
    daniel: {
      name: "Daniel Chen",
      role: "Counsel · Tax & Private Client",
      image: "assets/images/attorney-daniel.jpg",
      practice: "Tax Planning & Controversy",
      admissions: "New York · Massachusetts",
      education: "LL.M., NYU School of Law · J.D., Fordham Law",
      email: "dchen@whitmore-hale.com",
      bio: [
        "Daniel works with closely held businesses, executives and family offices on the tax consequences of transactions, compensation and succession. He also represents taxpayers in federal and New York State examinations.",
        "His planning memoranda are built around implementation: an explicit set of assumptions, a numerical comparison of alternatives, and a closing checklist for the client's advisers."
      ],
      focus: ["Transactional tax", "State and local tax", "Executive equity", "Tax controversy"],
      note: "Chairs the firm's tax working group."
    },
    julian: {
      name: "Julian Moretti",
      role: "Counsel · Intellectual Property",
      image: "assets/images/attorney-julian.jpg",
      practice: "Intellectual Property",
      admissions: "New York",
      education: "J.D., Cornell Law School · B.S., Rensselaer Polytechnic Institute",
      email: "jmoretti@whitmore-hale.com",
      bio: [
        "Julian helps software, media and consumer businesses build and protect IP portfolios. He handles licensing, trademark enforcement, ownership diligence and the policy questions raised by new data and AI tools.",
        "He works closely with the corporate group so that IP chain-of-title issues are resolved before financings and acquisitions rather than during closing."
      ],
      focus: ["Software licensing", "Trademarks", "Trade secrets", "Technology diligence"],
      note: "Advises the firm's pro bono clinic for small creative businesses."
    },
    amara: {
      name: "Amara Okafor",
      role: "Associate · Banking & Regulatory",
      image: "assets/images/attorney-amara.jpg",
      practice: "Banking & Regulatory",
      admissions: "New York",
      education: "J.D., Columbia Law School · B.A., University of Pennsylvania",
      email: "aokafor@whitmore-hale.com",
      bio: [
        "Amara advises financial institutions and payments companies on licensing, bank partnerships, examination responses and consumer-finance compliance. She also supports lenders in secured and unsecured credit transactions.",
        "Before law school she worked in bank operations, an experience that informs her emphasis on controls that can be documented, tested and explained to examiners."
      ],
      focus: ["Fintech licensing", "AML compliance", "Credit documentation", "Examinations"],
      note: "Co-author of the firm's regulatory update series."
    },
    naomi: {
      name: "Naomi Adler",
      role: "Associate · Pro Bono & Family Law",
      image: "assets/images/attorney-naomi.jpg",
      practice: "Family & Private Client",
      admissions: "New York · Massachusetts",
      education: "J.D., Yale Law School · B.A., Brown University",
      email: "nadler@whitmore-hale.com",
      bio: [
        "Naomi works on private-client planning, marital agreements and the firm's pro bono housing and immigrant-entrepreneur matters. She coordinates the monthly legal clinic operated with a New York community partner.",
        "Her practice combines careful drafting with a calm, practical manner in matters that are often personal as well as legal."
      ],
      focus: ["Estate planning", "Marital agreements", "Housing clinic", "Nonprofit counsel"],
      note: "Firm pro bono fellow, 2024–2026."
    }
  };

  function setActiveNavigation() {
    const active = document.body.dataset.active;
    if (!active) return;
    $$("[data-nav]").forEach((link) => {
      if (link.dataset.nav === active) {
        link.classList.add("active");
        link.setAttribute("aria-current", "page");
      }
    });
  }

  function setCurrentYear() {
    const year = String(new Date().getFullYear());
    $$("[data-current-year]").forEach((el) => { el.textContent = year; });
  }

  function initializeLanguageToggle() {
    const buttons = $$("[data-lang-select]");
    const translatable = $$("[data-es]");
    if (!buttons.length || !translatable.length) return;

    translatable.forEach((el) => {
      if (!el.dataset.enHtml) el.dataset.enHtml = el.innerHTML;
    });

    const setLanguage = (lang, persist) => {
      const isSpanish = lang === "es";
      translatable.forEach((el) => {
        el.innerHTML = isSpanish ? el.dataset.es : el.dataset.enHtml;
      });
      buttons.forEach((button) => {
        const selected = button.dataset.langSelect === lang;
        button.classList.toggle("active", selected);
        button.setAttribute("aria-pressed", String(selected));
      });
      document.documentElement.lang = isSpanish ? "es" : "en";
      if (persist) {
        try { window.localStorage.setItem("wh-language", lang); } catch (_) { /* storage unavailable */ }
      }
    };

    buttons.forEach((button) => {
      button.addEventListener("click", () => setLanguage(button.dataset.langSelect, true));
    });

    let stored = "en";
    try { stored = window.localStorage.getItem("wh-language") || "en"; } catch (_) { /* storage unavailable */ }
    if (stored === "es") setLanguage("es", false);
  }

  function initializeSmoothAnchors() {
    const header = $(".site-header");
    $$('a[href^="#"]').forEach((link) => {
      const href = link.getAttribute("href");
      if (!href || href === "#" || link.hasAttribute("data-bs-toggle")) return;
      link.addEventListener("click", (event) => {
        const target = document.querySelector(href);
        if (!target) return;
        event.preventDefault();
        const offset = (header ? header.offsetHeight : 0) + 14;
        const top = target.getBoundingClientRect().top + window.scrollY - offset;
        window.scrollTo({ top, behavior: reduceMotion ? "auto" : "smooth" });
        window.history.replaceState(null, "", href);
        const collapse = document.getElementById("primaryNav");
        if (collapse && collapse.classList.contains("show") && window.bootstrap) {
          window.bootstrap.Collapse.getOrCreateInstance(collapse).hide();
        }
      });
    });
  }

  function initializeDemoForms() {
    $$("[data-demo-form]").forEach((form) => {
      form.addEventListener("submit", (event) => {
        event.preventDefault();
        if (!form.checkValidity()) {
          form.reportValidity();
          return;
        }
        const status = $("[data-form-status]", form) || $("[data-form-status]", form.closest(".modal") || document);
        if (status) {
          status.textContent = form.dataset.success || "Thank you. This demonstration form has been validated locally; connect a secure intake endpoint before publishing.";
          status.classList.add("is-visible");
        }
        form.reset();
      });
    });
  }

  function initializeTestimonialSlider() {
    $$("[data-slider]").forEach((slider) => {
      const slides = $$("[data-slide]", slider);
      const dots = $$("[data-slide-dot]", slider);
      if (slides.length < 2) return;
      let index = 0;

      const show = (next) => {
        index = (next + slides.length) % slides.length;
        slides.forEach((slide, i) => {
          const active = i === index;
          slide.classList.toggle("is-active", active);
          slide.setAttribute("aria-hidden", String(!active));
        });
        dots.forEach((dot, i) => {
          dot.classList.toggle("is-active", i === index);
          dot.setAttribute("aria-current", String(i === index));
        });
      };

      const prev = $("[data-slide-prev]", slider);
      const next = $("[data-slide-next]", slider);
      if (prev) prev.addEventListener("click", () => show(index - 1));
      if (next) next.addEventListener("click", () => show(index + 1));
      dots.forEach((dot, i) => dot.addEventListener("click", () => show(i)));
      slider.addEventListener("keydown", (event) => {
        if (event.key === "ArrowLeft") show(index - 1);
        if (event.key === "ArrowRight") show(index + 1);
      });
      show(0);
    });
  }

  function initializeFilters() {
    const tabs = $$("[data-filter]");
    const rows = $$("[data-category]");
    if (!tabs.length || !rows.length) return;
    tabs.forEach((tab) => {
      tab.addEventListener("click", () => {
        const category = tab.dataset.filter;
        tabs.forEach((item) => item.classList.toggle("is-active", item === tab));
        rows.forEach((row) => {
          row.hidden = !(category === "all" || row.dataset.category.split(" ").includes(category));
        });
      });
    });
  }

  function initializeFaqSearch() {
    const search = $("[data-faq-search]");
    const items = $$("[data-faq-item]");
    const empty = $("[data-faq-empty]");
    if (!search || !items.length) return;
    search.addEventListener("input", () => {
      const term = search.value.trim().toLowerCase();
      let visible = 0;
      items.forEach((item) => {
        const match = item.textContent.toLowerCase().includes(term);
        item.hidden = !match;
        if (match) visible += 1;
      });
      if (empty) empty.hidden = visible !== 0;
    });
  }

  function populatePracticeDetail() {
    const root = $("[data-practice-detail]");
    if (!root) return;
    const params = new URLSearchParams(window.location.search);
    const key = params.get("area") || "corporate";
    const area = practiceAreas[key] || practiceAreas.corporate;
    const icon = $("[data-detail-icon]", root);
    const title = $("[data-detail-title]", root);
    const intro = $("[data-detail-intro]", root);
    const crumb = $("[data-detail-crumb]", root);
    const content = $("[data-detail-content]", root);

    if (icon) icon.className = `ph ${area.icon}`;
    if (title) title.textContent = area.title;
    if (intro) intro.textContent = area.intro;
    if (crumb) crumb.textContent = area.title;

    if (content) {
      content.innerHTML = `
        <h2 id="overview">Overview</h2>
        <p>${area.overview}</p>
        <h2 id="services">How we help</h2>
        <ul class="service-list">${area.services.map((service) => `<li>${service}</li>`).join("")}</ul>
        <h2 id="approach">Our approach</h2>
        <p>${area.approach}</p>
        <h2 id="experience">Representative experience</h2>
        <p>${area.experience}</p>
        <div class="alert-legal mt-4">Past results do not guarantee a similar outcome. Matter descriptions are illustrative and do not identify clients without consent.</div>
      `;
    }

    $$("[data-detail-contact]").forEach((link) => {
      link.href = `contact.html?area=${encodeURIComponent(key)}#consultation`;
    });
    document.title = `${area.title} | Whitmore & Hale LLP`;
  }

  function populateAttorneyProfile() {
    const root = $("[data-attorney-profile]");
    if (!root) return;
    const params = new URLSearchParams(window.location.search);
    const key = params.get("attorney") || "eleanor";
    const attorney = attorneys[key] || attorneys.eleanor;

    const setText = (selector, value) => {
      const el = $(selector, root);
      if (el) el.textContent = value;
    };
    setText("[data-profile-name]", attorney.name);
    setText("[data-profile-role]", attorney.role);
    setText("[data-profile-practice]", attorney.practice);
    setText("[data-profile-admissions]", attorney.admissions);
    setText("[data-profile-education]", attorney.education);
    setText("[data-profile-note]", attorney.note);
    setText("[data-profile-crumb]", attorney.name);

    const photo = $("[data-profile-photo]", root);
    if (photo) {
      photo.src = attorney.image;
      photo.alt = `Representative portrait for ${attorney.name}`;
    }
    const bio = $("[data-profile-bio]", root);
    if (bio) bio.innerHTML = attorney.bio.map((paragraph) => `<p>${paragraph}</p>`).join("");
    const focus = $("[data-profile-focus]", root);
    if (focus) focus.innerHTML = attorney.focus.map((item) => `<li>${item}</li>`).join("");
    $$("[data-profile-email]", root).forEach((link) => {
      link.href = `mailto:${attorney.email}?subject=Consultation%20request`;
      link.textContent = attorney.email;
    });
    document.title = `${attorney.name} | Whitmore & Hale LLP`;
  }

  function preselectContactArea() {
    const select = $("[data-practice-select]");
    if (!select) return;
    const params = new URLSearchParams(window.location.search);
    const key = params.get("area");
    if (key && practiceAreas[key]) select.value = practiceAreas[key].title;
  }

  function initializeGSAP() {
    if (reduceMotion || !window.gsap || !window.ScrollTrigger) return;
    const gsap = window.gsap;
    const ScrollTrigger = window.ScrollTrigger;
    gsap.registerPlugin(ScrollTrigger);
    document.documentElement.classList.add("gsap-ready");
    ScrollTrigger.config({ ignoreMobileResize: true });

    const heroImage = $(".hero-photo img");
    if (heroImage) {
      gsap.fromTo(heroImage,
        { scale: 1.02, xPercent: 0, yPercent: 0 },
        { scale: 1.12, xPercent: -1.5, yPercent: -1, duration: 22, ease: "sine.inOut", yoyo: true, repeat: -1 }
      );
    }

    $$("[data-reveal]").forEach((el) => {
      gsap.from(el, {
        autoAlpha: 0,
        y: 26,
        duration: 0.72,
        ease: "power2.out",
        scrollTrigger: { trigger: el, start: "top 88%", once: true }
      });
    });

    $$("[data-reveal-group]").forEach((group) => {
      gsap.from(Array.from(group.children), {
        autoAlpha: 0,
        y: 24,
        duration: 0.6,
        stagger: 0.09,
        ease: "power2.out",
        scrollTrigger: { trigger: group, start: "top 84%", once: true }
      });
    });

    $$(".mask-reveal").forEach((el) => {
      gsap.fromTo(el,
        { clipPath: "inset(0 100% 0 0)" },
        {
          clipPath: "inset(0 0% 0 0)",
          duration: 1.05,
          ease: "power3.out",
          scrollTrigger: { trigger: el, start: "top 82%", once: true }
        }
      );
    });

    const timeline = $(".process-timeline");
    const path = $(".timeline-svg path");
    if (timeline && path && typeof path.getTotalLength === "function") {
      const length = path.getTotalLength();
      gsap.set(path, { strokeDasharray: length, strokeDashoffset: length });
      gsap.to(path, {
        strokeDashoffset: 0,
        ease: "none",
        scrollTrigger: { trigger: timeline, start: "top 76%", end: "bottom 68%", scrub: 0.6 }
      });
    }

    const formatter = new Intl.NumberFormat("en-US");
    $$("[data-count]").forEach((el) => {
      const target = Number(el.dataset.count || 0);
      const prefix = el.dataset.prefix || "";
      const suffix = el.dataset.suffix || "";
      const counter = { value: 0 };
      gsap.to(counter, {
        value: target,
        duration: 1.8,
        ease: "power2.out",
        scrollTrigger: { trigger: el, start: "top 90%", once: true },
        onUpdate: () => {
          el.textContent = `${prefix}${formatter.format(Math.round(counter.value))}${suffix}`;
        }
      });
    });
  }

  function init() {
    setActiveNavigation();
    setCurrentYear();
    initializeLanguageToggle();
    initializeSmoothAnchors();
    initializeDemoForms();
    initializeTestimonialSlider();
    initializeFilters();
    initializeFaqSearch();
    populatePracticeDetail();
    populateAttorneyProfile();
    preselectContactArea();
    initializeGSAP();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
