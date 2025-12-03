from pathlib import Path

RESOURCES = Path(__file__).parent / 'resources'


def process_input() -> tuple[list, list]:
    """Processes day1 input file into 2 lists."""
    first = []
    second = []
    with open(RESOURCES / 'day1_input.txt') as file:
        for line in file:
            first.append(line[0])
            second.append(int(line[1:]))
    return first, second


def first_assignment() -> int:
    times_zero = 0
    dial_position = 50
    direction, steps = process_input()
    
    if not len(direction) == len(steps):
        raise ValueError("Input lists are not of equal length.")

    for i in range(len(direction)):
        if direction[i] == 'L':
            dial_position -= steps[i]
        elif direction[i] == 'R':
            dial_position += steps[i]
        else:
            raise ValueError(f"Invalid direction character: {direction[i]}")   
        # correct for the dial wrapping around
        dial_position = dial_position % 100
        if dial_position < 0 or dial_position > 99:
            raise ValueError(f"Dial position out of bounds: {dial_position}")
        if dial_position == 0:
            times_zero += 1
    return times_zero


def second_assignment() -> int:
    result = 0
    return result


print(f'answer to assignment 1 is: {first_assignment()}')  # 1158
print(f'answer to assignment 2 is: {second_assignment()}')