#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   day10.py
@Time    :   2024/12/10 12:37:35
@Author  :   Alejandro Marrero
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2024, Alejandro Marrero
@Desc    :   None
"""

from pathlib import Path


def read_map(filename: str = "test.txt"):
    raw = Path(__file__).with_name(filename).read_text().splitlines()
    coords = [list(map(int, r)) for r in raw]
    return coords


def get_neighbors(i: int, j: int, rows: int, cols: int):
    # At least one neighbor must be 1
    right = (i, j + 1) if j + 1 < cols else None
    left = (i, j - 1) if j - 1 >= 0 else None
    up = (i - 1, j) if i - 1 >= 0 else None
    down = (i + 1, j) if i + 1 < rows else None
    return filter(None, (right, left, up, down))


def get_trailheads(map: list[list[int]]):
    rows, cols = len(map), len(map[0])
    for i in range(rows):
        for j in range(cols):
            if map[i][j] == 0:
                valid_neighbors = tuple(
                    filter(
                        lambda t: map[t[0]][t[1]] == 1,
                        get_neighbors(i, j, rows, cols),
                    )
                )

                if valid_neighbors:
                    yield (i, j)


def calculate_good_hikings(head, map):
    rows, cols = len(map), len(map[0])

    reachable = []
    stack = [head]
    while stack:
        node = stack.pop()
        (cx, cy) = node
        if map[cx][cy] == 9:
            reachable.append(node)

        for neighbor in reversed(tuple(get_neighbors(cx, cy, rows, cols))):
            (nx, ny) = neighbor
            if map[nx][ny] - map[cx][cy] == 1:
                stack.append(neighbor)

    return reachable


if __name__ == "__main__":
    print("=" * 20 + " Day 10 " + "=" * 20)

    map = read_map("test.txt")
    trail_heads = get_trailheads(map)
    total_part_one = 0
    total_part_two = 0
    for trail_head in get_trailheads(map):
        reachable = calculate_good_hikings(trail_head, map)
        total_part_one += len(set(reachable))
        total_part_two += len(reachable)
    print(total_part_one, total_part_two)
