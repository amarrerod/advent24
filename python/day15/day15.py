#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   day15.py
@Time    :   2024/12/15 10:46:08
@Author  :   Alejandro Marrero 
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2023, Alejandro Marrero
@Desc    :   None
"""

from pathlib import Path


def read_input(filename: str = "test.txt"):
    house, moves = Path(__file__).with_name(filename).read_text().split("\n\n")
    moves = moves.replace("\n", "")

    robot = None
    walls = set()
    boxes = set()
    house = house.splitlines()
    rows, cols = len(house), len(house[0])
    for i, row in enumerate(house):
        for j, p in enumerate(row.rstrip()):
            if p == "#":
                walls.add((i, j))
            elif p == "@":
                robot = (i, j)
            elif p == "O":
                boxes.add((i, j))

    return robot, walls, boxes, moves, (rows, cols)


def print_house(walls, robot, boxes, rows, cols):
    s = "=" * 40 + "\n"
    for i in range(rows):
        for j in range(cols):
            if (i, j) in walls:
                s += "#"
            elif (i, j) == robot:
                s += "@"
            elif (i, j) in boxes:
                s += "O"
            else:
                s += "."
        s += "\n"
    s += "=" * 40 + "\n"
    print(s, end="\r")


def generate_moves(moves):
    for move in moves:
        print(f"Move: {move}")
        if move == "<":
            yield (0, -1)
        elif move == "^":
            yield (-1, 0)
        elif move == ">":
            yield (0, 1)
        elif move == "v":
            yield (1, 0)
        else:
            continue


def goods_position(robot, walls, boxes, moves, rows, cols):
    for x, y in generate_moves(moves):
        robot_np = (robot[0] + x, robot[1] + y)

        if robot_np not in walls:
            if robot_np in boxes:
                # Recoger las cajas vecinas
                nbr = robot_np
                nb_boxes = []
                while nbr in boxes:
                    nb_boxes.append(nbr)
                    nbr = (nbr[0] + x, nbr[1] + y)
                # Podemos moverlas sin tocar pared?
                nb_boxes_moved = [(n[0] + x, n[1] + y) for n in nb_boxes]
                if not any(n in walls for n in nb_boxes_moved):
                    boxes -= set(nb_boxes)
                    boxes |= set(nb_boxes_moved)
                    robot = robot_np

            else:
                robot = robot_np

        print_house(walls, robot, boxes, rows, cols)
    gps = 0
    for bx, by in boxes:
        gps += 100 * bx + by

    print(gps)


if __name__ == "__main__":
    robot, walls, boxes, moves, (rows, cols) = read_input("input.txt")
    print(moves)
    print_house(walls, robot, boxes, rows, cols)
    goods_position(robot, walls, boxes, moves, rows, cols)
