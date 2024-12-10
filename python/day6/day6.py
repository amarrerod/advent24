#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   day6.py
@Time    :   2024/12/09 09:59:49
@Author  :   Alejandro Marrero
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2024, Alejandro Marrero
@Desc    :   None
"""

from collections import deque
from copy import deepcopy
from pathlib import Path


def parse_file(filename: str = "test.txt"):
    raw = Path(__file__).with_name(filename).read_text().splitlines()
    guard = None
    obstacles: set[tuple[int, int]] = set()

    for i in range(len(raw)):
        row = list(raw[i])
        for j in range(len(row)):
            if row[j] == "^":
                guard = (i, j)
                continue
            elif row[j] == "#":
                obstacles.add((i, j))
    x_max = max(len(r) for r in raw)
    x_limit = (0, x_max)
    y_limit = (0, len(raw))
    return guard, obstacles, x_limit, y_limit


def compute_guard_path(
    guard: tuple[int, int],
    obstacles: set[tuple[int, int]],
    x_limit: tuple[int, int],
    y_limit: tuple[int, int],
) -> set[tuple[int, int]]:
    path: set[tuple[int, int]] = set()
    path.add(guard)

    current_position = guard
    x_min, x_max = x_limit
    y_min, y_max = y_limit
    orientations = deque([(-1, 0), (0, 1), (1, 0), (0, -1)])
    increase = orientations.popleft()

    while x_min <= current_position[0] < x_max and y_min <= current_position[1] < y_max:
        next_position = tuple(map(sum, zip(current_position, increase)))

        if next_position not in obstacles:
            current_position = next_position
            path.add(current_position)
        else:
            # Turn right
            orientations.append(increase)
            increase = orientations.popleft()
    return path


def obstacle_guard(
    guard: tuple[int, int],
    obstacles: set[tuple[int, int]],
    x_limit: tuple[int, int],
    y_limit: tuple[int, int],
):
    positions = set()
    positions.add(guard)

    x_min, x_max = x_limit
    y_min, y_max = y_limit

    orientations = deque([(-1, 0), (0, 1), (1, 0), (0, -1)])
    increase = orientations.popleft()
    current_position = guard

    while x_min <= current_position[0] < x_max and y_min <= current_position[1] < y_max:
        next_position = tuple(map(sum, zip(current_position, increase)))

        if next_position in positions:
            return True

        elif next_position not in obstacles:
            current_position = next_position

        else:
            # Turn right
            orientations.append(increase)
            increase = orientations.popleft()

            positions.add(current_position)

    return False


def how_many_ways(
    guard: tuple[int, int],
    route: set[tuple[int, int]],
    obstacles: set[tuple[int, int]],
    x_limit: tuple[int, int],
    y_limit: tuple[int, int],
):
    xr_min = min(p[0] for p in route)
    xr_max = max(p[0] for p in route)
    yr_min = min(p[1] for p in route)
    yr_max = max(p[1] for p in route)

    ways: list[bool] = []
    for i in range(xr_min, xr_max):
        for j in range(yr_min, yr_max):
            if (i, j) == guard:
                continue

            new_obstacles = deepcopy(obstacles)
            new_obstacles.add((i, j))

            ways.append(obstacle_guard(guard, new_obstacles, x_limit, y_limit))

    return len(list(filter(None, ways)))


if __name__ == "__main__":
    print("=" * 20 + " Day 6 " + "=" * 20)

    guard, obstacles, x_limit, y_limit = parse_file("input.txt")

    print(f"Boundaries: {x_limit}, {y_limit}")
    route = compute_guard_path(guard, obstacles, x_limit, y_limit)
    print(f"Distinct positions: {len(route)- 1}")
    n_ways = how_many_ways(guard, route, obstacles, x_limit, y_limit)
    print(f"How many ways: {n_ways}")
