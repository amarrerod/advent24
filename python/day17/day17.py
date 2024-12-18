#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   day17.py
@Time    :   2024/12/17 15:23:13
@Author  :   Alejandro Marrero
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2023, Alejandro Marrero
@Desc    :   None
"""

import re
from pathlib import Path

from instructions import instructions


def read_program(filename: str = "test.txt"):
    raw = Path(__file__).with_name(filename).read_text()
    registers_and_program = list(map(int, re.findall(r"\d+", raw)))

    return registers_and_program[:3], registers_and_program[3:]


def get_operand(operand: int, registers: list[int]):
    if 0 <= operand <= 3 or operand == 7:
        return operand
    else:
        return registers[operand - 4]


def run(program: list[int], registers: list[int]):
    ptr = 0
    while ptr < len(program):
        ins, op = program[ptr : ptr + 2]
        out = instructions[ins](op, registers)
        if out is not None:
            ptr = op - 2

        ptr += 2


if __name__ == "__main__":
    registers, program = read_program("input.txt")
    print(registers, program)
    run(program, registers)
