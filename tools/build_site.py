#!/usr/bin/env python3
"""Generate the 17 static HTML pages for Whitmore & Hale LLP.

The generated pages are intentionally self-contained and load only local
assets. Re-run after editing shared content:

    python3 tools/build_site.py
"""

from __future__ import annotations

from html import escape as h
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PRACTICES = [
    ("corporate", "Corporate & Transactions", "ph-buildings", "Mergers, financings, governance and commercial contracts for companies at every stage."),
    ("litigation", "Commercial Litigation", "ph-scales", "Trial-ready advocacy in contract, fiduciary and business-tort disputes."),
    ("tax", "Tax Planning & Controversy", "ph-currency-dollar", "Integrated federal, state and cross-border planning before and after a transaction."),
    ("realestate", "Real Estate & Finance", "ph-city", "Acquisitions, leasing, development and secured lending across the Northeast."),
    ("family", "Family & Private Client", "ph-users-three", "Discreet succession, marital-agreement and private-wealth counsel."),
    ("intellectualproperty", "Intellectual Property", "ph-lightbulb", "Ownership, licensing and enforcement for brands, software and data assets."),
    ("employment", "Employment & Investigations", "ph-briefcase", "Workplace investigations, executive agreements and employment defense."),
    ("banking", "Banking & Regulatory", "ph-bank", "Regulatory, credit and enforcement counsel for lenders and fintech companies."),
]

PARTNERS = [
    ("eleanor", "Eleanor Whitmore", "Managing Partner", "Corporate & Transactions", "partner-eleanor.jpg", "M&A and private capital"),
    ("arthur", "Arthur Hale", "Founding Partner", "Commercial Litigation", "partner-arthur.jpg", "Trials and appellate advocacy"),
    ("marcus", "Marcus Bennett", "Partner", "Employment & Investigations", "partner-marcus.jpg", "Investigations and compliance"),
    ("claire", "Claire Donovan", "Partner", "Real Estate & Finance", "partner-claire.jpg", "Leasing and secured lending"),
]

ATTORNEYS = [
    ("eleanor", "Eleanor Whitmore", "Managing Partner", "Corporate & Transactions", "partner-eleanor.jpg"),
    ("arthur", "Arthur Hale", "Founding Partner", "Commercial Litigation", "partner-arthur.jpg"),
    ("marcus", "Marcus Bennett", "Partner", "Employment & Investigations", "partner-marcus.jpg"),
    ("claire", "Claire Donovan", "Partner", "Real Estate & Finance", "partner-claire.jpg"),
    ("daniel", "Daniel Chen", "Counsel", "Tax & Private Client", "attorney-daniel.jpg"),
    ("julian", "Julian Moretti", "Counsel", "Intellectual Property", "attorney-julian.jpg"),
    ("amara", "Amara Okafor", "Associate", "Banking & Regulatory", "attorney-amara.jpg"),
    ("naomi", "Naomi Adler", "Associate", "Pro Bono & Family Law", "attorney-naomi.jpg"),
]

POSTS = [
    ("Fiduciary duties when a growth company misses its plan", "October 14, 2026", "Corporate", "assets/images/meeting-room.jpg", "A board's minutes, information rights and conflict protocol matter most when forecasts turn. A practical review of the record courts examine."),
    ("New York commercial lease assignment clauses after a sale", "September 28, 2026", "Real Estate", "assets/images/ny-office.jpg", "Consent standards, continuous-operation covenants and guaranty releases often determine the value embedded in a lease."),
    ("What an independent workplace investigation must preserve", "September 9, 2026", "Employment", "assets/images/contract-review.jpg", "Scope, privilege and document preservation should be settled before the first interview, not reconstructed later."),
    ("IP diligence gaps that delay venture financings", "August 21, 2026", "Intellectual Property", "assets/images/law-books.jpg", "Contractor assignments, open-source obligations and brand ownership are recurring sources of closing conditions."),
    ("Practical state-tax nexus review before a multi-state acquisition", "July 30, 2026", "Tax", "assets/images/library-interior.jpg", "A short pre-signing checklist for finance teams coordinating legal, accounting and operational data."),
    ("Arbitration clauses: small words with large consequences", "June 18, 2026", "Litigation", "assets/images/colonnade.jpg", "Delegation, seat, rules and emergency relief should be drafted as a coherent dispute-resolution system."),
]

FAQS = [
    ("How are legal fees structured?", "We generally work under hourly rates, fixed-fee phases or alternative arrangements depending on the matter. Rates are on request and are confirmed in a written engagement letter before work begins."),
    ("Do you offer an initial consultation?", "We offer a preliminary discussion at no charge to understand the matter, identify conflicts and determine whether the firm is the right fit. It is not legal advice and does not create an attorney-client relationship."),
    ("Which courts do you appear in?", "Our attorneys are admitted in New York and Massachusetts, with additional federal and appellate admissions listed on each attorney profile. We also coordinate local counsel for cross-border matters."),
    ("What should I bring to the first meeting?", "Bring the operative contracts, correspondence, court papers and a short timeline. A concise chronology is often more useful than an unfiltered document dump."),
    ("How do you handle conflicts of interest?", "A conflicts check is completed before substantive discussions. We use a centralized matter-opening process and will decline or seek a waiver where required by the applicable rules of professional conduct."),
    ("Can you guarantee a result?", "No. We can explain the law, the evidence and the likely range of outcomes, but past results and published case figures do not guarantee a similar outcome in another matter."),
]

RESULTS = [
    ("$12.4M", "Contract & Fraud", "Commercial Litigation", "Judgment after a six-week commercial trial for a New York manufacturing group.", "litigation"),
    ("$8.6M", "Shareholder Dispute", "Corporate", "Negotiated buyout and governance settlement for a closely held technology company.", "corporate"),
    ("$21.7M", "Real Estate Financing", "Finance", "Portfolio refinancing and acquisition facility for a regional owner-operator.", "realestate"),
]

RESULT_ROWS = [
    ("$4.9M", "Employment", "Executive compensation and restrictive-covenant dispute", "Arbitration award", "employment"),
    ("$3.2M", "Tax", "Multi-state audit resolution and penalty abatement", "Administrative resolution", "tax"),
    ("$15.1M", "Corporate", "Sale of a family-owned distribution business", "Closed transaction", "corporate"),
    ("$6.8M", "Real Estate", "Commercial lease and construction claim", "Settlement", "realestate"),
    ("$2.4M", "IP", "Trademark infringement and licensing recovery", "Consent judgment", "intellectualproperty"),
    ("$9.5M", "Banking", "Loan-workout and enforcement settlement", "Negotiated resolution", "banking"),
]

PUBLICATIONS = [
    ("October 2026", "New York choice-of-law clauses after a multi-state merger", "Client Advisory", "ph-file-text"),
    ("August 2026", "Board oversight and privileged investigations: a checklist", "White Paper", "ph-newspaper"),
    ("June 2026", "Commercial leasing in a higher-rate environment", "Firm Commentary", "ph-file-text"),
    ("April 2026", "Federal and New York tax developments for private clients", "Quarterly Review", "ph-newspaper"),
]

PRESS = [
    ("The New York Times", "Quoted on the practical implications of a state-court contract decision.", "Business section"),
    ("Bloomberg Law", "Commentary on middle-market acquisition diligence and disclosure.", "M&A analysis"),
    ("Reuters", "Analysis of a New York regulatory enforcement development.", "Regulatory review"),
]

INDUSTRIES = [
    "Financial Services", "Technology", "Real Estate", "Healthcare", "Manufacturing", "Media & Publishing",
    "Professional Services", "Private Equity", "Family-Owned Business", "Education", "Energy Transition",
    "Hospitality", "Nonprofits", "Life Sciences", "Retail & Consumer", "Infrastructure",
]

TESTIMONIALS = [
    ("They gave us a clear view of the risk before we committed capital. The advice was direct, documented and commercially useful.", "Chief Executive Officer", "Northeast Manufacturing Group", "Corporate transaction"),
    ("The litigation team was prepared for trial from the first week. That preparation changed the negotiation and ultimately the outcome.", "General Counsel", "Private Investment Firm", "Commercial dispute"),
    ("Every deadline in a complicated refinancing was visible to us. No surprises, and no unnecessary drama.", "Chief Financial Officer", "Regional Property Owner", "Real-estate finance"),
]


def attrs(**kwargs: str) -> str:
    return " ".join(value for key, value in kwargs.items() if value)


def page_banner(title, lead, crumbs, es_title, es_lead, title_attr="", lead_attr="", current_attr=""):
    items = []
    for label, url in crumbs:
        if url:
            items.append(f'<li><a href="{url}">{h(label)}</a></li>')
        else:
            items.append(f'<li><span {current_attr}>{h(label)}</span></li>')
    return f'''
<section class="page-banner">
  <div class="container">
    <ol class="breadcrumb">{"".join(items)}</ol>
    <span class="eyebrow">Whitmore &amp; Hale LLP</span>
    <h1 {title_attr} data-es="{h(es_title)}">{h(title)}</h1>
    <p {lead_attr} data-es="{h(es_lead)}">{h(lead)}</p>
  </div>
</section>'''


def section_heading(eyebrow, title, text, centered=False, dark=False, es_title=None, es_text=None):
    classes = "section-heading centered" if centered else "section-heading"
    es_title = es_title or title
    es_text = es_text or text
    return f'''
<div class="{classes}" data-reveal>
  <span class="eyebrow">{h(eyebrow)}</span>
  <h2 data-es="{h(es_title)}">{h(title)}</h2>
  <div class="gold-rule{' centered' if centered else ''}"></div>
  {f'<p data-es="{h(es_text)}">{h(text)}</p>' if text else ''}
</div>'''


def utility_bar():
    return '''
<div class="utility-bar">
  <div class="container">
    <div class="utility-group">
      <a href="tel:+12125550170"><i class="ph ph-phone" aria-hidden="true"></i>+1 (212) 555-0170</a>
      <span class="utility-divider"></span>
      <a class="utility-hide-md" href="contact.html#offices"><i class="ph ph-map-pin" aria-hidden="true"></i>New York | Boston</a>
      <span class="utility-divider"></span>
      <span class="utility-hide-md hide-xs">Attorney Advertising</span>
    </div>
    <div class="utility-group">
      <a href="#" data-bs-toggle="modal" data-bs-target="#portalModal"><i class="ph ph-user" aria-hidden="true"></i><span data-es="Portal del cliente">Client Portal</span></a>
      <span class="utility-divider"></span>
      <div class="language-switch" aria-label="Language selector">
        <i class="ph ph-translate" aria-hidden="true"></i>
        <button type="button" data-lang-select="en" class="active" aria-pressed="true">EN</button>
        <span class="slash">/</span>
        <button type="button" data-lang-select="es" aria-pressed="false">ES</button>
      </div>
    </div>
  </div>
</div>'''


