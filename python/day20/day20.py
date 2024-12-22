#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   day20.py
@Time    :   2024/12/20 17:22:53
@Author  :   Alejandro Marrero 
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2023, Alejandro Marrero
@Desc    :   None
"""

from pathlib import Path
import numpy as np
from tqdm import tqdm


def read_racetrack(filename: str = "test.txt"):
    raw = Path(__file__).with_name(filename).read_text().splitlines()
    track = []
    start, end = None, None
    for i, row in enumerate(raw):
        for j, p in enumerate(row):
            if p == "S":
                start = (i, j)
            elif p == "E":
                end = (i, j)
            elif p == ".":
                track.append((i, j))
    return track, start, end


def get_path(
    track: list[tuple[int, int]], start: tuple[int, int], end: tuple[int, int]
):
    visited = set()
    path = []
    queue = [start]
    while queue:
        position = queue.pop()
        visited.add(position)
        path.append(np.array(position))

        if position == end:
            break

        for x, y in (0, -1), (0, 1), (-1, 0), (1, 0):
            nbr = (x + position[0], y + position[1])
            if nbr not in visited and nbr in track:
                queue.append(nbr)
    return path


def count_cheats(path: list, max_cheats: int = 2, min_improve: int = 0):
    counter = 1
    for i in tqdm(range(len(path) - 1)):
        for j in range(i + 1, len(path)):
            a, b = path[i], path[j]
            distance = np.abs(a - b).sum()
            if distance > max_cheats:
                continue
            time_saved = j - i - distance
            if time_saved < min_improve:
                continue
            counter += 1
    return counter


if __name__ == "__main__":
    track, start, end = read_racetrack("test.txt")
    path = get_path(track, start, end)

    r = count_cheats(path, max_cheats=1, min_improve=50)
    print(r)
