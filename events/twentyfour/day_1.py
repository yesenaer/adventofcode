from pathlib import Path

RESOURCES = Path(__file__).parent / 'resources'


def process_input() -> tuple[list, list]:
    """Processes day1 input file into 2 lists."""
    first = []
    second = []
    with open(RESOURCES / 'day1_input.txt') as file:
        for line in file:
            splitted = line.split()
            first.append(int(splitted[0]))
            second.append(int(splitted[1]))
    return first, second


def first_assignment() -> int:
    total_distance = 0
    first, second = process_input()
    first.sort()
    second.sort()
    
    for i in range(len(first)):
        if second[i] > first[i]:
            diff = second[i] - first[i]
        else: 
            diff = first[i] - second[i]
        total_distance += diff
    return total_distance


def second_assignment() -> int:
    similarity_score = 0
    first, second = process_input()
    for i in range(len(first)):
        count = second.count(first[i])
        score = first[i] * count 
        similarity_score += score
    return similarity_score


print(f'answer to assignment 1 is: {first_assignment()}')
print(f'answer to assignment 2 is: {second_assignment()}')