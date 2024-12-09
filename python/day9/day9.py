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

import re
from collections import deque
from pathlib import Path

REGEX = r"(\d)(\d)"


def parse_file(filename: str = "test.txt"):
    disk_map = Path(__file__).with_name(filename).read_text()
    id = 0
    blocks = []
    is_file = True
    for v in disk_map:
        v = int(v)
        if is_file:
            blocks += [id] * v
            id += 1
        else:
            blocks += [None] * v

        is_file = not is_file
    print(blocks)
    return blocks


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


if __name__ == "__main__":
    blocks = parse_file("input.txt")

    checksum = rearrange(blocks)
    print(f"Checksum is: {checksum}")
