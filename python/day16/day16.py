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

from pathlib import Path
from heapq import heappop, heappush
from collections import defaultdict
from typing import Optional


def read_maze(filename: str = "test.txt"):
    raw = Path(__file__).with_name(filename).read_text().splitlines()
    maze = {
        i + j * 1j: c
        for i, row in enumerate(raw)
        for j, c in enumerate(row)
        if c != "#"
    }
    (start,) = (p for p in maze if maze[p] == "S")
    (end,) = (p for p in maze if maze[p] == "E")

    return raw, (
        maze,
        start,
        end,
    )


def print_maze(maze, path: Optional[list[complex]] = None):
    s = "=" * len(maze[0]) + "\n"
    for i, rows in enumerate(maze):
        for j, p in enumerate(rows):
            if p != "E" and path is not None and (i + j * 1j) in path:
                s += "🦌"
            else:
                s += p
        s += "\n"
    s += "=" * len(maze[0]) + "\n"
    print(s, end="\r")


def dijsktra(maze, start, end):
    distances = defaultdict(lambda: 1e9)
    best_score, best_path = 1e9, []
    seen = []
    queue = [(0, t := 0, start, 1j, [start])]
    # score, position, direction, visited tiles
    # when inserting to the priority queue, add a "tie-breaker" to your tuple.
    # So (score, position) becomes (score, t, position), where t is a unique value.
    # This can be a random number, or an ever incrementing value.
    while queue:
        score, _, position, direction, path = heappop(queue)
        if score > distances[position, direction]:
            continue
        else:
            distances[position, direction] = score

        if position == end and score <= best_score:
            seen += path
            best_score = score
            best_path = path

        for rotation, pts in (1, 1), (1j, 1001), (-1j, 1001):
            new = position + direction * rotation
            if new in maze:
                heappush(
                    queue,
                    (
                        score + pts,
                        t := t + 1,
                        new,
                        direction * rotation,
                        path + [new],
                    ),
                )

    return (best_score, len(set(seen)), best_path)


if __name__ == "__main__":
    raw, (maze, start, end) = read_maze("input.txt")
    print_maze(raw)
    score, tiles, best_path = dijsktra(maze, start, end)
    print_maze(raw, best_path)
    print(score, tiles)
