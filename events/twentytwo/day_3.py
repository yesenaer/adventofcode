import string
from itertools import chain
from typing import Dict, IO


def generate_priority_for_letters() -> Dict:
    priority = 1
    result = {}
    for letter in chain(string.ascii_lowercase, string.ascii_uppercase):
        result[letter] = priority
        priority += 1
    return result


def first_assignment(f: str, prio_dict: Dict) -> int:
    total_score = 0
    line_nr = 1
    with open(f) as file:
        for line in file:
            x = slice(len(line)//2)
            y = slice(len(line)//2, len(line), 1)
            for z in line[x]:
                if z in line[y]:
                    total_score += prio_dict[z]
                    break
            line_nr += 1
        return total_score


def second_assignment(f: str, prio_dict: Dict) -> int:
    total_score = 0
    line_nr = 1
    with open(f) as file:
        for line in file:
            group = [line.strip(), file.readline().strip(), file.readline().strip()]
            for i in group[0]:
                if i in group[1] and i in group[2]:
                    total_score += prio_dict[i]
                    break
        return total_score


priority_dict = generate_priority_for_letters()
puzzle_input = 'resources/day3_input.txt'
print(f'answer to assignment 1 is: {first_assignment(puzzle_input, priority_dict)}')
print(f'answer to assignment 2 is: {second_assignment(puzzle_input, priority_dict)}')
