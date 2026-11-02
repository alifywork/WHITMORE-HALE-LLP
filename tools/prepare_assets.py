#!/usr/bin/env python3
"""Prepare the fully local asset bundle for the Whitmore & Hale LLP website.

Downloads pinned npm packages from registry.npmjs.org, copies only the files the
site uses, optimizes the selected stock photographs, and derives the supplied
logo variants/favicons with ImageMagick. Run from anywhere:

    python3 tools/prepare_assets.py

The two original user-supplied PNGs must already be in assets/brand/.
Photograph source thumbnails are read from image-search/ when present; the
optimized files in assets/images/ are committed and are what the site loads.
"""

from __future__ import annotations

import base64
import json
import html
import shutil
import subprocess
import sys
import tarfile
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
BRAND = ASSETS / "brand"
IMAGES = ASSETS / "images"
VENDOR = ASSETS / "vendor"
SOURCE_IMAGES = ROOT / "image-search"

PACKAGES = {
    "bootstrap-5.3.3.tgz": "bootstrap@5.3.3",
    "phosphor-icons-web-2.1.2.tgz": "@phosphor-icons/web@2.1.2",
    "gsap-3.13.0.tgz": "gsap@3.13.0",
    "fontsource-playfair-display-5.2.8.tgz": "@fontsource/playfair-display@5.2.8",
    "fontsource-source-sans-3-5.2.8.tgz": "@fontsource/source-sans-3@5.2.8",
}

PHOTO_MAP = {
    "hero-courthouse.jpg": "site-pexels-com-photo-courthouse-columns-1.jpg",
    "courthouse-facade.jpg": "new-york-state-supreme-court-courthouse--1.jpg",
    "colonnade.jpg": "site-pexels-com-photo-courthouse-columns-3.jpg",
    "library-interior.jpg": "law-library-books-wood-interior-elegant--1.jpg",
    "reading-room.jpg": "new-york-public-library-reading-room-int-2.jpg",
    "law-books.jpg": "site-pexels-com-photo-law-books-library--1.jpg",
    "contract-review.jpg": "legal-contract-documents-desk-gavel-pen--3.jpg",
    "meeting-room.jpg": "site-pexels-com-photo-business-meeting-c-3.jpg",
    "ny-office.jpg": "new-york-office-building-interior-boardr-1.jpg",
    "boston-office.jpg": "boston-back-bay-office-building-architec-1.jpg",
    "architecture-detail.jpg": "new-york-office-building-interior-boardr-3.jpg",
    "map-midtown.png": "midtown-manhattan-street-map-lexington-a-3.png",
    "partner-eleanor.jpg": "older-woman-lawyer-professional-headshot-2.jpg",
    "partner-arthur.jpg": "older-man-lawyer-professional-headshot-s-1.jpg",
    "partner-marcus.jpg": "professional-lawyer-headshot-neutral-sui-4.jpg",
    "partner-claire.jpg": "professional-lawyer-headshot-neutral-sui-3.jpg",
    "attorney-daniel.jpg": "professional-lawyer-headshot-neutral-sui-1.jpg",
    "attorney-julian.jpg": "professional-lawyer-headshot-neutral-sui-2.jpg",
    "attorney-amara.jpg": "professional-lawyer-headshot-neutral-sui-5.jpg",
    "attorney-naomi.jpg": "older-woman-lawyer-professional-headshot-1.jpg",
}


def run(*args: str) -> None:
    subprocess.run(args, cwd=ROOT, check=True, stdout=subprocess.DEVNULL)


def copy(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)


