from typing import IO
POINTS = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3
}
WINNING_MOVE = {
    "A": "B",
    "B": "C",
    "C": "A"

}


def first_assignment(f: str) -> int:
    total_score = 0
    with open(f) as file:
        for line in f:
            command = line.split()
            not_u = command[0]
            u = command[1]
            total_score += POINTS[u]

            if (u == "X" and not_u == "C") or (u == "Y" and not_u == "A") or (u == "Z" and not_u == "B"):
                total_score += 6
            elif POINTS[u] == POINTS[not_u]:
                total_score += 3

        return total_score


def second_assignment(f: str) -> int:
    total_score = 0
    with open(f) as file:

        for line in file:
            command = line.split()
            not_u = command[0]
            u = command[1]

            if u == "Z":
                total_score += 6
                total_score += POINTS[WINNING_MOVE[not_u]]
            elif u == "Y":
                total_score += 3
                total_score += POINTS[not_u]  # you will score same value as opponent
            elif u == "X":
                what_would_be_winning = WINNING_MOVE[not_u]
                losing_move = WINNING_MOVE[what_would_be_winning]
                total_score += POINTS[losing_move]

        return total_score


puzzle_input = 'resources/day2_input.txt'
print(f'answer to assignment 1 is: {first_assignment(puzzle_input)}')
print(f'answer to assignment 2 is: {second_assignment(puzzle_input)}')
