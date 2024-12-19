#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   day16.py
@Time    :   2024/12/16 13:08:45
@Author  :   Alejandro Marrero
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2023, Alejandro Marrero
@Desc    :   None
"""

import re
from collections import deque
from itertools import batched
from pathlib import Path

from tqdm import tqdm

LIMITS = (70, 70)
DIRECTIONS = {(-1, 0), (1, 0), (0, 1), (0, -1)}  # Up, Down, Right, Left


def read_maze(filename: str):
    coordinates = list(
        map(int, re.findall(r"\d+", Path(__file__).with_name(filename).read_text()))
    )
    maze = set((x, y) for x in range(LIMITS[0] + 1) for y in range(LIMITS[1] + 1))
    bytes = list((x, y) for (x, y) in batched(coordinates, n=2))

    return maze, bytes


def print_maze(maze):
    s = "=" * (LIMITS[0] + 2) + "\n"
    for y in range(LIMITS[1] + 1):
        for x in range(LIMITS[0] + 1):
            if (x, y) == (0, 0):
                s += "S"
            elif (x, y) == LIMITS:
                s += "E"
            else:
                s += "." if (x, y) in maze else "#"
        s += "\n"
    s += "=" * (LIMITS[0] + 2) + "\n"
    print(s, end="\r")


def get_neighbors(position: tuple[int, int], maze: set[tuple[int, int]]):
    px, py = position
    for x, y in DIRECTIONS:
        nx, ny = (px + x, py + y)
        if 0 <= nx <= LIMITS[0] and 0 <= ny <= LIMITS[1] and (nx, ny) in maze:
            yield (nx, ny)
        else:
            continue


def bfs(maze, start, end):
    queue = deque([start])
    distances = {}
    distances[start] = 0
    visited = set()
    while queue:
        position = queue.popleft()
        if position not in visited:
            visited.add(position)
            if position == end:
                return distances[position]
            for nbr in get_neighbors(position, maze):
                distances.setdefault(nbr, distances[position] + 1)
                queue.append(nbr)

    return -1


if __name__ == "__main__":
    maze, bytes_in = read_maze(
        filename="input.txt",
    )

    maze = maze - set(bytes_in[:1024])
    print_maze(maze)

    for b in tqdm(range(1025, len(bytes_in))):
        maze = maze - set(bytes_in[:b])
        if bfs(maze, start=(0, 0), end=LIMITS) != -1:
            continue
        else:
            print(b - 1, bytes_in[b - 1])
            break