def site_header():
    dropdown = "".join(
        f'<li><a class="dropdown-item" href="{url}">{h(label)}</a></li>'
        for label, url in [
            ("About the Firm", "about.html"),
            ("Pro Bono", "pro-bono.html"),
            ("Careers", "careers.html"),
            ("Testimonials", "testimonials.html"),
            ("FAQ", "faq.html"),
        ]
    )
    return f'''
<header class="site-header" id="top">
  <div class="container header-inner">
    <a class="brand" href="index.html" aria-label="Whitmore & Hale LLP home">
      <img src="assets/brand/logo.svg" alt="Whitmore & Hale LLP">
    </a>
    <nav class="navbar navbar-expand-xl site-navbar" aria-label="Primary navigation">
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#primaryNav" aria-controls="primaryNav" aria-expanded="false" aria-label="Toggle navigation">
        <i class="ph ph-list" aria-hidden="true"></i>
      </button>
      <div class="collapse navbar-collapse site-nav" id="primaryNav">
        <ul class="navbar-nav nav-list">
          <li class="nav-item"><a class="nav-link" href="index.html" data-nav="home"><span data-es="Inicio">Home</span></a></li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="about.html" data-nav="firm" data-bs-toggle="dropdown" aria-expanded="false"><span data-es="La Firma">Firm</span></a>
            <ul class="dropdown-menu">{dropdown}</ul>
          </li>
          <li class="nav-item"><a class="nav-link" href="practice-areas.html" data-nav="practice"><span data-es="Áreas de práctica">Practice Areas</span></a></li>
          <li class="nav-item"><a class="nav-link" href="attorneys.html" data-nav="attorneys"><span data-es="Abogados">Attorneys</span></a></li>
          <li class="nav-item"><a class="nav-link" href="case-results.html" data-nav="results"><span data-es="Resultados">Case Results</span></a></li>
          <li class="nav-item"><a class="nav-link" href="insights.html" data-nav="insights"><span data-es="Perspectivas">Insights</span></a></li>
          <li class="nav-item"><a class="nav-link" href="contact.html" data-nav="contact"><span data-es="Contacto">Contact</span></a></li>
        </ul>
        <a class="btn-wh mobile-cta" href="contact.html#consultation"><span data-es="Solicitar consulta">Request a Consultation</span></a>
      </div>
    </nav>
    <a class="btn-wh header-cta" href="contact.html#consultation"><span data-es="Solicitar consulta">Request a Consultation</span></a>
  </div>
</header>'''


def site_footer():
    practice_links = "".join(
        f'<li><a href="practice-area-detail.html?area={key}">{h(title)}</a></li>'
        for key, title, _, _ in PRACTICES[:6]
    )
    quick_links = [
        ("About the Firm", "about.html"), ("Attorneys", "attorneys.html"), ("Case Results", "case-results.html"),
        ("Insights", "insights.html"), ("Pro Bono", "pro-bono.html"), ("Careers", "careers.html"),
        ("FAQ", "faq.html"), ("Testimonials", "testimonials.html"), ("Contact", "contact.html"),
        ("Privacy", "privacy.html"), ("Terms", "terms.html"),
    ]
    quick_html = "".join(f'<li><a href="{url}">{h(label)}</a></li>' for label, url in quick_links)
    return f'''
<footer class="site-footer">
  <div class="container">
    <div class="row g-4">
      <div class="col-lg-4 col-md-6">
        <img class="footer-logo" src="assets/brand/logo-white.svg" alt="Whitmore & Hale LLP">
        <p class="footer-about">A New York corporate law firm with a Boston office, advising businesses, boards and families since 1998. Measured counsel, senior attention and records built to withstand scrutiny.</p>
        <div class="badge-row">
          <span class="recognition-badge">Super Lawyers</span>
          <span class="recognition-badge">Chambers USA</span>
          <span class="recognition-badge">Best Lawyers</span>
        </div>
        <div class="social-row" aria-label="Social profiles">
          <span class="social-link" aria-hidden="true"><i class="ph ph-linkedin-logo"></i></span>
          <span class="social-link" aria-hidden="true"><i class="ph ph-x-logo"></i></span>
          <span class="social-link" aria-hidden="true"><i class="ph ph-facebook-logo"></i></span>
          <span class="social-link" aria-hidden="true"><i class="ph ph-youtube-logo"></i></span>
        </div>
      </div>
      <div class="col-lg-2 col-md-6 col-6">
        <h3 class="footer-heading">Practice Areas</h3>
        <ul class="footer-links">{practice_links}</ul>
      </div>
      <div class="col-lg-2 col-md-6 col-6">
        <h3 class="footer-heading">Quick Links</h3>
        <ul class="footer-links">{quick_html}</ul>
      </div>
      <div class="col-lg-4 col-md-6">
        <h3 class="footer-heading">Offices &amp; Newsletter</h3>
        <ul class="footer-contact">
          <li><i class="ph ph-map-pin" aria-hidden="true"></i><span>405 Lexington Ave, 26th Fl<br>New York, NY 10174</span></li>
          <li><i class="ph ph-map-pin" aria-hidden="true"></i><span>101 Federal St, 19th Fl<br>Boston, MA 02110</span></li>
          <li><i class="ph ph-phone" aria-hidden="true"></i><a href="tel:+12125550170">+1 (212) 555-0170</a></li>
        </ul>
        <form class="newsletter-form" data-demo-form data-success="Thank you. Newsletter signup is a local preview; connect a mailing-list service before publishing." aria-label="Newsletter signup">
          <label class="visually-hidden" for="footer-newsletter">Email address</label>
          <input id="footer-newsletter" type="email" placeholder="Email address" required>
          <button type="submit" aria-label="Subscribe"><i class="ph ph-arrow-right" aria-hidden="true"></i></button>
          <div class="form-status w-100" data-form-status aria-live="polite"></div>
        </form>
        <p class="form-note">Monthly legal updates. No third-party scripts or trackers.</p>
      </div>
    </div>
    <div class="footer-bottom">
      <div class="row">
        <div class="col-md-7">
          <span>&copy; <span data-current-year>2026</span> Whitmore &amp; Hale LLP. All rights reserved.</span>
          <div class="attorney-advertising">Attorney Advertising. Prior results do not guarantee a similar outcome. NY &amp; MA State Bar admissions. Photography is representative; attorney names and matter descriptions are illustrative for this website concept.</div>
        </div>
        <div class="col-md-5">
          <div class="footer-legal-links">
            <a href="privacy.html">Privacy</a>
            <a href="terms.html">Terms</a>
            <a href="contact.html">Request a Consultation</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</footer>'''


def portal_modal():
    return '''
<div class="modal fade" id="portalModal" tabindex="-1" aria-labelledby="portalModalLabel" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered">
    <div class="modal-content">
      <div class="modal-header">
        <img src="assets/brand/logo-with-bg.png" alt="Whitmore &amp; Hale LLP" style="width: 230px; max-width: 60%;">
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <h2 class="modal-title h3" id="portalModalLabel">Client Portal</h2>
        <p class="text-muted-2">Existing clients receive portal credentials directly from their matter team. This static preview does not transmit credentials.</p>
        <form data-demo-form data-success="This is a design preview only. Please contact your matter team for secure portal credentials." aria-label="Client portal preview">
          <div class="mb-3">
            <label class="form-label" for="portal-email">Email address</label>
            <input class="form-control" id="portal-email" type="email" autocomplete="username" required>
          </div>
          <div class="mb-3">
            <label class="form-label" for="portal-password">Password</label>
            <input class="form-control" id="portal-password" type="password" autocomplete="current-password" required>
          </div>
          <button class="btn-wh-navy w-100" type="submit">Sign In</button>
          <div class="form-status" data-form-status aria-live="polite"></div>
        </form>
      </div>
      <div class="modal-footer">
        <p class="mb-0 small text-muted-2">Need access? Call <a href="tel:+12125550170">+1 (212) 555-0170</a>.</p>
      </div>
    </div>
  </div>
</div>'''


def shell(title, description, body, active="", page="home", extra_head=""):
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{h(title)} | Whitmore &amp; Hale LLP</title>
  <meta name="description" content="{h(description)}">
  <meta name="theme-color" content="#0A2540">
  <link rel="icon" href="assets/brand/favicon.svg" type="image/svg+xml">
  <link rel="icon" type="image/png" sizes="32x32" href="assets/brand/favicon-32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="assets/brand/favicon-16.png">
  <link rel="icon" type="image/png" sizes="48x48" href="assets/brand/favicon-48.png">
  <link rel="icon" type="image/png" sizes="192x192" href="assets/brand/favicon-192.png">
  <link rel="icon" type="image/png" sizes="512x512" href="assets/brand/favicon-512.png">
  <link rel="apple-touch-icon" href="assets/brand/apple-touch-icon.png">
  <link rel="manifest" href="assets/brand/site.webmanifest">
  <link rel="preload" href="assets/vendor/fontsource/playfair-display/files/playfair-display-latin-700-normal.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="assets/vendor/fontsource/source-sans-3/files/source-sans-3-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="assets/vendor/bootstrap/css/bootstrap.min.css">
  <link rel="stylesheet" href="assets/vendor/phosphor/regular/style.css">
  <link rel="stylesheet" href="assets/css/fonts.css">
  <link rel="stylesheet" href="assets/css/styles.css">
  {extra_head}
</head>
<body data-active="{active}" data-page="{page}">
  <a class="skip-link" href="#main">Skip to main content</a>
  {utility_bar()}
  {site_header()}
  <main id="main">
{body}
  </main>
  {site_footer()}
  {portal_modal()}
  <a class="floating-call" href="tel:+12125550170" aria-label="Call Whitmore &amp; Hale LLP now"><i class="ph ph-phone" aria-hidden="true"></i><span>Call Now</span></a>
  <script src="assets/vendor/bootstrap/js/bootstrap.bundle.min.js" defer></script>
  <script src="assets/vendor/gsap/gsap.min.js" defer></script>
  <script src="assets/vendor/gsap/ScrollTrigger.min.js" defer></script>
  <script src="assets/js/main.js" defer></script>
</body>
</html>
'''


def hero_section():
    return '''
<section class="hero" id="hero">
  <div class="container">
    <div class="row">
      <div class="col-lg-7">
        <div class="hero-copy" data-reveal>
          <span class="eyebrow">New York · Boston · Since 1998</span>
          <h1 data-es="Asesoría jurídica en la que puede basar su caso.">Counsel you can build a case on.<span class="accent">Measured. Prepared. Exact.</span></h1>
          <p class="lead-lg" data-es="Asesores de confianza para juntas directivas, empresas y familias en transacciones, disputas y decisiones que importan.">Trusted advisors to boards, businesses and families in transactions, disputes and decisions that carry consequence.</p>
          <div class="hero-actions">
            <a class="btn-wh" href="contact.html#consultation"><span data-es="Solicitar una consulta">Request a Consultation</span><i class="ph ph-arrow-right" aria-hidden="true"></i></a>
            <a class="btn-wh-outline" href="practice-areas.html"><span data-es="Nuestras áreas de práctica">Explore Practice Areas</span></a>
          </div>
          <div class="hero-meta">
            <div><strong>Since 1998</strong><span>Established in New York</span></div>
            <div><strong>40 Attorneys</strong><span>Senior-led teams</span></div>
            <div><strong>NY &amp; MA</strong><span>State Bar admissions</span></div>
          </div>
        </div>
      </div>
      <div class="col-lg-5">
        <div class="hero-photo-wrap" data-reveal>
          <div class="hero-photo"><img src="assets/images/hero-courthouse.jpg" alt="Neoclassical courthouse columns and lamppost in New York" width="500" height="750"></div>
          <div class="hero-photo-caption">A record, a strategy and a clear view of risk.</div>
        </div>
      </div>
    </div>
  </div>
