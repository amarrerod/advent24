#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   day24.py
@Time    :   2024/12/24 08:44:18
@Author  :   Alejandro Marrero 
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2023, Alejandro Marrero
@Desc    :   None
"""


from pathlib import Path
import re
from collections import deque, OrderedDict
from operator import and_, or_, xor

OPERATIONS = {"AND": and_, "OR": or_, "XOR": xor}


def read_gates(filename: str = "test.txt"):
    inputs, connections = Path(__file__).with_name(filename).read_text().split("\n\n")
    inputs = re.findall(r"(\w+\d+):\s(\d)", inputs)
    wires = OrderedDict({k: int(v) for k, v in inputs})
    connections = re.findall(
        r"(\w*\d*)\s(AND|OR|XOR)\s(\w*\d*)\s->\s(\w*\d*)", connections
    )

    print(wires)
    print(connections)
    return wires, connections


def simulate_system(wires, connections):
    queue = deque(connections)
    print(queue)
    while queue:
        a, op, b, out = queue.popleft()
        if a in wires and b in wires:
            result = OPERATIONS[op](wires[a], wires[b])
            wires[out] = result
        else:
            queue.append((a, op, b, out))

    binary = "".join(
        str(wires[o])
        for o in sorted(
            list(filter(lambda x: x.startswith("z"), wires.keys())), reverse=True
        )
    )
    print(binary, int(binary, 2))


if __name__ == "__main__":
    wires, connections = read_gates("input.txt")
    simulate_system(wires, connections)
