#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   day2.py
@Time    :   2024/12/02 10:08:20
@Author  :   Alejandro Marrero
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2024, Alejandro Marrero
@Desc    :   None
"""

from itertools import pairwise
from pathlib import Path


def parse_file():
    raw = Path(__file__).with_name("input.txt").read_text().splitlines()
    reports = [list(map(int, line.split())) for line in raw]
    return reports


def is_report_safe(report: list[int]) -> bool:
    differences = list(b - a for a, b in pairwise(report))
    if all(1 <= d <= 3 for d in differences) or all(-3 <= d <= -1 for d in differences):
        return True
    return False


def is_report_safe2(report: list[int]) -> bool:
    if is_report_safe(report) or any(
        is_report_safe(report[:i] + report[i + 1 :]) for i in range(len(report))
    ):
        return True
    else:
        return False


if __name__ == "__main__":
    print("=" * 20 + " Day 2 " + "=" * 20)
    reports = parse_file()
    print(f"Safe reports: {len(list(filter(is_report_safe, reports)))}")
    print(f"Safe reports 2: {len(list(filter(is_report_safe2, reports)))}")
