from typing import Dict


def generate_elves_dict(path: str) -> Dict:
    with open(path) as file:
        elves = {}
        elve_number = 1
        elves[elve_number] = 0
        for line in file:
            if line.strip():
                elves[elve_number] += int(line)
            else:
                elve_number += 1
                elves[elve_number] = 0
        return elves


def first_assignment():
    elves = generate_elves_dict('resources/day1_input.txt')
    return max(elves.values())


def second_assignment():
    elves = generate_elves_dict('resources/day1_input.txt')
    total_sum = 0
    for i in range(3):
        current_highest = elves[max(elves, key=elves.get)]
        total_sum += current_highest
        del elves[max(elves, key=elves.get)]

    return total_sum


print(f'answer to assignment 1 is: {first_assignment()}')
print(f'answer to assignment 2 is: {second_assignment()}')
