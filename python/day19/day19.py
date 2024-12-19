#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   day19.py
@Time    :   2024/12/19 14:20:53
@Author  :   Alejandro Marrero
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2024, Alejandro Marrero
@Desc    :   None
"""

from pathlib import Path


def read_towels(filename: str = "test.txt"):
    raw = Path(__file__).with_name(filename).read_text().split("\n\n")
    towels = tuple(raw[0].split(", "))
    patterns = raw[1].split()
    return (towels, patterns)


_memoization = {"": 1}


def count_ways(pattern: str, towels: tuple[str]) -> int:
    if pattern in _memoization:
        return _memoization[pattern]
    else:
        counter = sum(
            count_ways(pattern[len(towel) :], towels)
            for towel in towels
            if pattern.startswith(towel)
        )
        _memoization[pattern] = counter
        return counter


if __name__ == "__main__":
    towels, patterns = read_towels("input.txt")
    print(towels)
    print(patterns)
    ways = [count_ways(p, towels) for p in patterns]
    print(f"Part One: {len(list(filter(None, ways)))}")
    print(f"Part Two: {sum(ways)}")
