#!/usr/bin/env python3
"""Sum up 25 November's world news in one image.

A make.fun program/v1 entry for the competition news-image-20261125.

The entry image lives next to this program at assets/entry.png: a
newspaper front page for Wednesday 25 November 2026, drawn at build
time by tools/generate.py from the day's reported news. It carries
48 stories across 8 regions and 17 fields -- three leads with
richly drawn illustrations (US tariffs on 14 economies, the Kospi
-6.2% chip rout, Pakistan's first astronaut docking at Tiangong),
ten more stories each with its own drawn scene, a world map with
numbered pins, 35 more stories, a KPI strip, a UTC timeline, and a
date check that keeps Tuesday's news out of Wednesday's page.

This program only copies that PNG to the output path, which the
competition rules explicitly allow: "the simplest entry is a
repository holding the image and a one-line program that copies it
there".

No network, no randomness, no wall-clock time, no third-party
packages -- only the Python standard library -- so the two grading
runs produce byte-identical output.

Run:  python3 main.py
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "assets", "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dest)
    return dest


if __name__ == "__main__":
    main()
