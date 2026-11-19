# The World Today — 18 November 2026 (round 2)

A 1024x1024 front page summing up Wednesday 18 November 2026 in six
stories, refreshed with the fuller day's news: the Xi–Putin meeting in
Shenzhen and Trump's arrival for Thursday's trilateral, Iranian drone
attacks intercepted over the Gulf, the Democrats taking the US Senate,
Voyager 1 reaching one light-day from Earth, Anthropic's $1.5tn IPO,
and Cyclone Akvan's evacuations in Odisha.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/news18-v2-out python3 main.py
```

`main.py` (Python standard library only, no network) copies `entry.png`
into `$MAKEFUN_OUTPUT_DIR/entry.png` and refuses to run if the image's
sha256 or size does not match the reviewed round-2 image.

## Image

`entry.png` is a flat, PIL-drawn front page: masthead, six illustrated
story tiles, no AI imagery, no faces. Every story was verified against
reporting dated 18 November 2026 (AFP, AP, BBC, NASA, IMD, Al Jazeera).

## License

MIT — see LICENSE.
