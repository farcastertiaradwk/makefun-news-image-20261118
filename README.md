# The World Today — 18 November 2026

make.fun news-image-20261118 entry: one image summing up the world's news of
Wednesday 18 November 2026.

`main.py` (Python 3.13, standard library only) copies `entry.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`), with a size cap and a
sha256 guard. No network; both runs write identical bytes.

The image is a newspaper front page: masthead "THE WORLD TODAY" with the date,
then six stories — APEC opens in Shenzhen; Hormuz shipping at a standstill;
Trump in Manila for Quad talks; the EU seeks €45bn more for Ukraine; the UK
sanctions settlement firms; Cyclone Akvan strengthens. Drawn with PIL from
verified reporting (BBC · AP · Reuters · Al Jazeera · UKMTO · IMD).

License: MIT.
