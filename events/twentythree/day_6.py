from pathlib import Path


RESOURCES_DIR = Path(__file__).parent / 'resources'


def first_assignment():
    with open(RESOURCES_DIR / 'day5_input.txt') as file:
        pass
    return 0


def second_assignment():
    with open(RESOURCES_DIR / 'day5_input.txt') as file:
        pass

    return 0


print(f'answer to assignment 1 is: {first_assignment()}')
print(f'answer to assignment 2 is: {second_assignment()}')
