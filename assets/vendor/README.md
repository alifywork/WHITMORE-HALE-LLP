# Local vendor bundle

All runtime libraries are vendored; no CDN is used.

| Package | Version | Local path |
|---|---:|---|
| Bootstrap | 5.3.3 | `bootstrap/` |
| Phosphor Icons Web | 2.1.2 | `phosphor/` |
| GSAP + ScrollTrigger | 3.13.0 | `gsap/` |
| Fontsource Playfair Display | 5.2.8 | `fontsource/playfair-display/` |
| Fontsource Source Sans 3 | 5.2.8 | `fontsource/source-sans-3/` |

Regenerate with `python3 tools/prepare_assets.py`. Packages are fetched from
`registry.npmjs.org`; license files are included beside each package.