</section>'''


def trust_strip():
    items = [
        ("ph-certificate", "NY & MA Bar", "State admissions"),
        ("ph-shield-check", "AV Preeminent", "Martindale-Hubbell"),
        ("ph-user-focus", "Senior Attention", "Partner-led matters"),
        ("ph-clock", "Since 1998", "28 years of practice"),
    ]
    markup = "".join(
        f'<div class="trust-item"><i class="ph {icon}" aria-hidden="true"></i><div><strong>{h(strong)}</strong><span>{h(small)}</span></div></div>'
        for icon, strong, small in items
    )
    return f'<section class="trust-strip" aria-label="Firm credentials"><div class="container"><div class="trust-grid">{markup}</div></div></section>'


def practice_cards():
    cards = "".join(
        f'''<a class="practice-card" href="practice-area-detail.html?area={key}">
          <i class="ph {icon}" aria-hidden="true"></i>
          <h3>{h(title)}</h3>
          <p>{h(desc)}</p>
          <span class="card-action">View practice <i class="ph ph-arrow-right" aria-hidden="true"></i></span>
        </a>''' for key, title, icon, desc in PRACTICES
    )
    return f'<div class="practice-grid" data-reveal-group>{cards}</div>'


def partner_cards(limit=4):
    cards = "".join(
        f'''<article class="partner-card">
          <a href="attorney-profile.html?attorney={key}" aria-label="View profile for {h(name)}">
            <div class="partner-photo"><img src="assets/images/{photo}" alt="Representative portrait of {h(name)}" loading="lazy"></div>
            <div class="partner-info">
              <h3>{h(name)}</h3>
              <span class="role">{h(role)}</span><br>
              <span class="link-arrow">View profile <i class="ph ph-arrow-right" aria-hidden="true"></i></span>
            </div>
          </a>
          <div class="partner-specialty">{h(specialty)}</div>
        </article>''' for key, name, role, _, photo, specialty in PARTNERS[:limit]
    )
    return f'<div class="partner-grid" data-reveal-group>{cards}</div>'


def attorney_cards():
    cards = "".join(
        f'''<article class="partner-card">
          <a href="attorney-profile.html?attorney={key}" aria-label="View profile for {h(name)}">
            <div class="partner-photo"><img src="assets/images/{photo}" alt="Representative portrait of {h(name)}" loading="lazy"></div>
            <div class="partner-info">
              <h3>{h(name)}</h3>
              <span class="role">{h(role)}</span><br>
              <span class="link-arrow">View profile <i class="ph ph-arrow-right" aria-hidden="true"></i></span>
            </div>
          </a>
          <div class="partner-specialty">{h(practice)}</div>
        </article>''' for key, name, role, practice, photo in ATTORNEYS
    )
    return f'<div class="partner-grid" data-reveal-group>{cards}</div>'


def result_cards():
    cards = "".join(
        f'''<article class="result-card" data-reveal>
          <span class="result-amount">{amount}</span>
          <h3>{h(title)}</h3>
          <p>{h(desc)}</p>
          <div class="result-meta">{h(meta)}</div>
        </article>''' for amount, title, meta, desc, _ in RESULTS
    )
    return f'<div class="result-grid">{cards}</div>'


def blog_cards(posts):
    cards = "".join(
        f'''<article class="blog-card">
          <a href="blog-single.html" aria-label="Read {h(title)}">
            <div class="blog-image"><img src="{image}" alt="" loading="lazy"></div>
            <div class="blog-body">
              <span class="blog-meta">{h(date)} · {h(category)}</span>
              <h3>{h(title)}</h3>
              <p>{h(excerpt)}</p>
              <span class="link-arrow">Read article <i class="ph ph-arrow-right" aria-hidden="true"></i></span>
            </div>
          </a>
        </article>''' for title, date, category, image, excerpt in posts
    )
    return f'<div class="blog-grid" data-reveal-group>{cards}</div>'


def faq_accordion(items, prefix):
    markup = []
    for i, (question, answer) in enumerate(items, 1):
        expanded = i == 1
        markup.append(f'''
<div class="faq-item" data-faq-item>
  <button class="faq-button" type="button" data-bs-toggle="collapse" data-bs-target="#{prefix}-{i}" aria-expanded="{str(expanded).lower()}" aria-controls="{prefix}-{i}">
    <span>{h(question)}</span>
    <i class="ph ph-plus" aria-hidden="true"></i><i class="ph ph-minus" aria-hidden="true"></i>
  </button>
  <div class="collapse{' show' if expanded else ''}" id="{prefix}-{i}">
    <div class="faq-answer">{h(answer)}</div>
  </div>
</div>''')
    return f'<div class="faq-list" data-reveal>{"".join(markup)}</div>'


def contact_form(prefix, full=True):
    phone_company = '''
      <div class="form-field">
        <label class="form-label" for="%s-phone">Phone</label>
        <input class="form-control" id="%s-phone" name="phone" type="tel" autocomplete="tel">
      </div>
      <div class="form-field">
        <label class="form-label" for="%s-company">Company / Organization</label>
        <input class="form-control" id="%s-company" name="company" type="text" autocomplete="organization">
      </div>''' % (prefix, prefix, prefix, prefix) if full else ""
    return f'''
<form class="form-shell" data-demo-form data-success="Thank you. Your request has been validated locally. Please call +1 (212) 555-0170 or connect a secure intake service before publishing." aria-label="Consultation request">
  <span class="eyebrow">Confidential Inquiry</span>
  <h3>Tell us what needs attention.</h3>
  <p class="text-muted-2">A member of the intake team responds within one business day. Rates are on request.</p>
  <div class="form-grid">
    <div class="form-field">
      <label class="form-label" for="{prefix}-name">Full name <span class="required-marker">*</span></label>
      <input class="form-control" id="{prefix}-name" name="name" type="text" autocomplete="name" required>
    </div>
    <div class="form-field">
      <label class="form-label" for="{prefix}-email">Email <span class="required-marker">*</span></label>
      <input class="form-control" id="{prefix}-email" name="email" type="email" autocomplete="email" required>
    </div>
    {phone_company}
    <div class="form-field{' full' if phone_company else ''}">
      <label class="form-label" for="{prefix}-area">Practice area <span class="required-marker">*</span></label>
      <select class="form-select" id="{prefix}-area" name="practice_area" data-practice-select required>
        <option value="" selected disabled>Select an area</option>
        {"".join(f'<option>{h(title)}</option>' for _, title, _, _ in PRACTICES)}
        <option>General inquiry</option>
      </select>
    </div>
    <div class="form-field full">
      <label class="form-label" for="{prefix}-message">Brief description <span class="required-marker">*</span></label>
      <textarea class="form-control" id="{prefix}-message" name="message" rows="4" required></textarea>
    </div>
  </div>
  <div class="form-check mt-3">
    <input class="form-check-input" id="{prefix}-consent" type="checkbox" required>
    <label class="form-label d-inline" for="{prefix}-consent">I understand that submitting this form does not create an attorney-client relationship.</label>
  </div>
  <button class="btn-wh mt-4" type="submit">Submit Request <i class="ph ph-arrow-right" aria-hidden="true"></i></button>
  <p class="form-note">Do not include confidential or time-sensitive information. This static preview does not transmit form data.</p>
  <div class="form-status" data-form-status aria-live="polite"></div>
</form>'''


def cta_band():
    return '''
<section class="cta-band">
  <div class="container">
    <div class="row">
      <div class="col-lg-8">
        <span class="eyebrow">A measured first step</span>
        <h2 data-es="Hable con un abogado senior antes de tomar su próxima decisión.">Speak with senior counsel before the next decision.</h2>
        <p data-es="Una conversación preliminar para entender el asunto, los conflictos y si la firma es la opción adecuada.">A preliminary discussion to understand the matter, identify conflicts and determine whether the firm is the right fit.</p>
      </div>
      <div class="col-lg-4 text-lg-end">
        <a class="btn-wh" href="contact.html#consultation"><span data-es="Solicitar consulta gratuita">Request a Consultation</span><i class="ph ph-arrow-right" aria-hidden="true"></i></a>
      </div>
    </div>
  </div>
</section>'''


def office_cards():
    return '''
<div class="office-grid">
  <article class="office-card">
    <span class="eyebrow">Headquarters</span>
    <h3>New York</h3>
    <address>405 Lexington Ave, 26th Fl<br>New York, NY 10174<br>United States</address>
    <div class="office-contact">
      <a href="tel:+12125550170"><i class="ph ph-phone" aria-hidden="true"></i>+1 (212) 555-0170</a>
      <a href="mailto:intake@whitmore-hale.com"><i class="ph ph-envelope" aria-hidden="true"></i>Email</a>
    </div>
  </article>
  <article class="office-card">
    <span class="eyebrow">Regional office</span>
    <h3>Boston</h3>
    <address>101 Federal St, 19th Fl<br>Boston, MA 02110<br>United States</address>
    <div class="office-contact">
      <a href="tel:+16175550184"><i class="ph ph-phone" aria-hidden="true"></i>+1 (617) 555-0184</a>
      <a href="mailto:boston@whitmore-hale.com"><i class="ph ph-envelope" aria-hidden="true"></i>Email</a>
    </div>
  </article>
</div>'''


def offices_section():
    return f'''
<section class="section offices-section" id="offices">
  <div class="container">
    {section_heading("Offices", "Two desks. One standard.", "Midtown Manhattan and Boston's Financial District, with coordinated teams across corporate, litigation and regulatory matters.", centered=True, dark=True, es_title="Dos oficinas. Un mismo estándar.")}
    <div class="map-panel" data-reveal>
      <img src="assets/images/map-midtown.png" alt="Local street map of Midtown Manhattan near Lexington Avenue and East 42nd Street" loading="lazy">
      <span class="map-label">Midtown Manhattan · Lexington Ave &amp; E 42nd St</span>
      <span class="map-pin ny"><i class="ph ph-map-pin" aria-hidden="true"></i>405 Lexington Ave</span>
    </div>
    {office_cards()}
  </div>
</section>'''


def stats_section():
    return '''
