#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   day4.py
@Time    :   2024/12/04 10:42:10
@Author  :   Alejandro Marrero
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2024, Alejandro Marrero
@Desc    :   None
"""

import itertools as it
import re

import numpy as np


def parse_file(filename: str = "test.txt") -> list[list[str]]:
    return np.genfromtxt(filename, dtype=str, delimiter=1)


def count_xmas(words):
    expected = "XMAS"

    n = len(words)
    m = len(words[0])
    for i in range(n):
        for j in range(m):
            if words[i][j] == "X":
                # We can have something here
                for ni, nj in it.product([-1, 0, 1], [-1, 0, 1]):
                    if ni == nj == 0:
                        continue  # Same character
                    if all(
                        0 <= i + k * ni < n
                        and 0 <= j + k * nj < m
                        and words[i + k * ni][j + k * nj] == expected[k]
                        for k in range(4)
                    ):
                        yield 1


def count_mas(words):
    n = len(words)
    m = len(words[0])
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if words[i][j] == "A":
                left = words[i - 1][j - 1] + words[i][j] + words[i + 1][j + 1]
                right = words[i - 1][j + 1] + words[i][j] + words[i + 1][j - 1]
                if all(x == "MAS" or x == "SAM" for x in (left, right)):
                    yield 1


if __name__ == "__main__":
    print("=" * 20 + " Day 4 " + "=" * 20)

    raw = parse_file("input.txt")

    print(f"N of XMAS: {sum(count_xmas(raw))}")
    part_two = sum(count_mas(raw))
    print(f"Crossed MAS are: {part_two}")
