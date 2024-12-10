#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   day8.py
@Time    :   2024/12/10 14:43:56
@Author  :   Alejandro Marrero
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2024, Alejandro Marrero
@Desc    :
    The signal only applies its nefarious effect at specific antinodes based on the resonant frequencies of the antennas.
    In particular, an antinode occurs at any point that is perfectly in line with two antennas of the same frequency
    - but only when one of the antennas is twice as far away as the other.
    This means that for any pair of antennas with the same frequency,
    there are two antinodes, one on either side of them.
"""

import itertools
from pathlib import Path

import numpy as np
from tqdm import tqdm


def read_map(filename: str = "test.txt"):
    raw = Path(__file__).with_name(filename).read_text().splitlines()
    antennas = {}
    for i, line in enumerate(raw):
        for j, c in enumerate(line):
            if c != ".":
                antennas.setdefault(c, []).append([i, j])

    max_x = len(raw)
    max_y = len(raw[0])
    return antennas, max_x, max_y


def is_in_line(a, b, c):
    (ax, ay) = a
    (bx, by) = b
    (cx, cy) = c
    return not (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))


def euclidean(a, b) -> float:
    return (((a[0] - b[0]) ** 2) + ((a[1] - b[1]) ** 2)) ** 0.5  # fast sqrt


def plant_antinodes(
    antennas: dict[str, list[tuple[int]]],
    max_x: int,
    max_y: int,
    part_two: bool = False,
):
    antinodes = set()
    for _, locations in tqdm(antennas.items()):
        for l0, l1 in itertools.combinations(locations, r=2):
            # Now sample all points
            for x, y in itertools.product(range(max_x), range(max_y)):
                p = [x, y]
                if part_two and is_in_line(l0, l1, p):
                    antinodes.add(tuple(p))
                elif not part_two:
                    d0 = euclidean(l0, p)
                    d1 = euclidean(l1, p)

                    if min(d0, d1) * 2 == max([d0, d1]) and is_in_line(l0, l1, p):
                        # One is twice as far
                        antinodes.add(tuple(p))

    return antinodes


if __name__ == "__main__":
    print("=" * 20 + " Day 8 " + "=" * 20)

    antennas, max_x, max_y = read_map("input.txt")
    antinodes = plant_antinodes(antennas, max_x, max_y)
    print(len(antinodes))
    antinodes = plant_antinodes(antennas, max_x, max_y, part_two=True)
    print(len(antinodes))
