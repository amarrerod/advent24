#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   day12.py
@Time    :   2024/12/12 10:36:01
@Author  :   Alejandro Marrero
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2024, Alejandro Marrero
@Desc    :   None
"""

from functools import lru_cache
from pathlib import Path


def read_map(
    filename: str = "test.txt",
) -> tuple[list[list[str]], set[tuple[int, int]]]:
    raw = Path(__file__).with_name(filename).read_text().splitlines()
    farm = [list(r) for r in raw]
    candidates = set((i, j) for i in range(len(farm)) for j in range(len(farm[i])))

    return farm, candidates


def get_neighbors(i: int, j: int, rows: int, cols: int, filtered: bool = True):
    for x, y in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        s = (i + x, j + y)
        if filtered:
            if 0 <= s[0] < rows and 0 <= s[1] < cols:
                yield s
            else:
                continue
        else:
            yield s


def flood_fill(plant: str, start: tuple[int, int], farm: list[list[str]]):
    rows, cols = len(farm), len(farm[0])
    region = {start}
    stack = [start]
    while stack:
        (i, j) = stack.pop()
        for ni, nj in get_neighbors(i, j, rows, cols):
            if (ni, nj) not in region and farm[ni][nj] == plant:
                region.add((ni, nj))
                stack.append((ni, nj))
    return region


def get_perimeter(region: set[tuple[int, int]], rows: int, cols: int) -> int:
    result = 0
    for i, j in region:
        perim = 4 - len(set(get_neighbors(i, j, rows, cols)) & region)
        result += perim
    return result


def get_sides(region, rows: int, cols: int) -> int:
    edges = set()
    for point in region:
        (i, j) = point
        for nbr in get_neighbors(i, j, rows, cols, filtered=False):
            if nbr not in region:
                edges.add((point, nbr))
    sides = 0
    for (x1, y1), (x2, y2) in edges:
        if y1 == y2:
            if ((x1, y1 - 1), (x2, y2 - 1)) not in edges:
                sides += 1
        else:
            if ((x1 - 1, y1), (x2 - 1, y2)) not in edges:
                sides += 1

    return sides


if __name__ == "__main__":
    farm, candidates = read_map("input.txt")
    rows, cols = len(farm), len(farm[0])
    part_one = 0
    part_two = 0
    while candidates:
        start = candidates.pop()
        plant = farm[start[0]][start[1]]
        region = flood_fill(plant, start, farm)
        candidates -= region

        area = len(region)
        perimeter = get_perimeter(region, rows, cols)
        part_one += area * perimeter
        sides = get_sides(region, rows, cols)
        part_two += area * sides
        print(f"Plant: {plant}, Area: {area}, Perimeter: {perimeter}, S: {sides}")
    print(part_one, part_two)
