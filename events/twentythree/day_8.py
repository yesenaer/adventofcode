from pathlib import Path


RESOURCES_DIR = Path(__file__).parent / 'resources'


def first_assignment():
    result = 0
    with open(RESOURCES_DIR / 'day8_input.txt') as file:
        pass
    return result


def second_assignment():
    result = 0
    with open(RESOURCES_DIR / 'day8_input.txt') as file:
        pass
    return 0


print(f'answer to assignment 1 is: {first_assignment()}')
print(f'answer to assignment 2 is: {second_assignment()}')
