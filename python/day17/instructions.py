#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   instructions.py
@Time    :   2024/12/17 15:49:42
@Author  :   Alejandro Marrero
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2023, Alejandro Marrero
@Desc    :   None
"""


def get_combo(operand: int, registers: list[int]):
    if 0 <= operand <= 3 or operand == 7:
        return operand
    else:
        return registers[operand - 4]


def adv(n: int, registers: list[int]):
    combo = get_combo(n, registers)
    registers[0] //= 2**combo


def bxl(n: int, registers: list[int]):
    registers[1] = registers[1] ^ n


def bst(n: int, registers: list[int]):
    combo = get_combo(n, registers)
    registers[1] = combo % 8


def jnz(n: int, registers: list[int]):
    if registers[0] != 0:
        return n


def bxc(_: int, registers: list[int]):
    registers[1] = registers[1] ^ registers[2]


def out(n: int, registers: list[int]):
    combo = get_combo(n, registers)
    c = combo % 8
    print(c, end=",")


def bdv(n: int, registers: list[int]):
    combo = get_combo(n, registers)
    registers[1] = registers[0] // 2**combo


def cdv(n: int, registers: list[int]):
    combo = get_combo(n, registers)
    registers[2] = registers[0] // 2**combo


instructions = {0: adv, 1: bxl, 2: bst, 3: jnz, 4: bxc, 5: out, 6: bdv, 7: cdv}
