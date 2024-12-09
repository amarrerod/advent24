#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   day7.py
@Time    :   2024/12/09 11:24:25
@Author  :   Alejandro Marrero
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2024, Alejandro Marrero
@Desc    :   None
"""

import itertools
from pathlib import Path


def parse_file(filename: str = "test.txt"):
    raw = Path(__file__).with_name(filename).read_text().splitlines()
    equations = []
    for line in raw:
        test, numbers = line.split(":")
        numbers = tuple(map(int, numbers.split(" ")[1:]))
        equations.append((int(test), numbers))

    return equations


def compute_reduce(operators, numbers) -> int:
    value = numbers[0]
    for i in range(1, len(numbers)):
        match operators[i - 1]:
            case "+":
                value += numbers[i]
            case "*":
                value *= numbers[i]
            case "|":
                value = int(f"{value}{numbers[i]}")
    return value


def valid_equations(equation):
    test, numbers = equation

    operations = "+*|"
    for ops in itertools.product(operations, repeat=len(numbers) - 1):
        if compute_reduce(ops, numbers) == test:
            return test

    return 0


if __name__ == "__main__":
    equations = parse_file("input.txt")
    result = sum(valid_equations(eq) for eq in equations)
    print(result)
