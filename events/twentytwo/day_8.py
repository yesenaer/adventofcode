from typing import List
import numpy as np


# class Tree:
#     # x: int
#     # y: int
#     height: int
#     visible: bool
#
#     def __init__(self, height: int):
#         self.height = height
#         self.visible = True


def first_assignment(f: str) -> int:
    total_score = 0

    forest = np.loadtxt(fname=f, converters=float, dtype=int)
    # print(forest.max(axis=0))
    # for each tree in forest
    for r in range(0, 99):
        for c in range(0, 99):

            if r == 0 or r == 98:  # tree is at side
                total_score += 1
                continue
            if c == 0 or c == 98:  # tree is top or bottom
                total_score += 1
                continue

            if forest[r, c] > max(forest[r][0:c]):  # tree is higher than left
                total_score += 1
                continue

            if forest[r, c] > max(forest[r][c+1:99]):  # tree is higher than right
                total_score += 1
                continue

            arr = forest[0:r, c]
            if forest[r, c] > max(arr):  # tree is higher than top
                total_score += 1
                continue

            arr2 = forest[r+1:99, c]
            if forest[r, c] > max(arr2):  # tree is higher than bottom
                total_score += 1
                continue

    return total_score


def second_assignment(f: str) -> int:
    total_score = 0
    forest = np.loadtxt(fname=f, converters=float, dtype=int)

    for r in range(0, 99):
        for c in range(0, 99):

            if r == 0 or r == 98 or c == 0 or c == 98:  # tree is at edge
                continue
        # check sides for higher trees








    return total_score


def generate_matrix_input(f: str, new_f: str):
    new_file = open(new_f, "w")
    with open(f) as file:
        for line in file:
            updated_line = ' '.join(line)
            new_file.write(updated_line)


puzzle_input = 'resources/day8_input.txt'
filename = 'resources/day8_updated.txt'
generate_matrix_input(puzzle_input, filename)
print(f'answer to assignment 1 is: {first_assignment(filename)}')
print(f'answer to assignment 2 is: {second_assignment(filename)}')
