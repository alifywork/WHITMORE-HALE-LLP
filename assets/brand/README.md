# Brand assets

`header-logo.png` and `logo-with-bg.png` are the two original files supplied by
the client. All other logo/favicon files are deterministic local derivatives of
`header-logo.png`.

The SVG files are self-contained wrappers around local PNG derivatives: the PNG
is embedded as a data URI and the label is XML-escaped, so the files render when
used as an `<img>` source. Root-level `logo*.svg` and `favicon.svg` files provide
the exact URLs requested in the brief. No remote logo or icon service is used.
