#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   day23.py
@Time    :   2024/12/23 21:16:10
@Author  :   Alejandro Marrero 
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2023, Alejandro Marrero
@Desc    :   None
"""


from pathlib import Path
from itertools import combinations


def read_map(filename: str = "test.txt"):
    raw = Path(__file__).with_name(filename).read_text().splitlines()
    connections = {}

    for line in raw:
        fr, to = line.split("-")
        connections.setdefault(fr, set()).add(to)
        connections.setdefault(to, set()).add(fr)

    return connections


def is_clique(computers, connections) -> bool:
    for cpu in computers:
        for nbr in computers:
            if cpu == nbr:
                continue
            if nbr not in connections[cpu]:
                return False
    return True


def connected_computers(
    connections: dict[str, set[str]], K: int = 3, start: str = "t"
) -> int:

    computers = set(connections.keys())
    valid_cycles = list()
    for c in combinations(computers, r=3):
        if is_clique(c, connections) and any(cpu.startswith(start) for cpu in c):
            valid_cycles.append(c)

    return len(valid_cycles)


def bron_kerbosch(
    connections, cclique: set, potential: set, processed: set, cliques: list
) -> str:
    if not potential and not processed:
        cliques.append(cclique)
        return

    for vertex in list(potential):
        new_cclique = {vertex} | cclique
        new_potential = potential & connections[vertex]
        new_processed = processed & connections[vertex]
        bron_kerbosch(connections, new_cclique, new_potential, new_processed, cliques)
        potential.remove(vertex)
        processed.add(vertex)


def find_max_clique(connections):
    cliques = []
    bron_kerbosch(connections, set(), set(connections.keys()), set(), cliques)
    cliques = sorted(cliques, key=len, reverse=True)
    print(cliques)
    return ",".join(c for c in sorted(cliques[0]))


if __name__ == "__main__":
    connections = read_map("input.txt")
    print(connections)
    t = find_max_clique(connections)
    print(t)
