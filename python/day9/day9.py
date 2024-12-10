#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   day9.py
@Time    :   2024/12/09 13:32:37
@Author  :   Alejandro Marrero
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2024, Alejandro Marrero
@Desc    :   None
"""

import numpy as np
from tqdm import tqdm


def make_filesystem(disk_map):
    id = 0
    blocks = []
    is_file = True
    sizes = [0] * len(disk_map)
    locations = [0] * len(disk_map)

    for v in disk_map:
        v = int(v)
        if is_file:
            sizes[id] = v
            locations[id] = len(blocks)
            blocks += [id] * v
            id += 1

        else:
            blocks += [None] * v

        is_file = not is_file

    return np.array(blocks), sizes, locations


def rearrange(blocks) -> int:
    free_space = 0
    while blocks[free_space] is not None:
        free_space += 1

    last = len(blocks) - 1
    while blocks[last] is None:
        last -= 1

    while last > free_space:
        blocks[free_space], blocks[last] = blocks[last], None
        while blocks[last] is None:
            last -= 1
        while blocks[free_space] is not None:
            free_space += 1

    checksum = sum([i * x for i, x in enumerate(blocks) if x is not None])
    return checksum


def rearrange_entire_file(blocks, sizes: list[int], locations: list[int]) -> int:
    file_to_move = 0
    while sizes[file_to_move] > 0:
        file_to_move += 1
    file_to_move -= 1
    for to_move in tqdm(range(file_to_move, -1, -1)):
        # Find first free space that works
        free_space = 0
        first_free = 0
        while first_free < locations[to_move] and free_space < sizes[to_move]:
            first_free = first_free + free_space
            free_space = 0
            while blocks[first_free] is not None:
                first_free += 1
            while (
                first_free + free_space < len(blocks)
                and blocks[first_free + free_space] is None
            ):
                free_space += 1

        if first_free >= locations[to_move]:
            continue

        # Move file
        blocks[first_free : first_free + sizes[to_move]] = [to_move]
        blocks[locations[to_move] : locations[to_move] + sizes[to_move]] = [None]

    checksum = sum([i * x for i, x in enumerate(blocks) if x is not None])
    return checksum


if __name__ == "__main__":
    print("=" * 20 + " Day 9 " + "=" * 20)

    with open("input.txt") as f:
        disk_map = f.read().strip()

    blocks, sizes, locations = make_filesystem(disk_map)

    # checksum = rearrange(blocks)
    # print(f"Checksum is: {checksum}")
    checksum2 = rearrange_entire_file(blocks, sizes, locations)
    print(f"Checksum if fitting entire file is: {checksum2}")
