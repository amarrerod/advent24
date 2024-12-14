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
from tqdm import tqdm
from collections import Counter
from functools import reduce
from operator import mul


def read_robots(filename: str = "test.txt"):
    raw = Path(__file__).with_name(filename).read_text().splitlines()
    positions: list[tuple[int]] = []
    speeds: list[tuple[int]] = []
    for line in raw:
        (x, y, vx, vy) = list(map(int, re.findall(r"-?\d+", line)))
        positions.append((x, y))
        speeds.append((vx, vy))

    return positions, speeds


def print_robots(robots, x_limit: int = 11, y_limit: int = 7):
    s = ""
    for y in range(y_limit):
        for x in range(x_limit):
            s += "🤖" if (x, y) in robots else "."
        s += "\n"

    print(s, end="\r")


def count_by_quadrant(robots, quadrant):
    x0, x1, y0, y1 = quadrant
    s = "\n"
    counter = 0
    for x in range(x0, x1 + 1):
        for y in range(y0, y1 + 1):
            if (y, x) in robots:
                s += str(robots[(y, x)])
                counter += robots[(y, x)]
            else:
                s += "."
        s += "\n"

    print(s, end="\r")
    return counter


def move_robots(
    robots: list[int],
    speeds: list[int],
    x_limit: int = 11,
    y_limit: int = 7,
    seconds: int = 100,
):
    for _ in tqdm(range(seconds)):
        for i in range(len(robots)):
            (x, y), (vx, vy) = robots[i], speeds[i]
            nx = (x + vx) % x_limit
            ny = (y + vy) % y_limit
            robots[i] = (nx, ny)

    quad_x_lim, quad_y_lim = (x_limit // 2) - 1, (y_limit // 2) - 1
    first = (0, quad_y_lim, 0, quad_x_lim)
    second = (0, quad_y_lim, quad_x_lim + 2, x_limit - 1)
    third = (quad_y_lim + 2, y_limit - 1, 0, quad_x_lim)
    fourth = (quad_y_lim + 2, y_limit - 1, quad_x_lim + 2, x_limit - 1)

    robot_counter = Counter(robots)
    quadrants = [
        count_by_quadrant(robot_counter, q) for q in (first, second, third, fourth)
    ]
    return reduce(mul, [s if s != 0 else 1 for s in quadrants], 1)


if __name__ == "__main__":
    robots, speeds = read_robots("input.txt")
    print_robots(robots)
    factor = move_robots(robots, speeds, x_limit=101, y_limit=103)
    print(factor)
