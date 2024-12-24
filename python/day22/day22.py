#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   day22.py
@Time    :   2024/12/22 08:55:59
@Author  :   Alejandro Marrero 
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2023, Alejandro Marrero
@Desc    :   None
"""


from pathlib import Path


def read_secrets(filename: str = "test.txt") -> list[int]:
    raw = Path(__file__).with_name(filename).read_text().splitlines()
    return list(map(int, raw))


def random(secret: int) -> int:
    secret = ((secret << 6) ^ secret) % 16777216
    secret = ((secret >> 5) ^ secret) % 16777216
    secret = ((secret << 11) ^ secret) % 16777216
    return secret


def sum_of_secrets(secrets: list[int]) -> int:
    total = 0
    for number in secrets:
        secret = number
        for _ in range(2000):
            secret = random(secret)
        total += secret
    return total


def calculate_bananas(secrets: list[int]) -> int:
    ranges = {}
    for number in secrets:
        secret = number
        visited = set()
        changes = []
        for _ in range(2000):
            next_secret = random(secret)
            changes.append((next_secret % 10) - (secret % 10))
            secret = next_secret
            if len(changes) == 4:
                k = tuple(changes)
                if k not in visited:
                    ranges.setdefault(k, []).append(next_secret % 10)
                    visited.add(k)

                changes.pop(0)
    bananas = max(sum(v) for v in ranges.values())
    return bananas


if __name__ == "__main__":
    secrets = read_secrets("input.txt")
    s = sum_of_secrets(secrets)
    print(s)
    bananas = calculate_bananas(secrets)
    print(bananas)
