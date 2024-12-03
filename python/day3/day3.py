#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   day3.py
@Time    :   2024/12/03 09:35:20
@Author  :   Alejandro Marrero
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2024, Alejandro Marrero
@Desc    :   None
"""

import re
from pathlib import Path

REGEX = r"mul\(\d+,\d+\)|do\(+\)|don\'t\(+\)"


def parse_file():
    raw = Path(__file__).with_name("input.txt").read_text()
    matches = re.finditer(REGEX, raw)
    numbers = []
    compute = True
    for s in (match.group() for match in matches):
        if s == "don't()":
            compute = False
        elif s == "do()":
            compute = True
        elif compute:
            n = s[4:-1].split(",")
            numbers.append((int(n[0]), int(n[1])))
    return numbers


if __name__ == "__main__":
    print("=" * 20 + " Day 3 " + "=" * 20)

    multiplications = parse_file()
    part_one = sum(m[0] * m[1] for m in multiplications)
    print(f"Solution of part two: {part_one}")