def sync_vendor() -> None:
    print("Downloading pinned local vendor packages...")
    with tempfile.TemporaryDirectory(prefix="wh-vendor-") as tmp:
        tmp_path = Path(tmp)
        subprocess.run(
            ["npm", "pack", "--silent", "--pack-destination", str(tmp_path), *PACKAGES.values()],
            cwd=ROOT,
            check=True,
            stdout=subprocess.DEVNULL,
        )
        extracted = tmp_path / "extracted"
        extracted.mkdir()
        for tarball in tmp_path.glob("*.tgz"):
            with tarfile.open(tarball) as archive:
                archive.extractall(extracted / tarball.stem)

        def pkg(filename: str) -> Path:
            return extracted / Path(filename).stem / "package"

        bootstrap = pkg("bootstrap-5.3.3.tgz")
        copy(bootstrap / "dist/css/bootstrap.min.css", VENDOR / "bootstrap/css/bootstrap.min.css")
        copy(bootstrap / "dist/css/bootstrap.min.css.map", VENDOR / "bootstrap/css/bootstrap.min.css.map")
        copy(bootstrap / "dist/js/bootstrap.bundle.min.js", VENDOR / "bootstrap/js/bootstrap.bundle.min.js")
        copy(bootstrap / "dist/js/bootstrap.bundle.min.js.map", VENDOR / "bootstrap/js/bootstrap.bundle.min.js.map")
        copy(bootstrap / "LICENSE", VENDOR / "bootstrap/LICENSE.txt")

        phosphor = pkg("phosphor-icons-web-2.1.2.tgz") / "src/regular"
        for name in ("style.css", "Phosphor.woff2", "Phosphor.woff", "Phosphor.ttf", "Phosphor.svg"):
            copy(phosphor / name, VENDOR / "phosphor/regular" / name)
        copy(pkg("phosphor-icons-web-2.1.2.tgz") / "LICENSE", VENDOR / "phosphor/LICENSE.txt")

        gsap_root = pkg("gsap-3.13.0.tgz")
        gsap = gsap_root / "dist"
        for name in ("gsap.min.js", "gsap.min.js.map", "ScrollTrigger.min.js", "ScrollTrigger.min.js.map"):
            copy(gsap / name, VENDOR / "gsap" / name)
        copy(gsap_root / "README.md", VENDOR / "gsap/README.md")
        (VENDOR / "gsap" / "LICENSE-NOTICE.md").write_text(
            "GSAP 3.13.0 is distributed under GreenSock's standard license.\n"
            "The npm package does not ship a standalone LICENSE file; retain the\n"
            "upstream package metadata and README included here for attribution.\n",
            encoding="utf-8",
        )

        font_specs = {
            "playfair-display": ("fontsource-playfair-display-5.2.8.tgz", ["latin-400-italic.css", "latin-600.css", "latin-700.css", "latin-700-italic.css"]),
            "source-sans-3": ("fontsource-source-sans-3-5.2.8.tgz", ["latin-400.css", "latin-400-italic.css", "latin-600.css", "latin-700.css"]),
        }
        for folder, (filename, css_files) in font_specs.items():
            source_root = pkg(filename)
            destination = VENDOR / "fontsource" / folder
            for css_name in css_files:
                copy(source_root / css_name, destination / css_name)
                weight_part = css_name.replace("latin-", "").replace(".css", "")
                variant = weight_part if "italic" in weight_part else f"{weight_part}-normal"
                base = "playfair-display" if folder == "playfair-display" else "source-sans-3"
                for ext in ("woff2", "woff"):
                    font_name = f"{base}-latin-{variant}.{ext}"
                    copy(source_root / "files" / font_name, destination / "files" / font_name)
            copy(source_root / "LICENSE", destination / "LICENSE.txt")

    (VENDOR / "README.md").write_text(
        """# Local vendor bundle\n\nAll runtime libraries are vendored; no CDN is used.\n\n| Package | Version | Local path |\n|---|---:|---|\n| Bootstrap | 5.3.3 | `bootstrap/` |\n| Phosphor Icons Web | 2.1.2 | `phosphor/` |\n| GSAP + ScrollTrigger | 3.13.0 | `gsap/` |\n| Fontsource Playfair Display | 5.2.8 | `fontsource/playfair-display/` |\n| Fontsource Source Sans 3 | 5.2.8 | `fontsource/source-sans-3/` |\n\nRegenerate with `python3 tools/prepare_assets.py`. Packages are fetched from\n`registry.npmjs.org`; license files are included beside each package.\n""",
        encoding="utf-8",
    )


def sync_photos() -> None:
    if not SOURCE_IMAGES.exists():
        print("image-search/ not present; keeping existing optimized photographs.")
        return
    print("Optimizing selected local photographs...")
    for target, source_name in PHOTO_MAP.items():
        source = SOURCE_IMAGES / source_name
        if not source.exists():
            print(f"  ! missing source: {source_name}")
            continue
        destination = IMAGES / target
        destination.parent.mkdir(parents=True, exist_ok=True)
        command = ["convert", str(source), "-auto-orient", "-strip"]
        if target == "architecture-detail.jpg":
            command += ["-resize", "1000x1500>"]
        if destination.suffix.lower() in {".jpg", ".jpeg"}:
            command += ["-sampling-factor", "4:2:0", "-interlace", "Plane", "-quality", "86"]
        command.append(str(destination))
        subprocess.run(command, cwd=ROOT, check=True, stdout=subprocess.DEVNULL)


