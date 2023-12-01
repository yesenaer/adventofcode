from typing import Tuple


def check_full_overlap(left: list, right: list) -> int:
    if int(left[0]) <= int(right[0]):  # check if left start is smaller
        if int(left[1]) >= int(right[1]):  # then it should also be equal or larger
            return 1
    if int(right[0]) <= int(left[0]):  # check if right is smaller + larger
        if int(right[1]) >= int(left[1]):
            return 1
    return 0


def check_partial_overlap(left: list, right: list) -> int:
    if check_full_overlap(left, right):  # it fully overlaps, no further questions
        return 1
    if int(left[0]) <= int(right[0]) <= int(left[1]):  # right starts before left ends
        return 1
    if int(right[0]) <= int(left[0]) <= int(right[1]):  # left starts before right ends
        return 1
    return 0


def first_assignment(f: str) -> int:
    total_score = 0
    with open(f) as file:
        for line in file:
            left, right = extract_assignments(line)
            total_score += check_full_overlap(left, right)

        return total_score


def second_assignment(f: str) -> int:
    total_score = 0
    with open(f) as file:
        for line in file:
            left, right = extract_assignments(line)
            total_score += check_partial_overlap(left, right)
    return total_score


def extract_assignments(line: str) -> Tuple[list, list]:
    assignment = line.strip().split(',')
    left = assignment[0].split('-')
    right = assignment[1].split('-')
    return left, right


puzzle_input = 'resources/day4_input.txt'
print(f'answer to assignment 1 is: {first_assignment(puzzle_input)}')
print(f'answer to assignment 2 is: {second_assignment(puzzle_input)}')