<section class="stats-section" aria-label="Firm statistics">
  <div class="container">
    <div class="stat-grid">
      <div class="stat"><span class="stat-number" data-count="1200" data-suffix="+">1,200+</span><span class="stat-label">Matters handled</span></div>
      <div class="stat"><span class="stat-number" data-count="94" data-suffix="%">94%</span><span class="stat-label">Favorable resolution rate</span></div>
      <div class="stat"><span class="stat-number" data-count="28">28</span><span class="stat-label">Years serving clients</span></div>
      <div class="stat"><span class="stat-number" data-count="40">40</span><span class="stat-label">Attorneys</span></div>
    </div>
    <p class="disclaimer-note text-center mb-0 mt-4">Statistics are illustrative website copy. Past results do not guarantee a similar outcome.</p>
  </div>
</section>'''


def process_section():
    steps = [
        ("ph-handshake", "Consultation", "We define the question, identify conflicts and agree whether an engagement makes sense."),
        ("ph-folder-open", "Case review", "The team builds a chronology, collects the operative documents and isolates the decisions that matter."),
        ("ph-scales", "Strategy", "You receive a written plan with options, risks, budget phases and a named partner responsible for the file."),
        ("ph-trophy", "Resolution", "We negotiate, litigate or close with the record prepared for the next stage, including appeal or integration."),
    ]
    markup = "".join(
        f'''<article class="timeline-step" data-reveal>
          <span class="timeline-icon"><i class="ph {icon}" aria-hidden="true"></i></span>
          <span class="step-number">Step {i:02d}</span>
          <h3>{h(title)}</h3>
          <p>{h(text)}</p>
        </article>''' for i, (icon, title, text) in enumerate(steps, 1)
    )
    return f'''
<section class="section process-section" id="process">
  <div class="container">
    {section_heading("How we work", "A disciplined process, visible at every stage.", "No black box. Each phase has an owner, a deliverable and a decision point.", centered=True, es_title="Un proceso disciplinado, visible en cada etapa.")}
    <div class="process-timeline">
      <svg class="timeline-svg" viewBox="0 0 40 800" preserveAspectRatio="none" aria-hidden="true"><path d="M20 0 V800"></path></svg>
      {markup}
    </div>
  </div>
</section>'''


def testimonial_slider():
    slides = "".join(
        f'''<div class="testimonial-slide" data-slide aria-hidden="{str(i != 0).lower()}">
          <i class="ph ph-quotes" aria-hidden="true"></i>
          <div class="stars" aria-label="Five stars"><i class="ph ph-star"></i><i class="ph ph-star"></i><i class="ph ph-star"></i><i class="ph ph-star"></i><i class="ph ph-star"></i></div>
          <blockquote>“{h(quote)}”</blockquote>
          <div class="testimonial-client">{h(role)}<span>{h(company)} · {h(context)}</span></div>
        </div>''' for i, (quote, role, company, context) in enumerate(TESTIMONIALS)
    )
    dots = "".join(
        f'<button class="slider-dot{" is-active" if i == 0 else ""}" type="button" data-slide-dot aria-label="Show testimonial {i+1}" aria-current="{str(i == 0).lower()}"></button>'
        for i in range(len(TESTIMONIALS))
    )
    return f'''
<div class="testimonial-slider" data-slider tabindex="0" aria-roledescription="carousel" aria-label="Client testimonials" aria-live="polite">
  {slides}
  <div class="slider-controls">
    <button class="slider-btn" type="button" data-slide-prev aria-label="Previous testimonial"><i class="ph ph-caret-left" aria-hidden="true"></i></button>
    <div class="slider-dots">{dots}</div>
    <button class="slider-btn" type="button" data-slide-next aria-label="Next testimonial"><i class="ph ph-caret-right" aria-hidden="true"></i></button>
  </div>
</div>'''


def home_page():
    practice_heading = section_heading("Expertise", "Eight practices, one standard of work.", "Focused teams that coordinate across transactions, disputes and regulation — without handing your matter between unfamiliar desks.", es_title="Ocho prácticas, un solo estándar de trabajo.")
    about_points = [
        ("ph-user-focus", "Partner-led files", "The lawyer who scopes the work remains accountable for the result."),
        ("ph-shield-check", "Institutional judgment", "Clear conflict procedures, careful records and candid risk assessment."),
        ("ph-globe-hemisphere-west", "Cross-border coordination", "New York and Massachusetts teams supported by a vetted local-counsel network."),
    ]
    about_points_html = "".join(
        f'<li><i class="ph {icon}" aria-hidden="true"></i><div><strong>{h(title)}</strong><span>{h(text)}</span></div></li>'
        for icon, title, text in about_points
    )
    reasons = [
        ("Senior attention", "A partner is responsible for scope, staffing and the advice that leaves the firm."),
        ("Written economics", "Phased budgets and rates on request, documented before substantive work begins."),
        ("Evidence first", "We organize the record early, whether the destination is a closing, motion or board decision."),
        ("Measured communication", "Concise updates tied to decisions, not activity for its own sake."),
        ("Institutional continuity", "Since 1998, clients have worked with teams built for long relationships, not one-off matters."),
    ]
    reasons_html = "".join(
        f'''<article class="reason-row" data-reveal>
          <span class="reason-number">{i:02d}</span>
          <div><h3>{h(title)}</h3><p>{h(text)}</p></div>
        </article>''' for i, (title, text) in enumerate(reasons, 1)
    )
    industry_tags = "".join(f'<span class="industry-tag">{h(tag)}</span>' for tag in INDUSTRIES)
    publication_rows_left = "".join(
        f'''<article class="publication-row">
          <span class="pub-date">{h(date)}</span>
          <div><h3 class="pub-title">{h(title)}</h3><span class="pub-type">{h(kind)}</span></div>
          <a class="link-arrow" href="insights.html">Read <i class="ph ph-arrow-right" aria-hidden="true"></i></a>
        </article>''' for date, title, kind, _ in PUBLICATIONS[:2]
    )
    publication_rows_right = "".join(
        f'''<article class="publication-row">
          <span class="pub-date">{h(date)}</span>
          <div><h3 class="pub-title">{h(title)}</h3><span class="pub-type">{h(kind)}</span></div>
          <a class="link-arrow" href="insights.html">Read <i class="ph ph-arrow-right" aria-hidden="true"></i></a>
        </article>''' for date, title, kind, _ in PUBLICATIONS[2:]
    )
    press_html = "".join(
        f'<article class="press-item" data-reveal><span class="press-name">{h(name)}</span><p>{h(text)}</p><span>{h(kind)}</span></article>'
        for name, text, kind in PRESS
    )
    return f'''
{hero_section()}
{trust_strip()}
<section class="section" id="practice-areas">
  <div class="container">{practice_heading}{practice_cards()}</div>
</section>
<section class="section bg-paper" id="about">
  <div class="container">
    <div class="about-split">
      <div class="about-portrait">
        <div class="gold-frame mask-reveal">
          <img src="assets/images/partner-eleanor.jpg" alt="Representative portrait of the managing partner" loading="lazy">
          <div class="frame-caption">Eleanor Whitmore · Managing Partner</div>
        </div>
      </div>
      <div>
        <div data-reveal>
          <span class="eyebrow">About the firm</span>
          <h2>A traditional standard, practiced with modern discipline.</h2>
          <div class="gold-rule"></div>
          <p class="lead-lg">Founded in New York in 1998, Whitmore &amp; Hale LLP advises companies, boards, investors and families where the legal record must be as strong as the commercial judgment behind it.</p>
          <p>Our teams are deliberately small and senior-led. We do not measure service by volume of activity. We measure it by whether the client understands the decision in front of them, the evidence supporting it, and the cost of getting it wrong.</p>
          <a class="link-arrow" href="about.html">Read our history <i class="ph ph-arrow-right" aria-hidden="true"></i></a>
        </div>
        <ul class="about-points" data-reveal>{about_points_html}</ul>
      </div>
    </div>
  </div>
</section>
{stats_section()}
<section class="section" id="case-results">
  <div class="container">
    {section_heading("Case results", "Outcomes with the record behind them.", "Selected public and illustrative matters. Amounts reflect judgments, settlements or transaction value.", es_title="Resultados respaldados por el expediente.")}
    {result_cards()}
    <p class="disclaimer-note">Past results do not guarantee a similar outcome. Client names are withheld unless consent is given.</p>
  </div>
</section>
<section class="section bg-white" id="partners">
  <div class="container">
    {section_heading("Meet the partners", "The people accountable for your matter.", "Hover over a portrait to see the partner's principal specialisation.", es_title="Las personas responsables de su asunto.")}
    {partner_cards()}
    <div class="text-center mt-4"><a class="link-arrow" href="attorneys.html">View all attorneys <i class="ph ph-arrow-right" aria-hidden="true"></i></a></div>
  </div>
</section>
<section class="section" id="why-us">
  <div class="container">
    <div class="why-grid">
      <div class="why-sticky" data-reveal>
        <span class="eyebrow">Why Whitmore &amp; Hale</span>
        <h2>Five reasons clients stay.</h2>
        <div class="gold-rule"></div>
        <p class="lead-lg">The work is serious, the advice is candid, and the team remains recognizable from the first call to the last document.</p>
      </div>
      <div>{reasons_html}</div>
    </div>
  </div>
</section>
{process_section()}
<section class="section section-sm" id="industries">
  <div class="container">
    {section_heading("Industries served", "Sector fluency without a sector script.", "Legal judgment grounded in how our clients actually operate.", centered=True, es_title="Conocimiento del sector sin guiones prefabricados.")}
    <div class="tag-cloud" data-reveal>{industry_tags}</div>
  </div>
</section>
<section class="section bg-white" id="publications">
  <div class="container">
    {section_heading("Recent opinions & publications", "Written for decision-makers.", "Short analyses from the lawyers handling the matters behind the headlines.", es_title="Escrito para quienes toman decisiones.")}
    <div class="row g-5" data-reveal>
      <div class="col-md-6"><div class="publication-list">{publication_rows_left}</div></div>
      <div class="col-md-6"><div class="publication-list">{publication_rows_right}</div></div>
    </div>
  </div>
</section>
<section class="section section-sm bg-paper" id="press">
  <div class="container">
    {section_heading("Media & press", "Counsel in the public record.", "Selected quotations and commentary in national and legal-business press.", centered=True, es_title="Asesoría en el registro público.")}
    <div class="press-grid">{press_html}</div>
  </div>
</section>
<section class="section testimonial-section" id="testimonials">
  <div class="container">
    {section_heading("Client testimonials", "In their words.", "Representative comments about responsiveness, judgment and preparation.", centered=True, es_title="En palabras de nuestros clientes.")}
    {testimonial_slider()}
  </div>
</section>
<section class="section" id="insights">
  <div class="container">
    {section_heading("Insights", "The latest from our desks.", "Practical notes on transactions, disputes and regulation.", es_title="Lo más reciente de nuestros equipos.")}
    {blog_cards(POSTS[:3])}
    <div class="text-center mt-4"><a class="link-arrow" href="insights.html">Read all insights <i class="ph ph-arrow-right" aria-hidden="true"></i></a></div>
  </div>
