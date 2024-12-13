#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   day13.py
@Time    :   2024/12/13 13:57:32
@Author  :   Alejandro Marrero
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2024, Alejandro Marrero
@Desc    :   None
"""

import re
from pathlib import Path

import numpy as np

REGEX = r"Button\sA:\sX\+(\d+),\sY\+(\d+)\nButton\sB:\sX\+(\d+),\sY\+(\d+)\nPrize:\sX=(\d+),\sY=(\d+)"


def load_configurations(filename: str = "test.txt") -> list[tuple[int, ...]]:
    raw = Path(__file__).with_name(filename).read_text()
    configurations = [tuple(int(x) for x in match) for match in re.findall(REGEX, raw)]

    return configurations


def is_possible_to_win(configuration) -> list[int]:
    ax, ay, bx, by, x, y = configuration
    det = ax * by - bx * ay
    result = [0, 0]
    for i, (x, y) in enumerate(((x, y), (x + 10000000000000, y + 10000000000000))):
        na, ra = divmod(by * x - bx * y, det)
        nb, rb = divmod(ax * y - ay * x, det)
        r = 3 * na + nb if na >= ra == 0 == rb <= nb else 0
        result[i] = r

    return result


if __name__ == "__main__":
    configurations = load_configurations("input.txt")
    solutions = np.array([is_possible_to_win(config) for config in configurations]).sum(
        axis=0
    )
    print(f"The solutions are: {solutions}")
