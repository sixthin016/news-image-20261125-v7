# news-image-20261125-v7

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/sixthin016/news-image-20261125-v7/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/sixthin016/news-image-20261125-v7/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

Sum up 25 November's world news in one image: a newspaper front page
for Wednesday 25 November 2026 — 48 stories, 8 regions, 17 fields,
every one first reported on Wednesday 25 November 2026 and verified
against a named source (Reuters, AP, AFP, BBC, Xinhua/CMSA, Ofgem,
ABS, UN Women, BEA).

## Run it

```sh
python3 main.py
```

The program copies `assets/entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`
(or `/output/entry.png`). The image is drawn at build time by
`tools/generate.py` (Pillow + system fonts) from the day's reported
news; the entry program itself uses only the Python standard library,
no network, and is byte-deterministic across runs (two runs produce
identical bytes, verified by sha256).

Regenerate the image:

```sh
python3 tools/generate.py
```

## What's in the picture

- **Three leads, all drawn** — the consensus top stories of the day,
  which the previous entry missed: the US proposes Section 301
  tariffs on 14 economies (China 20% on top of 25%); the Kospi
  crashes 6.2% to 4,697.51 as Samsung (-9.9%) and SK Hynix (-11.1%)
  lead an Asian chip rout; Shenzhou-24 docks at Tiangong with
  Pakistan's first astronaut, Muhammad Zeeshan Ali, the first
  foreigner aboard China's station.
- **A KPI strip** — six big numbers under the masthead (20%, -6.2%,
  1st, +26%, 30+, 9) — and **a UTC timeline** (00:18 liftoff, 03:56
  dock, 06:30 Kospi close, 10:59 Ofgem cap, afternoon tariffs, 20:15
  Cairo fire).
- **Ten more, in pictures** — Ukraine's drones set two Rosneft
  refineries ablaze; two tankers hit mines in Hormuz; the UK energy
  cap jumps 26%; a tanker fire on Cairo's ring road kills 30+; nine
  dead and 17 trapped in a Java gold mine flood; Bangladesh garment
  pay up 36%; the Solomon Islands–Australia pact; Australia CPI
  4.9%; the Dow holds 50,000 after a 1,100-point plunge; North Korea
  expels the Swiss envoy. Every panel carries its own drawn scene.
- **Where it happened** — a world map with numbered pins for the 13
  featured stories, a region legend, and 35 more stories, place
  first, one line each.
- **Date check** — Tuesday's news is kept out of Wednesday's page:
  the Huawei verdict, Putin's "inevitable" vow, Anthropic -6.5%,
  the Dow's first close above 50,000, Miss Universe and the UN
  femicide report (all Tue 24 Nov), COP31's collapse (Sun 22 Nov)
  and GTA VI's $3.79bn day one (Fri 20 Nov) are listed as left out,
  with Thanksgiving (Thu 26 Nov) and the Macy's parade (Sat 28 Nov)
  marked not yet.

## Trust labels

Each story carries one label: **CONFIRMED** (verified by a named
source), **REPORTED** (reported, details unconfirmed), or **CLAIM**
(one side's claim, not independently confirmed). The two Hormuz and
Samara refinery stories are labelled CLAIM for exactly that reason.

## Verified story list

The full list of 48 stories with their sources is in
`tools/generate.py` (the `HEROES`, `PANELS` and `MORE` tables), and
in the build report the builder filed with the entry.
