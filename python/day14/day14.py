#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   day14.py
@Time    :   2024/12/14 11:23:32
@Author  :   Alejandro Marrero 
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2023, Alejandro Marrero
@Desc    :   None
"""

from pathlib import Path
import re
from functools import reduce
from operator import mul


def read_robots(filename: str = "test.txt"):
    raw = Path(__file__).with_name(filename).read_text().splitlines()
    robots = []
    for line in raw:
        (x, y, vx, vy) = list(map(int, re.findall(r"-?\d+", line)))
        robots.append((x, y, vx, vy))

    return robots


def print_robots(robots, width: int = 11, height: int = 7):
    s = "=" * 40 + "\n"
    for y in range(height):
        for x in range(width):
            s += "🤖" if (x, y) in robots else "."
        s += "\n"
    s += "=" * 40 + "\n"
    print(s, end="\r")


def move_robots(
    robots: list[int],
    width: int = 11,
    height: int = 7,
    seconds: int = 100,
):
    quadrants = [0, 0, 0, 0]
    final_positions = []
    width_limit, height_limit = width // 2, height // 2

    for x, y, vx, vy in robots:
        nx = (vx * seconds + x) % width
        ny = (vy * seconds + y) % height
        final_positions.append((nx, ny))

        if nx < width_limit and ny < height_limit:
            quadrants[0] += 1
        elif nx > width_limit and ny < height_limit:
            quadrants[1] += 1
        elif nx < width_limit and ny > height_limit:
            quadrants[2] += 1
        elif nx > width_limit and ny > height_limit:
            quadrants[3] += 1

    print_robots(final_positions)
    return reduce(mul, [s if s != 0 else 1 for s in quadrants], 1)


if __name__ == "__main__":
    robots = read_robots("test.txt")
    positions = [(x, y) for (x, y, _, _) in robots]
    print_robots(positions)
    factor = move_robots(robots, width=11, height=7)
    print(factor)
