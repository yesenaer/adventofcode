from enum import Enum
from typing import Tuple, List


class bcolors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'


class Crate:
    id: str

    def __init__(self, id: str):
        self.id = id

    def __repr__(self) -> str:
        return self.id.replace('[', '').replace(']', '')


class Stack:
    id: int
    crates: List[Crate]

    def __init__(self, id: int, crates: List[Crate] = None):
        self.id = id
        if crates:
            self.crates = crates
        else:
            self.crates = []

    def add_crate(self, crate: Crate):
        self.crates.append(crate)

    def _insert_crate_at_bottom(self, crate: Crate):
        self.crates.insert(0, crate)

    def remove_crate(self) -> Crate:
        return self.crates.pop()

    def get_top_crate(self) -> str:
        return self.crates[-1].__repr__()


class Crane(Enum):
    CRATEMOVER9000 = 0
    CRATEMOVER9001 = 1


class Ship:
    crane_type: Crane
    capacity: int
    stacks: List[Stack]

    def __init__(self, crane_type: Crane, capacity: int):
        self.crane_type = crane_type
        self.capacity = capacity
        self.stacks = []
        for i in range(1, capacity + 1):  # start at 1 instead of 0
            stack = Stack(id=i)
            self.stacks.append(stack)

    def __repr__(self):


        length = []
        for i in self.stacks:
            length.append(len(i.crates))

        for height in range(max(length) - 1, -1, -1):
            print()
            print('  ', end='')
            for index in self.stacks:
                if len(index.crates) > height:
                    print(bcolors.RED + index.crates[height].id, end=" ")
                else:
                    print('    ' + bcolors.ENDC, end='')

        print(bcolors.GREEN + '|----|')
        print('\  1   2   3   4   5   6   7   8   9  |    / ')
        print(' \________________________________________/  ' + bcolors.ENDC)
        return ''

    def get_index_from_id(self, id: int) -> int:
        for i in range(len(self.stacks)):
            if self.stacks[i].id == id:
                return i

    def move_crate_to_another_stack(self, from_stack: int, to_stack: int):
        from_index = self.get_index_from_id(from_stack)
        to_index = self.get_index_from_id(to_stack)

        crate = self.stacks[from_index].remove_crate()
        self.stacks[to_index].add_crate(crate)

    def move_crates_per_command(self, command: str):
        steps = command.split()
        crate_amount = int(steps[1])
        from_stack_id = int(steps[3])
        to_stack_id = int(steps[5])
        if self.crane_type == Crane.CRATEMOVER9000:
            for i in range(1, crate_amount + 1):
                self.move_crate_to_another_stack(from_stack_id, to_stack_id)
        else:
            self.move_all_crates_at_once(from_stack_id, to_stack_id, crate_amount)

    def get_top_crates(self) -> str:
        top_crates = ''
        for i in self.stacks:
            top_crates += i.get_top_crate()
        return top_crates

    def move_all_crates_at_once(self, from_stack, to_stack, crate_amount: int):
        from_index = self.get_index_from_id(from_stack)
        to_index = self.get_index_from_id(to_stack)

        crates_to_move = self.stacks[from_index].crates[-crate_amount:]
        for crate in crates_to_move:
            self.stacks[to_index].add_crate(crate)
        del self.stacks[from_index].crates[-crate_amount:]


def first_assignment(input_path: str) -> str:
    deck_layout, instructions = split_input_to_start_and_instructions(input_path)
    ship = load_initial_ship(Crane.CRATEMOVER9000, deck_layout)
    for instruction in instructions:
        ship.move_crates_per_command(instruction)

    return ship.get_top_crates()


def load_initial_ship(crane: Crane, deck: List) -> Ship:
    capacity = int(deck.pop()[-1])  # get last row (the numbers) last digit (max row), remove that row (not crates)
    ship = Ship(crane, capacity)
    deck.reverse()
    for level in deck:
        crate_width = 4
        for crate_position in range(0, len(level), crate_width):
            current_stack = (crate_position + crate_width) // crate_width
            crate_location = str(level[slice(crate_position, crate_position + crate_width)]).strip()
            if crate_location:  # only add if there is actually a crate
                crate = Crate(id=crate_location)
                stack_index = ship.get_index_from_id(current_stack)
                ship.stacks[stack_index].add_crate(crate)

    return ship


def second_assignment(input_path: str) -> str:
    deck_layout, instructions = split_input_to_start_and_instructions(input_path)
    ship = load_initial_ship(Crane.CRATEMOVER9001, deck_layout)
    print(ship)
    for instruction in instructions:
        ship.move_crates_per_command(instruction)
    print(ship)
    return ship.get_top_crates()


def split_input_to_start_and_instructions(f: str) -> Tuple[list, list]:
    start = []
    instructions = []
    with open(f) as file:
        for line in file:
            if line.startswith('move'):
                instructions.append(line.strip())
            elif line.strip():
                start.append(line.replace('\n', ''))
    return start, instructions


puzzle_input = 'resources/day5_input.txt'
print(f'answer to assignment 1 is: {first_assignment(puzzle_input)}')
print(f'answer to assignment 2 is: {second_assignment(puzzle_input)}')