</section>
{offices_section()}
{cta_band()}
<section class="section" id="faq">
  <div class="container">
    <div class="row">
      <div class="col-lg-4">{section_heading("FAQ", "Common questions, plain answers.", "A few things clients ask before an engagement begins.")}</div>
      <div class="col-lg-8">{faq_accordion(FAQS, "faq-home")}</div>
    </div>
  </div>
</section>
<section class="section bg-white" id="consultation">
  <div class="container">
    <div class="row align-items-center g-5">
      <div class="col-lg-5" data-reveal>
        <span class="eyebrow">Start a conversation</span>
        <h2>Tell us what is at stake.</h2>
        <div class="gold-rule"></div>
        <p class="lead-lg">A short, confidential inquiry is enough to begin. We will identify conflicts and tell you plainly whether the firm can help.</p>
        <ul class="check-list mt-4">
          <li>Response within one business day</li>
          <li>No attorney-client relationship formed online</li>
          <li>Rates on request</li>
        </ul>
      </div>
      <div class="col-lg-7" data-reveal>{contact_form("home", full=False)}</div>
    </div>
  </div>
</section>'''


def about_page():
    timeline = [
        ("1998", "Founded in New York", "Arthur Hale and Eleanor Whitmore open the firm with four lawyers and a corporate-litigation practice."),
        ("2004", "Boston office", "A Massachusetts desk is established to serve New England financial and family-owned businesses."),
        ("2011", "Regulatory group", "The firm adds banking and investigations capability as clients' supervisory demands increase."),
        ("2017", "Cross-border desk", "A vetted international counsel network is formalized for inbound and outbound transactions."),
        ("2022", "Pro bono clinic", "A monthly New York community clinic becomes a firm-wide program."),
        ("2026", "Twenty-eight years", "Forty attorneys across two offices, still organized around partner accountability."),
    ]
    timeline_html = "".join(
        f'''<article class="history-item" data-reveal><span class="history-year">{year}</span><h3>{h(title)}</h3><p>{h(text)}</p></article>'''
        for year, title, text in timeline
    )
    values = [
        ("ph-shield-check", "Integrity", "We say no to a position the record cannot support. Conflicts are resolved before advice is given."),
        ("ph-user-focus", "Senior attention", "Partners stay close to the evidence, the drafting and the client conversation."),
        ("ph-scales", "Proportion", "The legal response is sized to the actual risk, not to the volume of work that could be billed."),
    ]
    values_html = "".join(
        f'''<article class="info-card" data-reveal><i class="ph {icon}" aria-hidden="true"></i><h3>{h(title)}</h3><p>{h(text)}</p></article>'''
        for icon, title, text in values
    )
    certifications = ["NY State Bar", "Massachusetts Bar", "Chambers USA", "Best Lawyers", "Super Lawyers", "Martindale-Hubbell"]
    cert_html = "".join(f'<div class="certification-badge">{h(name)}</div>' for name in certifications)
    return f'''
{page_banner("About the Firm", "A New York firm built around partner accountability, careful records and long client relationships since 1998.", [("Home", "index.html"), ("About the Firm", "")], "Sobre la Firma", "Una firma neoyorquina basada en la responsabilidad del socio, expedientes cuidadosos y relaciones duraderas desde 1998.")}
<section class="section">
  <div class="container">
    <div class="about-split">
      <div data-reveal>
        <span class="eyebrow">Our history</span>
        <h2>Founded on a simple professional premise.</h2>
        <div class="gold-rule"></div>
        <p class="lead-lg">The client should know who is responsible for the advice, what the work will cost and which facts matter most.</p>
        <p>Whitmore &amp; Hale began in 1998 with four lawyers and two practice groups. Growth has been deliberate: each new capability answers a recurring client need rather than a market trend. The Boston office, regulatory group and pro bono clinic all followed that pattern.</p>
        <p>Today, forty attorneys work from Midtown Manhattan and Boston's Financial District. Matter teams remain intentionally compact, with a named partner accountable from engagement through resolution.</p>
      </div>
      <div class="gold-frame mask-reveal">
        <img src="assets/images/reading-room.jpg" alt="Historic New York reading room with long tables and chandeliers" loading="lazy">
        <div class="frame-caption">New York · A standard of careful work</div>
      </div>
    </div>
  </div>
</section>
<section class="section bg-paper">
  <div class="container">
    {section_heading("Values", "Three principles that govern the work.", "They shape staffing, budgets, writing and the advice we are willing to give.", centered=True, es_title="Tres principios que rigen nuestro trabajo.")}
    <div class="value-grid" data-reveal-group>{values_html}</div>
  </div>
</section>
<section class="section">
  <div class="container">
    {section_heading("Firm timeline", "Steady growth, no reinventions.", "A chronological view of the decisions that shaped the firm.", centered=True, es_title="Crecimiento constante, sin reinvenciones.")}
    <div class="history-timeline">{timeline_html}</div>
  </div>
</section>
<section class="section bg-white">
  <div class="container">
    {section_heading("Our team", "Partners and counsel.", "Representative profiles for this website concept; photography is illustrative.", centered=True, es_title="Socios y asesores.")}
    {attorney_cards()}
  </div>
</section>
<section class="section section-sm bg-paper">
  <div class="container">
    {section_heading("Certifications & recognition", "Professional standing.", "Memberships and recognition references included as brand markers in this concept.", centered=True, es_title="Colegiación y reconocimientos.")}
    <div class="certification-row" data-reveal>{cert_html}</div>
  </div>
</section>
{cta_band()}'''


def practice_areas_page():
    rows = "".join(
        f'''<article class="practice-list-row" data-reveal>
          <div class="practice-list-title"><i class="ph {icon}" aria-hidden="true"></i><h3>{h(title)}</h3></div>
          <div><p>{h(desc)}</p><a class="link-arrow" href="practice-area-detail.html?area={key}">View practice <i class="ph ph-arrow-right" aria-hidden="true"></i></a></div>
        </article>''' for key, title, icon, desc in PRACTICES
    )
    return f'''
{page_banner("Practice Areas", "Eight focused practices, coordinated by partners who remain accountable for the whole matter.", [("Home", "index.html"), ("Practice Areas", "")], "Áreas de práctica", "Ocho prácticas especializadas, coordinadas por socios responsables de todo el asunto.")}
<section class="section">
  <div class="container">
    <div class="row g-5 align-items-start">
      <div class="col-lg-4" data-reveal>
        <span class="eyebrow">Capabilities</span>
        <h2>Counsel organized around decisions.</h2>
        <div class="gold-rule"></div>
        <p class="lead-lg">Our practice descriptions are deliberately short. The useful answer begins with the specific facts, documents and commercial objective.</p>
        <a class="link-arrow" href="contact.html#consultation">Discuss a matter <i class="ph ph-arrow-right" aria-hidden="true"></i></a>
      </div>
      <div class="col-lg-8"><div class="practice-list">{rows}</div></div>
    </div>
  </div>
</section>
{cta_band()}'''


def practice_detail_page():
    related = "".join(
        f'''<a class="info-card d-block" href="practice-area-detail.html?area={key}">
          <i class="ph {icon}" aria-hidden="true"></i><h3>{h(title)}</h3><p>{h(desc)}</p><span class="link-arrow">View <i class="ph ph-arrow-right" aria-hidden="true"></i></span>
        </a>''' for key, title, icon, desc in PRACTICES[1:4]
    )
    return f'''
<div data-practice-detail>
{page_banner("Corporate & Transactions", "Practical counsel for formations, governance, financings, acquisitions and the decisions that change a company's trajectory.", [("Home", "index.html"), ("Practice Areas", "practice-areas.html"), ("Corporate & Transactions", "")], "Derecho corporativo y transacciones", "Asesoría práctica para constituciones, gobierno corporativo, financiaciones y adquisiciones.", title_attr="data-detail-title", lead_attr="data-detail-intro", current_attr="data-detail-crumb")}
<section class="section">
  <div class="container">
    <div class="detail-layout">
      <aside class="sticky-sidebar" aria-label="Practice detail sidebar">
        <div class="sidebar-card">
          <i class="ph ph-buildings" data-detail-icon aria-hidden="true" style="font-size:2rem;color:var(--clr-secondary)"></i>
          <h3 class="mt-3">On this page</h3>
          <ul class="sidebar-nav">
            <li><a href="#overview" class="active">Overview</a></li>
            <li><a href="#services">How we help</a></li>
            <li><a href="#approach">Our approach</a></li>
            <li><a href="#experience">Experience</a></li>
          </ul>
          <div class="sidebar-cta">
            <p class="small text-muted-2">Speak with the practice lead about a specific matter.</p>
            <a class="btn-wh" data-detail-contact href="contact.html">Request Consultation</a>
          </div>
        </div>
      </aside>
      <article class="detail-content prose" data-detail-content data-reveal>
        <h2 id="overview">Overview</h2><p>Loading practice detail…</p>
        <h2 id="services">How we help</h2><p>Practice capabilities are loaded from the local site script.</p>
        <h2 id="approach">Our approach</h2><p>Select a practice area to view its approach.</p>
        <h2 id="experience">Representative experience</h2><p>Matter descriptions are illustrative.</p>
      </article>
    </div>
  </div>
</section>
<section class="section bg-paper">
  <div class="container">
    {section_heading("Related practices", "Often coordinated with this team.", "Clients frequently need more than one desk; we staff accordingly.", es_title="Prácticas relacionadas.")}
    <div class="related-grid" data-reveal-group>{related}</div>
  </div>
</section>
{cta_band()}
</div>'''


def attorneys_page():
    return f'''
{page_banner("Attorneys", "Forty attorneys across New York and Boston, organized in compact, senior-led matter teams.", [("Home", "index.html"), ("Attorneys", "")], "Abogados", "Cuarenta abogados en Nueva York y Boston, organizados en equipos reducidos dirigidos por socios.")}
<section class="section">
  <div class="container">
    {section_heading("Our people", "Profiles and principal specialisations.", "Portraits and biographies are representative for this website concept.", centered=True, es_title="Perfiles y especialidades principales.")}
    {attorney_cards()}
  </div>
</section>
{cta_band()}'''


def attorney_profile_page():
    related = "".join(
        f'''<a class="info-card d-block" href="attorney-profile.html?attorney={key}">
          <h3>{h(name)}</h3><p>{h(role)} · {h(practice)}</p><span class="link-arrow">View profile <i class="ph ph-arrow-right" aria-hidden="true"></i></span>
        </a>''' for key, name, role, practice, _ in ATTORNEYS[1:4]
    )
    return f'''
