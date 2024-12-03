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

REGEX = r"mul\((\d+),(\d+)\)|(do\(+\))|(don\'t\(+\))"


def parse_file(filename: str = ""):
    raw = Path(__file__).with_name(filename).read_text()
    matches = re.finditer(REGEX, raw)
    compute = True
    for match in matches:
        content = list(filter(lambda x: x, match.groups()))
        if len(content) == 1:
            # The only options are do or don't
            compute = False if content[0] == "don't()" else True
        elif compute:
            # Here we have two numbers to multiply
            yield int(content[0]) * int(content[1])


if __name__ == "__main__":
    print("=" * 20 + " Day 3 " + "=" * 20)
    part_one = sum(parse_file(filename="input.txt"))
    print(f"Solution of part two: {part_one}")
