#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   day11.py
@Time    :   2024/12/11 08:31:29
@Author  :   Alejandro Marrero
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2024, Alejandro Marrero
@Desc    :   None
"""

from collections import Counter, defaultdict
from functools import lru_cache
from pathlib import Path

from tqdm import tqdm


def read_stones(filename: str = "test.txt") -> list[int]:
    raw = Path(__file__).with_name(filename).read_text().rstrip().split(" ")
    return list(map(int, raw))


@lru_cache
def blink(stone: int):
    if stone == 0:
        return [1]
    s = str(stone)
    if len(s) % 2 == 0:
        left = int(s[: len(s) // 2])
        right = int(s[(len(s) // 2) :])
        return [left, right]
    else:
        return [stone * 2024]


if __name__ == "__main__":
    stones = Counter(read_stones("input.txt"))

    print(stones)
    for _ in tqdm(range(75)):
        new_stones = defaultdict(int)
        for stone, count in stones.items():
            for child in blink(stone):
                new_stones[child] += count

        stones = new_stones
    print(sum(stones.values()))
