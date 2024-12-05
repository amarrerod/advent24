#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   day5.py
@Time    :   2024/12/05 10:45:48
@Author  :   Alejandro Marrero 
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2023, Alejandro Marrero
@Desc    :   None
"""
from pathlib import Path


def parse_file(filename: str = "test.txt"):
    raw = Path(__file__).with_name(filename).read_text().splitlines()
    rules = {}
    updates = []
    update = False
    for line in raw:
        if line == "":
            update = True
            continue
        if update:
            updates.append(list(map(int, line.split(","))))
        else:
            x, y = line.split("|")
            rules.setdefault(int(y), []).append(int(x))
            rules.setdefault(int(x), [])
    return rules, updates


def check_update_is_correct(
    update: list[int], rules: dict[int, list[int]]
) -> list[bool]:
    correct = []
    for i in range(len(update) - 1):
        r = all(update[i] in rules[y] for y in update[i + 1 :])
        correct.append(r)

    return correct


def compute_middle_page(
    rules: dict[int, list[int]], updates: list[list[int]], part_one: bool = True
):
    for update in updates:
        correctness = check_update_is_correct(update, rules)
        if part_one:
            if all(correctness):
                m = update[len(update) // 2]
                yield m
        else:
            if not all(correctness):
                while not all(correctness):
                    for i in range(len(correctness)):
                        if not correctness[i]:
                            update[i], update[i + 1] = update[i + 1], update[i]

                        correctness = check_update_is_correct(update, rules)

                yield update[len(update) // 2]


if __name__ == "__main__":
    rules, updates = parse_file("input.txt")

    middle_pages = sum(compute_middle_page(rules, updates))
    print(f"Middle pages: {middle_pages}")
    middle_pages = sum(compute_middle_page(rules, updates, part_one=False))
    print(f"Middle pages part two: {middle_pages}")