<div data-attorney-profile>
{page_banner("Eleanor Whitmore", "Managing Partner · Corporate & Transactions", [("Home", "index.html"), ("Attorneys", "attorneys.html"), ("Eleanor Whitmore", "")], "Perfil del abogado", "Socia directora · Derecho corporativo y transacciones", title_attr="data-profile-name", lead_attr="data-profile-role", current_attr="data-profile-crumb")}
<section class="section">
  <div class="container">
    <div class="profile-layout">
      <div class="profile-photo">
        <div class="gold-frame mask-reveal">
          <img data-profile-photo src="assets/images/partner-eleanor.jpg" alt="Representative attorney portrait">
          <div class="frame-caption">Whitmore &amp; Hale LLP · New York</div>
        </div>
      </div>
      <article data-reveal>
        <span class="eyebrow">Attorney profile</span>
        <h2 data-es="Biografía">Biography</h2>
        <div class="gold-rule"></div>
        <div class="prose" data-profile-bio><p>Loading profile…</p></div>
        <div class="profile-meta-grid">
          <div><span>Primary practice</span><strong data-profile-practice>Corporate &amp; Transactions</strong></div>
          <div><span>Bar admissions</span><strong data-profile-admissions>New York · Massachusetts</strong></div>
          <div><span>Education</span><strong data-profile-education>J.D., Columbia Law School</strong></div>
          <div><span>Email</span><strong><a data-profile-email href="mailto:ewhitmore@whitmore-hale.com">ewhitmore@whitmore-hale.com</a></strong></div>
        </div>
        <p class="small-caps">Representative recognition</p>
        <p data-profile-note>Selected by Best Lawyers for corporate law.</p>
        <a class="btn-wh" href="contact.html#consultation">Request a Consultation <i class="ph ph-arrow-right" aria-hidden="true"></i></a>
      </article>
    </div>
  </div>
</section>
<section class="section bg-paper">
  <div class="container">
    <div class="row g-5">
      <div class="col-lg-5">{section_heading("Focus", "Principal areas of focus.", "A short list is more useful than an exhaustive one.")}</div>
      <div class="col-lg-7"><ul class="check-list" data-profile-focus><li>Corporate transactions</li></ul></div>
    </div>
  </div>
</section>
<section class="section">
  <div class="container">
    {section_heading("Other attorneys", "Work with the wider team.", "Matter teams are assembled around the issue, not the org chart.", centered=True, es_title="Conozca al equipo.")}
    <div class="related-grid" data-reveal-group>{related}</div>
  </div>
</section>
{cta_band()}
</div>'''


def case_results_page():
    rows = "".join(
        f'''<tr data-category="{category}">
          <td class="amount">{amount}</td><td>{h(area)}</td><td>{h(matter)}</td><td>{h(outcome)}</td>
          <td><a class="link-arrow" href="contact.html">Discuss <i class="ph ph-arrow-right" aria-hidden="true"></i></a></td>
        </tr>''' for amount, area, matter, outcome, category in RESULT_ROWS
    )
    return f'''
{page_banner("Case Results", "Selected judgments, settlements and transactions, presented with the context needed to read them responsibly.", [("Home", "index.html"), ("Case Results", "")], "Resultados", "Sentencias, acuerdos y transacciones seleccionados, presentados con el contexto necesario.")}
<section class="section">
  <div class="container">
    {section_heading("Featured outcomes", "Three matters, three different definitions of success.", "A trial judgment, a negotiated governance solution and a financing that closed on its original timetable.", es_title="Tres asuntos, tres definiciones distintas de éxito.")}
    {result_cards()}
    <p class="disclaimer-note">Past results do not guarantee a similar outcome. Figures and descriptions are illustrative for this website concept.</p>
  </div>
</section>
<section class="section bg-paper">
  <div class="container">
    {section_heading("Selected matters", "A wider view of our work.", "Use the filters to view a category; the table remains fully local and requires no database.")}
    <div class="filter-tabs" aria-label="Filter case results">
      <button class="filter-tab is-active" type="button" data-filter="all">All</button>
      <button class="filter-tab" type="button" data-filter="litigation">Litigation</button>
      <button class="filter-tab" type="button" data-filter="corporate">Corporate</button>
      <button class="filter-tab" type="button" data-filter="realestate">Real Estate</button>
      <button class="filter-tab" type="button" data-filter="employment">Employment</button>
      <button class="filter-tab" type="button" data-filter="tax">Tax</button>
    </div>
    <div class="results-table-wrap" data-reveal>
      <table class="results-table">
        <thead><tr><th>Amount / Value</th><th>Practice</th><th>Matter</th><th>Resolution</th><th></th></tr></thead>
        <tbody>{rows}</tbody>
      </table>
    </div>
  </div>
</section>
{cta_band()}'''


def sidebar_widgets():
    categories = "".join(
        f'<li><a href="insights.html">{h(category)}</a></li>' for category in sorted({post[2] for post in POSTS})
    )
    recent = "".join(
        f'<li><a href="blog-single.html">{h(post[0])}</a></li>' for post in POSTS[:4]
    )
    return f'''
<aside class="sidebar" aria-label="Insights sidebar">
  <div class="sidebar-widget"><h3>Categories</h3><ul>{categories}</ul></div>
  <div class="sidebar-widget"><h3>Recent posts</h3><ul>{recent}</ul></div>
  <div class="sidebar-widget">
    <h3>Firm newsletter</h3>
    <p class="small text-muted-2">A monthly note on legal developments that affect transactions and disputes.</p>
    <form data-demo-form data-success="Thank you. This newsletter form is a local preview." aria-label="Newsletter signup">
      <label class="form-label" for="sidebar-newsletter">Email</label>
      <input class="form-control mb-3" id="sidebar-newsletter" type="email" required>
      <button class="btn-wh-navy w-100" type="submit">Subscribe</button>
      <div class="form-status" data-form-status aria-live="polite"></div>
    </form>
  </div>
</aside>'''


def insights_page():
    posts_html = "".join(
        f'''<article class="post-row" data-reveal>
          <img src="{image}" alt="" loading="lazy">
          <div>
            <span class="blog-meta">{h(date)} · {h(category)}</span>
            <h2><a href="blog-single.html">{h(title)}</a></h2>
            <p>{h(excerpt)}</p>
            <a class="link-arrow" href="blog-single.html">Read article <i class="ph ph-arrow-right" aria-hidden="true"></i></a>
          </div>
        </article>''' for title, date, category, image, excerpt in POSTS
    )
    return f'''
{page_banner("Insights", "Practical notes on corporate transactions, disputes, regulation and the decisions that follow.", [("Home", "index.html"), ("Insights", "")], "Perspectivas", "Notas prácticas sobre transacciones, disputas, regulación y las decisiones posteriores.")}
<section class="section">
  <div class="container">
    <div class="blog-layout">
      <div>{posts_html}</div>
      {sidebar_widgets()}
    </div>
  </div>
</section>
{cta_band()}'''


def blog_single_page():
    return f'''
{page_banner("Insights", "A single-article reading view with a focused 720px measure and no external trackers.", [("Home", "index.html"), ("Insights", "insights.html"), ("Article", "")], "Perspectivas", "Vista de lectura con una columna de 720 píxeles y sin rastreadores externos.")}
<section class="section">
  <div class="container">
    <article class="article-column">
      <span class="small-caps">Corporate · October 14, 2026</span>
      <h1>Fiduciary duties when a growth company misses its plan</h1>
      <p class="article-lede">Boards rarely face a fiduciary question when the plan is working. The record matters when forecasts turn, liquidity tightens and directors must choose between competing stakeholders.</p>
      <img class="article-hero" src="assets/images/meeting-room.jpg" alt="Professionals in a conference room reviewing documents" loading="lazy">
      <div class="article-body prose">
        <p>A board is not required to be prescient. It is required to be informed, disinterested and deliberate. Those qualities are demonstrated less by the final decision than by the process that produced it: the information requested, the alternatives considered, the advice received and the minutes that record the discussion.</p>
        <h2>Start with the record, not the slogan</h2>
        <p>When a company misses a forecast, the first task is factual. Which assumptions failed, when did management know, what obligations mature next, and which constituencies have enforceable rights? A concise chronology and a matrix of contractual constraints will often narrow the board's real options faster than a general discussion of duties.</p>
        <blockquote>Good minutes do not merely state that directors discussed a matter. They show what was before the board, who advised it and which alternatives were rejected.</blockquote>
        <h2>Conflicts should be identified early</h2>
        <p>Directors affiliated with a lender, investor or counterparty may need separate counsel, a recusal or a carefully defined committee. The applicable standard of review can turn on whether a majority of decision-makers was disinterested and independent. That determination should not be reconstructed after a transaction is challenged.</p>
        <h2>A practical checklist</h2>
        <ul>
          <li>Prepare a dated chronology of forecast changes and board communications.</li>
          <li>Identify contractual thresholds, liquidity covenants and notice obligations.</li>
          <li>Confirm which directors have interests in the proposed transaction.</li>
          <li>Engage independent advisers where the transaction or conflict structure requires it.</li>
          <li>Record the alternatives, the advice and the reasons for the chosen course.</li>
        </ul>
        <p>The point is not to create defensive paperwork. It is to give directors the information and structure needed to make a difficult decision well. A disciplined record is a by-product of that work.</p>
      </div>
      <div class="alert-legal">This article is general information, not legal advice. Reading it does not create an attorney-client relationship.</div>
      <div class="author-box">
        <img src="assets/images/partner-eleanor.jpg" alt="Representative author portrait">
        <div><span class="small-caps">Written by</span><h3 class="mb-1">Eleanor Whitmore</h3><p class="small text-muted-2 mb-0">Managing Partner · Corporate &amp; Transactions</p></div>
      </div>
    </article>
  </div>
</section>
<section class="section bg-paper">
  <div class="container">
    {section_heading("Related insights", "Continue reading.", "More notes from the firm's practice groups.", centered=True, es_title="Seguir leyendo.")}
    {blog_cards(POSTS[1:4])}
  </div>
</section>
{cta_band()}'''


def pro_bono_page():
    initiatives = [
        ("ph-house-line", "Housing clinic", "Monthly advice and representation for New York tenants facing documentation and habitability issues."),
        ("ph-briefcase", "Small-business clinic", "Contract, formation and IP basics for early-stage entrepreneurs in underserved neighborhoods."),
        ("ph-users-three", "Nonprofit counsel", "Governance and employment policies for community organizations with limited legal budgets."),
    ]
    initiative_html = "".join(
        f'<article class="info-card" data-reveal><i class="ph {icon}" aria-hidden="true"></i><h3>{h(title)}</h3><p>{h(text)}</p></article>' for icon, title, text in initiatives
    )
    return f'''
{page_banner("Pro Bono", "Access to careful legal work should not depend on the size of a client's budget.", [("Home", "index.html"), ("Firm", "about.html"), ("Pro Bono", "")], "Pro Bono", "El acceso a un trabajo jurídico cuidadoso no debería depender del presupuesto del cliente.")}
<section class="section">
  <div class="container">
    <div class="row g-5 align-items-center">
      <div class="col-lg-6" data-reveal>
        <span class="eyebrow">Commitment</span>
        <h2>Part of the practice, not an appendix.</h2>
        <div class="gold-rule"></div>
        <p class="lead-lg">Every attorney is expected to contribute. Pro bono matters are opened, staffed and reviewed with the same conflicts and quality procedures as commercial work.</p>
        <p>Our longest-running program is a monthly clinic operated with a New York community partner. Cases are prepared by an associate and supervised by a partner, with a deliberate handoff protocol so clients always know who is responsible for the file.</p>
        <a class="link-arrow" href="careers.html">Learn about our culture <i class="ph ph-arrow-right" aria-hidden="true"></i></a>
      </div>
      <div class="col-lg-6"><div class="gold-frame mask-reveal"><img src="assets/images/law-books.jpg" alt="Shelves of legal reference books" loading="lazy"><div class="frame-caption">Community legal clinic · New York</div></div></div>
    </div>
  </div>
