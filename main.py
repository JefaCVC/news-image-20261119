#!/usr/bin/env python3
"""news-image-20261119 entry (Python 3.13, standard library only).

The entry image is entry.png beside this file: a 1024x1024 newspaper
front page for Thursday 19 November 2026 with 36 stories, 15 pictured
cells, a numbers strip, a UTC timeline, a dotted world map and a DATE
CHECK box. This program copies it to /output/entry.png, which is what
the gate reads and the judge sees.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(SRC, os.path.join(out_dir, "entry.png"))


if __name__ == "__main__":
    main()
