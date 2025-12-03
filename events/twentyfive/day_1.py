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
    result = 0
    return result


def second_assignment() -> int:
    result = 0
    return result


print(f'answer to assignment 1 is: {first_assignment()}')
print(f'answer to assignment 2 is: {second_assignment()}')