def image_size(path: Path) -> tuple[int, int]:
    output = subprocess.check_output(
        ["identify", "-format", "%w %h", str(path)], cwd=ROOT, text=True
    ).strip()
    width, height = output.split()
    return int(width), int(height)


def svg_with_embedded_png(source: Path, target: Path, label: str) -> None:
    """Create a self-contained SVG wrapper around a local PNG derivative.

    The PNG is embedded as a data URI because SVG-as-image decoders do not load
    relative external resources. The label is XML-escaped so an ampersand in the
    firm name cannot make the SVG invalid.
    """
    width, height = image_size(source)
    encoded = base64.b64encode(source.read_bytes()).decode("ascii")
    safe_label = html.escape(label, quote=True)
    target.write_text(
        f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="{safe_label}">
  <image width="{width}" height="{height}" preserveAspectRatio="xMidYMid meet" href="data:image/png;base64,{encoded}" xlink:href="data:image/png;base64,{encoded}"/>
</svg>
''',
        encoding="utf-8",
    )


def build_brand() -> None:
    print("Deriving logo variants and favicons from the supplied artwork...")
    header = BRAND / "header-logo.png"
    if not header.exists():
        raise SystemExit(f"Missing supplied logo: {header}")

    work = BRAND / "_derived"
    work.mkdir(parents=True, exist_ok=True)
    alpha = work / "alpha.png"
    white_all = work / "white-all.png"
    white_final = work / "logo-white.png"
    mono = work / "logo-mono.png"
    scale_region = work / "scale-region.png"
    icon = work / "icon.png"
    wordmark = work / "wordmark.png"
    vertical = work / "logo-vertical.png"
    favicon_bg = work / "favicon-bg.png"
    favicon_master = work / "favicon-512.png"

    run("convert", str(header), "-alpha", "extract", str(alpha))
    run("convert", "-size", "469x125", "xc:white", str(alpha), "-alpha", "off", "-compose", "CopyOpacity", "-composite", str(white_all))
    run("convert", str(header), "-crop", "160x125+0+0", "+repage", str(scale_region))
    run("convert", str(white_all), str(scale_region), "-gravity", "NorthWest", "-compose", "Over", "-composite", str(white_final))
    run("convert", "-size", "469x125", "xc:#0A2540", str(alpha), "-alpha", "off", "-compose", "CopyOpacity", "-composite", str(mono))
    run("convert", str(header), "-crop", "160x125+0+0", "+repage", "-trim", "+repage", "-bordercolor", "none", "-border", "12", str(icon))
    run("convert", str(header), "-crop", "309x125+160+0", "+repage", "-trim", "+repage", str(wordmark))
    run(
        "convert", "-size", "360x250", "xc:none",
        "(", str(icon), "-resize", "x130", ")",
        "-gravity", "North", "-geometry", "+0+10", "-composite",
        "(", str(wordmark), "-resize", "330x", ")",
        "-gravity", "South", "-geometry", "+0+18", "-composite",
        str(vertical),
    )
    run("convert", "-size", "512x512", "xc:none", "-fill", "#0A2540", "-draw", "roundrectangle 0,0 511,511 41,41", str(favicon_bg))
    run(
        "convert", str(favicon_bg),
        "(", str(icon), "-resize", "315x315", ")",
        "-gravity", "Center", "-geometry", "+0-28", "-composite",
        "-stroke", "#B08D3F", "-strokewidth", "5", "-fill", "none",
        "-draw", "roundrectangle 16,16 495,495 34,34",
        "-font", "DejaVu-Serif-Bold", "-pointsize", "46", "-fill", "#B08D3F", "-stroke", "none",
        "-gravity", "South", "-annotate", "+0+40", "WH",
        str(favicon_master),
    )

    for size in (16, 32, 48, 192, 512):
        run("convert", str(favicon_master), "-resize", f"{size}x{size}", str(BRAND / f"favicon-{size}.png"))
    run("convert", str(favicon_master), "-resize", "180x180", str(BRAND / "apple-touch-icon.png"))
    run(
        "convert", str(BRAND / "favicon-16.png"), str(BRAND / "favicon-32.png"), str(BRAND / "favicon-48.png"),
        str(BRAND / "favicon.ico"),
    )

    derived_pngs = {
        "logo.png": header,
        "logo-white.png": white_final,
        "logo-mono.png": mono,
        "logo-icon-only.png": icon,
        "logo-vertical.png": vertical,
        "favicon.png": favicon_master,
    }
    for name, source in derived_pngs.items():
        copy(source, BRAND / name)

    brand_svg_specs = [
        (BRAND / "logo.png", BRAND / "logo.svg", "Whitmore & Hale LLP horizontal logo"),
        (BRAND / "logo.png", BRAND / "logo-horizontal.svg", "Whitmore & Hale LLP horizontal logo"),
        (BRAND / "logo-white.png", BRAND / "logo-white.svg", "Whitmore & Hale LLP white and gold logo"),
        (BRAND / "logo-mono.png", BRAND / "logo-mono.svg", "Whitmore & Hale LLP monochrome navy logo"),
        (BRAND / "logo-icon-only.png", BRAND / "logo-icon-only.svg", "Whitmore & Hale LLP scales mark"),
        (BRAND / "logo-vertical.png", BRAND / "logo-vertical.svg", "Whitmore & Hale LLP vertical logo"),
        (BRAND / "favicon.png", BRAND / "favicon.svg", "Whitmore & Hale LLP WH crest"),
    ]
    for source, target, label in brand_svg_specs:
        svg_with_embedded_png(source, target, label)

    root_svg_specs = [
        (BRAND / "logo.png", ROOT / "logo.svg", "Whitmore & Hale LLP horizontal logo"),
        (BRAND / "logo.png", ROOT / "logo-horizontal.svg", "Whitmore & Hale LLP horizontal logo"),
        (BRAND / "logo-white.png", ROOT / "logo-white.svg", "Whitmore & Hale LLP white and gold logo"),
        (BRAND / "logo-mono.png", ROOT / "logo-mono.svg", "Whitmore & Hale LLP monochrome navy logo"),
        (BRAND / "logo-icon-only.png", ROOT / "logo-icon-only.svg", "Whitmore & Hale LLP scales mark"),
        (BRAND / "logo-vertical.png", ROOT / "logo-vertical.svg", "Whitmore & Hale LLP vertical logo"),
        (BRAND / "favicon.png", ROOT / "favicon.svg", "Whitmore & Hale LLP WH crest"),
    ]
    for source, target, label in root_svg_specs:
        svg_with_embedded_png(source, target, label)

    for name in (
        "header-logo.png", "logo-with-bg.png", "favicon-16.png", "favicon-32.png",
        "favicon-48.png", "favicon-192.png", "favicon-512.png", "apple-touch-icon.png", "favicon.ico",
    ):
        copy(BRAND / name, ROOT / name)

    manifest = {
        "name": "Whitmore & Hale LLP",
        "short_name": "Whitmore Hale",
        "icons": [
            {"src": "favicon-192.png", "sizes": "192x192", "type": "image/png"},
            {"src": "favicon-512.png", "sizes": "512x512", "type": "image/png"},
        ],
        "theme_color": "#0A2540",
        "background_color": "#FBFAF7",
        "display": "standalone",
        "start_url": "./",
    }
    (BRAND / "site.webmanifest").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    root_manifest = dict(manifest)
    root_manifest["icons"] = [
        {"src": "assets/brand/favicon-192.png", "sizes": "192x192", "type": "image/png"},
        {"src": "assets/brand/favicon-512.png", "sizes": "512x512", "type": "image/png"},
    ]
    (ROOT / "site.webmanifest").write_text(json.dumps(root_manifest, indent=2) + "\n", encoding="utf-8")

    (BRAND / "README.md").write_text(
        """# Brand assets\n\n`header-logo.png` and `logo-with-bg.png` are the two original files supplied by\nthe client. All other logo/favicon files are deterministic local derivatives of\n`header-logo.png`.\n\nThe SVG files are self-contained wrappers around local PNG derivatives: the PNG\nis embedded as a data URI and the label is XML-escaped, so the files render when\nused as an `<img>` source. Root-level `logo*.svg` and `favicon.svg` files provide\nthe exact URLs requested in the brief. No remote logo or icon service is used.\n""",
        encoding="utf-8",
    )
    shutil.rmtree(work)


def main() -> None:
    BRAND.mkdir(parents=True, exist_ok=True)
    IMAGES.mkdir(parents=True, exist_ok=True)
    sync_vendor()
    sync_photos()
    build_brand()
    print("Local assets are ready.")


if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as exc:
        print(f"Asset preparation failed: {exc}", file=sys.stderr)
        raise
