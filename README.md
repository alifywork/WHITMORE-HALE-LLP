# Whitmore & Hale LLP — static corporate law-firm website

A 17-page, fully local editorial website concept for a New York corporate law firm with a Boston office. The visual language follows the supplied brand brief: deep navy, antique gold, Playfair Display headings, Source Sans 3 body copy, thin rules, real photography, generous whitespace and restrained motion.

## Run locally

The site is plain static HTML and needs no build step or backend:

```bash
python3 -m http.server 4173 --bind 0.0.0.0
# then open http://localhost:4173/
```

Open `index.html` directly also works, although the local HTTP server is recommended for fonts and the web manifest.

## Everything is local

No CDN, Google Fonts, remote icon font, remote map, analytics, social widget or image service is used at runtime.

| Resource | Local location |
|---|---|
| Bootstrap 5.3.3 CSS/JS | `assets/vendor/bootstrap/` |
| Phosphor Icons Web 2.1.2 | `assets/vendor/phosphor/regular/` — equivalent Phosphor classes replace the brief's Font Awesome map so a single local icon font is loaded |
| GSAP 3.13.0 + ScrollTrigger | `assets/vendor/gsap/` |
| Playfair Display + Source Sans 3 | `assets/vendor/fontsource/` |
| Supplied logos, all SVG variants and favicons | root-level `logo*.svg`, `favicon*`, `apple-touch-icon.png` and `site.webmanifest`; source/PNG derivatives in `assets/brand/` |
| Optimized local photographs and map | `assets/images/` |
| Site CSS / JavaScript | `assets/css/`, `assets/js/main.js` |

`assets/vendor/README.md` records versions and license files. `assets/images/CREDITS.md` records photography sources and notes that portraits are representative.

## Pages

`index.html`, `about.html`, `practice-areas.html`, `practice-area-detail.html`, `attorneys.html`, `attorney-profile.html`, `case-results.html`, `insights.html`, `blog-single.html`, `pro-bono.html`, `careers.html`, `faq.html`, `testimonials.html`, `contact.html`, `privacy.html`, `terms.html`, `404.html`.

The practice-detail and attorney-profile pages are data-driven from local JavaScript:

- `practice-area-detail.html?area=litigation`
- `attorney-profile.html?attorney=marcus`
- `contact.html?area=tax#consultation` pre-selects a practice area.

## Interactions

- Bootstrap collapse, dropdown, accordion and modal.
- GSAP Ken Burns hero, staggered card reveals, clip-path image reveals, animated counters, SVG timeline line-draw and ScrollTrigger sequencing.
- CSS sticky sidebars and `prefers-reduced-motion` fallback.
- Local testimonial slider, case-result filters, FAQ search, language preference and smooth in-page anchors.
- Consultation, newsletter, careers and portal forms validate locally and explicitly state that they do not transmit data.

## Regeneration

```bash
python3 tools/build_site.py        # regenerate the 17 HTML pages
python3 tools/prepare_assets.py    # re-download pinned npm packages and rebuild brand derivatives
```

`prepare_assets.py` needs `npm`, ImageMagick's `convert`, and the two original client logo PNGs already present in `assets/brand/`. It downloads from `registry.npmjs.org` and keeps all runtime files in `assets/vendor/`. Optimized photographs remain committed, so the site does not depend on the temporary `image-search/` source folder.

## Compliance notes

The site is a design concept. Attorney names, testimonials, recognition references, statistics, case results and client-portal behavior are illustrative. The footer includes Attorney Advertising, prior-results, bar-admission and representative-photography disclosures. Connect a secure intake endpoint and replace illustrative copy with approved content before publication.