</section>
<section class="stats-section">
  <div class="container"><div class="stat-grid">
    <div class="stat"><span class="stat-number">2,400+</span><span class="stat-label">Pro bono hours</span></div>
    <div class="stat"><span class="stat-number">14</span><span class="stat-label">Community partners</span></div>
    <div class="stat"><span class="stat-number">100%</span><span class="stat-label">Attorney participation</span></div>
    <div class="stat"><span class="stat-number">2022</span><span class="stat-label">Clinic established</span></div>
  </div></div>
</section>
<section class="section bg-paper">
  <div class="container">
    {section_heading("Initiatives", "Where the work is concentrated.", "Focused programs allow the firm to train associates and build repeatable expertise.", centered=True, es_title="Dónde se concentra el trabajo.")}
    <div class="value-grid" data-reveal-group>{initiative_html}</div>
  </div>
</section>
{cta_band()}'''


def careers_page():
    jobs = [
        ("Corporate Associate, 3–5 years", "New York · Full time", "Support M&A, financings and governance matters with direct partner contact and early drafting responsibility."),
        ("Litigation Associate, 2–4 years", "New York · Full time", "Research, discovery, motion drafting and trial preparation on commercial disputes."),
        ("Regulatory Counsel, 5+ years", "Boston · Full time", "Advise financial institutions and fintech companies on licensing, examinations and compliance."),
        ("Summer Associate, Class of 2027", "New York / Boston · Summer", "A ten-week program with two practice rotations, writing feedback and a supervising partner."),
    ]
    jobs_html = "".join(
        f'''<div class="job-item">
          <button class="job-button" type="button" data-bs-toggle="collapse" data-bs-target="#job-{i}" aria-expanded="{str(i == 1).lower()}" aria-controls="job-{i}">
            <span>{h(title)}<br><span class="job-meta">{h(meta)}</span></span><i class="ph ph-plus" aria-hidden="true"></i>
          </button>
          <div class="collapse{' show' if i == 1 else ''}" id="job-{i}"><div class="job-body"><p>{h(text)}</p><a class="link-arrow" href="mailto:careers@whitmore-hale.com">Apply by email <i class="ph ph-arrow-right" aria-hidden="true"></i></a></div></div>
        </div>''' for i, (title, meta, text) in enumerate(jobs, 1)
    )
    benefits = [
        ("ph-user-focus", "Partner mentoring", "A named partner reviews work and progress twice each year."),
        ("ph-clock", "Sustainable staffing", "Matter teams are monitored for load and predictable time off."),
        ("ph-certificate", "CLE & bar dues", "Admission, CLE and professional membership costs are covered."),
        ("ph-scales", "Pro bono credit", "Pro bono hours count fully toward annual expectations."),
    ]
    benefits_html = "".join(
        f'<article class="benefit-card"><i class="ph {icon}" aria-hidden="true"></i><h3>{h(title)}</h3><p class="small text-muted-2 mb-0">{h(text)}</p></article>' for icon, title, text in benefits
    )
    return f'''
{page_banner("Careers", "Small teams, direct responsibility and standards that do not change with the size of the matter.", [("Home", "index.html"), ("Firm", "about.html"), ("Careers", "")], "Carreras", "Equipos pequeños, responsabilidad directa y estándares que no cambian con el tamaño del asunto.")}
<section class="section">
  <div class="container">
    <div class="about-split">
      <div data-reveal>
        <span class="eyebrow">Life at the firm</span>
        <h2>Learn the work by doing it, with the record in view.</h2>
        <div class="gold-rule"></div>
        <p class="lead-lg">Associates at Whitmore &amp; Hale see the whole matter: the first client call, the strategy discussion, the drafting and the closing or court appearance.</p>
        <p>We hire for judgment, writing and curiosity. Training happens in live matters under close supervision, supported by a short internal syllabus on legal writing, privilege, conflicts and matter management.</p>
      </div>
      <div class="gold-frame mask-reveal"><img src="assets/images/architecture-detail.jpg" alt="New York office building architecture" loading="lazy"><div class="frame-caption">New York · 405 Lexington Avenue</div></div>
    </div>
  </div>
</section>
<section class="section bg-paper">
  <div class="container">
    {section_heading("Benefits", "Professional support, plainly stated.", "No vague culture language; these are the structural commitments.", centered=True, es_title="Apoyo profesional, explicado con claridad.")}
    <div class="benefit-grid" data-reveal>{benefits_html}</div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="row g-5">
      <div class="col-lg-5">{section_heading("Open positions", "Current searches.", "Send a résumé, a short writing sample and a note on the practice that interests you.")}</div>
      <div class="col-lg-7" data-reveal>{jobs_html}</div>
    </div>
  </div>
</section>
<section class="section bg-white">
  <div class="container">
    <div class="row align-items-center g-5">
      <div class="col-lg-5" data-reveal><span class="eyebrow">General application</span><h2>Do not see your role?</h2><p class="lead-lg">We keep applications from strong candidates on file for six months. Rates and compensation are discussed directly and are on request.</p></div>
      <div class="col-lg-7" data-reveal>{contact_form("careers", full=True)}</div>
    </div>
  </div>
</section>
{cta_band()}'''


def faq_page():
    extra_questions = [
        ("How quickly can the firm begin work?", "Timing depends on conflicts, urgency and the documents available. For a genuinely time-sensitive matter, we will state what can be done within the first business day and what cannot."),
        ("Do you work with in-house legal teams?", "Yes. Many matters are jointly staffed. We agree at the outset who owns drafting, board communication, outside advisers and privilege."),
        ("Can you provide a fixed fee?", "For discrete diligence, contract review or defined litigation phases, often yes. The scope and assumptions are set out in the engagement letter."),
        ("What languages are available?", "Spanish-language consultations can be arranged through the New York office. Use the EN / ES control in the utility bar for translated navigation and contact prompts."),
        ("How are client documents handled?", "The firm uses a conflicts-checked matter workspace and a documented retention policy. This website concept does not transmit files or form data."),
        ("Where are the offices located?", "405 Lexington Ave, 26th Fl, New York, NY 10174 and 101 Federal St, 19th Fl, Boston, MA 02110. Office hours appear on the contact page."),
    ]
    return f'''
{page_banner("Frequently Asked Questions", "Direct answers about fees, conflicts, admissions, consultations and how an engagement begins.", [("Home", "index.html"), ("Firm", "about.html"), ("FAQ", "")], "Preguntas frecuentes", "Respuestas directas sobre honorarios, conflictos, colegiación y consultas.")}
<section class="section">
  <div class="container">
    <div class="row g-5">
      <aside class="col-lg-4">
        <div class="sticky-sidebar">
          <div class="sidebar-card">
            <h3>Search questions</h3>
            <label class="form-label" for="faq-search">Keyword</label>
            <input class="form-control" id="faq-search" type="search" data-faq-search placeholder="fees, conflicts, offices">
            <div class="gold-rule short"></div>
            <p class="small text-muted-2 mb-0">If your question is not answered here, contact the intake team. Do not send confidential information through the website.</p>
          </div>
        </div>
      </aside>
      <div class="col-lg-8">
        {section_heading("Engagements", "Before we begin.", "Six questions clients ask most often.")}
        {faq_accordion(FAQS, "faq-page")}
        <div class="mt-5">{section_heading("Working together", "Process and logistics.", "A few practical answers about staffing and communication.")}</div>
        {faq_accordion(extra_questions, "faq-extra")}
        <p class="alert-legal mt-4" data-faq-empty hidden>No questions match that keyword. Try another term or call +1 (212) 555-0170.</p>
      </div>
    </div>
  </div>
</section>
{cta_band()}'''


def testimonials_page():
    quote_cards = "".join(
        f'''<article class="quote-card" data-reveal>
          <i class="ph ph-quotes" aria-hidden="true"></i>
          <blockquote>“{h(quote)}”</blockquote>
          <div class="client">{h(role)} · {h(company)}</div>
        </article>''' for quote, role, company, _ in TESTIMONIALS
    )
    return f'''
{page_banner("Testimonials", "Representative comments about preparation, responsiveness and judgment from the client's side of the table.", [("Home", "index.html"), ("Firm", "about.html"), ("Testimonials", "")], "Testimonios", "Comentarios representativos sobre preparación, respuesta y criterio jurídico.")}
<section class="section">
  <div class="container">
    {section_heading("In their words", "What clients notice.", "The same themes recur: a clear plan, a partner who stays involved and no avoidable surprises.", centered=True, es_title="Lo que observan los clientes.")}
    <div class="quote-grid" data-reveal-group>{quote_cards}</div>
    <p class="disclaimer-note text-center mt-4">Testimonials are illustrative website copy and are not endorsements from actual clients.</p>
  </div>
</section>
<section class="section testimonial-section">
  <div class="container">
    {section_heading("Featured comment", "A closer look.", "Use the arrows to move between representative comments.", centered=True, es_title="Un comentario destacado.")}
    {testimonial_slider()}
  </div>
</section>
{cta_band()}'''


def contact_page():
    return f'''
{page_banner("Contact", "A confidential starting point for a new matter, with two offices and a response within one business day.", [("Home", "index.html"), ("Contact", "")], "Contacto", "Un punto de partida confidencial para un nuevo asunto, con dos oficinas y respuesta en un día hábil.")}
<section class="section" id="consultation">
  <div class="container">
    <div class="contact-layout">
      <div data-reveal>{contact_form("contact", full=True)}</div>
      <aside class="contact-aside" id="offices" data-reveal>
        <span class="eyebrow">Offices &amp; hours</span>
        <h2>Where to find us.</h2>
        <div class="gold-rule"></div>
        <div class="office-block">
          <h3>New York</h3>
          <p><i class="ph ph-map-pin" aria-hidden="true"></i>405 Lexington Ave, 26th Fl<br>New York, NY 10174</p>
          <p><i class="ph ph-phone" aria-hidden="true"></i><a href="tel:+12125550170">+1 (212) 555-0170</a></p>
          <p class="mb-0"><i class="ph ph-envelope" aria-hidden="true"></i><a href="mailto:intake@whitmore-hale.com">intake@whitmore-hale.com</a></p>
        </div>
        <div class="office-block">
          <h3>Boston</h3>
          <p><i class="ph ph-map-pin" aria-hidden="true"></i>101 Federal St, 19th Fl<br>Boston, MA 02110</p>
          <p class="mb-0"><i class="ph ph-phone" aria-hidden="true"></i><a href="tel:+16175550184">+1 (617) 555-0184</a></p>
        </div>
        <h3 class="mt-4">Office hours</h3>
        <table class="hours-table">
          <tbody><tr><td>Monday – Friday</td><td>9:00 – 6:00</td></tr><tr><td>Saturday – Sunday</td><td>By appointment</td></tr><tr><td>Client portal</td><td>24 / 7</td></tr></tbody>
        </table>
        <p class="small mt-3 mb-0"><i class="ph ph-question" aria-hidden="true"></i> Rates are on request. Attorney Advertising.</p>
      </aside>
    </div>
  </div>
