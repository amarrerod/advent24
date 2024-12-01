#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   day1.py
@Time    :   2024/12/01 12:35:30
@Author  :   Alejandro Marrero 
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2023, Alejandro Marrero
@Desc    :   None
"""

from pathlib import Path
from collections import Counter


def parse_file():
    raw = Path(__file__).with_name("input.txt").read_text().splitlines()
    sequences = ([], [])
    for line in raw:
        a, b = line.split()
        sequences[0].append(int(a))
        sequences[1].append(int(b))
    return sequences


def part_one(locations: tuple[list[int]]) -> int:
    l_0 = sorted(locations[0])
    l_1 = sorted(locations[1])
    total_distance = sum(abs(l_0[i] - l_1[i]) for i in range(len(l_0)))
    return total_distance


def part_two(locations: tuple[list[int]]) -> int:
    counter = Counter(locations[1])
    similarity_score = sum(counter[i] * i for i in locations[0])
    return similarity_score


if __name__ == "__main__":
    locations = parse_file()
    dist = part_one(locations)
    print(dist)
    similarity = part_two(locations)
    print(similarity)
