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


def turn_left(start: int, steps: int) -> tuple[int, int]: 
        times_zero = 0
        if start == 0:
            current = 100
        else:
            current = start

        for i in range(steps):
            current -= 1
            if current == 0:
                times_zero += 1
                current = 100
       
        if current == 100:
            current = 0

        if current > 100 or current < 0:
            raise ValueError(f"Dial position out of bounds: {current}")
        
        return current, times_zero


def turn_right(start: int, steps: int) -> tuple[int, int]: 
        times_zero = 0
        if start == 100:
            current = 0
        else:
            current = start

        for i in range(steps):
            current += 1
            if current == 100:
                times_zero += 1
                current = 0
        
        if current > 100 or current < 0:
            raise ValueError(f"Dial position out of bounds: {current}")

        return current, times_zero


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
    times_zero = 0
    dial_position = 50
    direction, steps = process_input()
    
    if not len(direction) == len(steps):
        raise ValueError("Input lists are not of equal length.")

    for i in range(len(direction)):

        if direction[i] == 'L':
            dial_position, count = turn_left(dial_position, steps[i])
            times_zero += count
            
        
        elif direction[i] == 'R':
            dial_position, count = turn_right(dial_position, steps[i])
            times_zero += count

    return times_zero


print(f'answer to assignment 1 is: {first_assignment()}')  # 1158
print(f'answer to assignment 2 is: {second_assignment()}')  # 6860