</section>
<section class="contact-map-full" aria-label="Midtown Manhattan office map">
  <img src="assets/images/map-midtown.png" alt="Local street map of Midtown Manhattan near Lexington Avenue and East 42nd Street" loading="lazy">
  <div class="map-overlay-card">
    <span class="eyebrow">New York headquarters</span>
    <h3>405 Lexington Avenue</h3>
    <p class="text-muted-2">26th Floor · New York, NY 10174<br>Adjacent to Grand Central Terminal</p>
    <a class="link-arrow" href="tel:+12125550170">Call the office <i class="ph ph-arrow-right" aria-hidden="true"></i></a>
  </div>
</section>
<section class="section bg-paper">
  <div class="container">
    <div class="row g-5 align-items-center">
      <div class="col-lg-6">{office_cards()}</div>
      <div class="col-lg-6" data-reveal>
        <span class="eyebrow">Before you write</span>
        <h2>Please do not send confidential details online.</h2>
        <p class="lead-lg">An initial message should include only your name, contact details, the general practice area and a short description. We will complete a conflicts check before any substantive discussion.</p>
        <p>Submitting a form on this website does not create an attorney-client relationship. If a filing deadline is imminent, call the New York office directly.</p>
        <a class="btn-wh-navy" href="faq.html">Read the FAQ <i class="ph ph-arrow-right" aria-hidden="true"></i></a>
      </div>
    </div>
  </div>
</section>
{cta_band()}'''


def privacy_page():
    return f'''
{page_banner("Privacy", "How this website concept handles information, local storage and forms.", [("Home", "index.html"), ("Privacy", "")], "Privacidad", "Cómo este concepto de sitio web trata la información, el almacenamiento local y los formularios.")}
<section class="section">
  <div class="container">
    <div class="detail-layout">
      <aside class="sticky-sidebar"><div class="sidebar-card"><h3>Contents</h3><ul class="sidebar-nav"><li><a class="active" href="#scope">Scope</a></li><li><a href="#information">Information</a></li><li><a href="#storage">Local storage</a></li><li><a href="#forms">Forms</a></li><li><a href="#contact">Contact</a></li></ul></div></aside>
      <article class="prose" data-reveal>
        <span class="eyebrow">Last updated November 2, 2026</span>
        <h2 id="scope">Scope</h2>
        <p>This page describes the informational website concept for Whitmore &amp; Hale LLP. It is not a client portal, does not authenticate users and does not send form contents to a server. A production law-firm website would require a reviewed policy that reflects its actual intake, analytics and document systems.</p>
        <h2 id="information">Information we collect</h2>
        <p>The site does not run third-party analytics, advertising pixels or remote font requests. All fonts, icons, scripts, logos and images are loaded from this site's own <code>assets/</code> directory. Standard web-server logs may record an IP address, requested path, user agent and timestamp for security and diagnostics.</p>
        <h2 id="storage">Local storage</h2>
        <p>The EN / ES language control stores a single preference, <code>wh-language</code>, in your browser's local storage. It contains either <code>en</code> or <code>es</code> and is not transmitted to the firm. Clearing browser data removes it.</p>
        <h2 id="forms">Forms and the client portal</h2>
        <p>Consultation, newsletter, careers and portal forms are front-end demonstrations. They validate locally, display a confirmation and then reset. No credentials, messages or email addresses are transmitted. Do not enter real passwords or confidential facts into the portal preview.</p>
        <h2 id="contact">Contact and changes</h2>
        <p>Questions about privacy may be directed to <a href="mailto:privacy@whitmore-hale.com">privacy@whitmore-hale.com</a> or +1 (212) 555-0170. This notice may be updated as the site's functionality changes.</p>
        <div class="alert-legal">Attorney Advertising. This website and its sample content are illustrative and do not constitute legal advice.</div>
      </article>
    </div>
  </div>
</section>
<section class="section section-sm bg-paper"><div class="container text-center"><img src="assets/brand/logo-mono.svg" alt="Whitmore &amp; Hale LLP monochrome logo" style="width:240px;max-width:70%"><p class="small-caps mt-4 mb-0">A document with a clear record</p></div></section>'''


def terms_page():
    return f'''
{page_banner("Terms", "Terms governing the use of this informational website concept.", [("Home", "index.html"), ("Terms", "")], "Términos", "Términos que rigen el uso de este sitio web informativo.")}
<section class="section">
  <div class="container">
    <article class="article-column prose" data-reveal>
      <span class="small-caps">Last updated November 2, 2026</span>
      <h2>Informational use only</h2>
      <p>The content on this site is general information and is not legal advice. Reading an article, submitting a demonstration form or contacting the firm through the site does not create an attorney-client relationship. Legal advice is provided only after a conflicts check and a written engagement agreement.</p>
      <h2>Illustrative content</h2>
      <p>Attorney names, client testimonials, recognition references, statistics and case results are illustrative for this design concept. Prior results do not guarantee a similar outcome. Portraits are representative stock photography and do not depict actual personnel.</p>
      <h2>No remote dependencies</h2>
      <p>The site intentionally loads Bootstrap, Phosphor Icons, GSAP, webfonts, logos, photographs and scripts from local files. It does not embed third-party maps, analytics, advertising or social widgets. External links, where present, are provided for convenience only.</p>
      <h2>Intellectual property</h2>
      <p>The Whitmore &amp; Hale name, supplied logo artwork, layout and original text are used for this website concept. Third-party software and font files remain subject to their respective licenses, copies of which are included in <code>assets/vendor/</code>.</p>
      <h2>Accessibility</h2>
      <p>The site is built with semantic headings, keyboard-visible focus states, text alternatives, reduced-motion support and a skip link. If you encounter an accessibility barrier, contact the office so it can be corrected.</p>
      <h2>Contact</h2>
      <p>Questions about these terms may be sent to <a href="mailto:intake@whitmore-hale.com">intake@whitmore-hale.com</a> or +1 (212) 555-0170.</p>
      <div class="alert-legal">Attorney Advertising · New York &amp; Massachusetts State Bar admissions · Rates on request.</div>
    </article>
  </div>
</section>'''


def not_found_page():
    links = [
        ("Home", "index.html"), ("Practice Areas", "practice-areas.html"), ("Attorneys", "attorneys.html"),
        ("Insights", "insights.html"), ("Contact", "contact.html"),
    ]
    link_html = "".join(f'<a href="{url}">{h(label)}</a>' for label, url in links)
    return f'''
<section class="error-page">
  <div class="container">
    <img class="error-crest" src="assets/brand/logo-vertical.svg" alt="Whitmore &amp; Hale LLP crest">
    <span class="eyebrow">Page not found</span>
    <span class="error-code">404</span>
    <h1>The page is not in the record.</h1>
    <p class="lead-lg mx-auto" style="max-width:560px">The address may be outdated, or the document may have moved. Use the links below or return to the home page.</p>
    <div class="error-links">{link_html}</div>
  </div>
</section>'''


PAGES = [
    ("index.html", "Corporate Law Firm in New York", "Whitmore & Hale LLP is a New York corporate law firm advising businesses, boards and families in transactions, disputes and regulation.", "home", "home", home_page),
    ("about.html", "About the Firm", "Learn about the history, values, timeline and attorneys of Whitmore & Hale LLP, a New York law firm founded in 1998.", "firm", "about", about_page),
    ("practice-areas.html", "Practice Areas", "Explore eight corporate, litigation, tax, real-estate, employment, IP, family and banking practices.", "practice", "practice-areas", practice_areas_page),
    ("practice-area-detail.html", "Practice Area Detail", "Detailed capabilities, approach and representative experience for a Whitmore & Hale practice area.", "practice", "practice-detail", practice_detail_page),
    ("attorneys.html", "Attorneys", "Meet the partners, counsel and associates of Whitmore & Hale LLP in New York and Boston.", "attorneys", "attorneys", attorneys_page),
    ("attorney-profile.html", "Attorney Profile", "Biography, admissions, education and focus areas for a Whitmore & Hale attorney.", "attorneys", "attorney-profile", attorney_profile_page),
    ("case-results.html", "Case Results", "Selected judgments, settlements and transactions from Whitmore & Hale LLP.", "results", "case-results", case_results_page),
    ("insights.html", "Insights", "Practical legal articles on transactions, disputes, employment, tax and intellectual property.", "insights", "insights", insights_page),
    ("blog-single.html", "Fiduciary Duties When a Growth Company Misses Its Plan", "An insights article on board process, conflicts and minutes when a growth company misses its plan.", "insights", "blog-single", blog_single_page),
    ("pro-bono.html", "Pro Bono", "Whitmore & Hale LLP pro bono clinics, community partners and attorney participation.", "firm", "pro-bono", pro_bono_page),
    ("careers.html", "Careers", "Open positions, benefits, training and culture at Whitmore & Hale LLP.", "firm", "careers", careers_page),
    ("faq.html", "FAQ", "Answers about legal fees, consultations, conflicts, courts and working with Whitmore & Hale LLP.", "firm", "faq", faq_page),
    ("testimonials.html", "Testimonials", "Representative client comments on preparation, responsiveness and legal judgment.", "firm", "testimonials", testimonials_page),
    ("contact.html", "Contact", "Contact Whitmore & Hale LLP in New York or Boston and request a consultation.", "contact", "contact", contact_page),
    ("privacy.html", "Privacy", "Privacy notice for the Whitmore & Hale LLP website concept.", "", "privacy", privacy_page),
    ("terms.html", "Terms", "Terms of use for the Whitmore & Hale LLP website concept.", "", "terms", terms_page),
    ("404.html", "Page Not Found", "The requested Whitmore & Hale LLP page could not be found.", "", "404", not_found_page),
]


def main():
    for filename, title, description, active, page, builder in PAGES:
        extra = '<meta name="robots" content="noindex">' if filename == "404.html" else ""
        html = shell(title, description, builder(), active, page, extra)
        (ROOT / filename).write_text(html + "\n", encoding="utf-8")
        print(f"wrote {filename}")
    (ROOT / "robots.txt").write_text("User-agent: *\nAllow: /\n", encoding="utf-8")
    print(f"wrote {len(PAGES)} pages")


if __name__ == "__main__":
    main()
