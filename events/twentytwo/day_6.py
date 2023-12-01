from typing import List


def create_list_from_input(f):
    unique_chars = []
    with open(f) as file:
        for line in file:
            for char in line:
                unique_chars.append(char)
    return unique_chars


def find_sequence(unique_chars: List, sequence_length) -> int:
    before_sequence = sequence_length - 1

    total_count = before_sequence  # start counting at first sequence
    for i in range(before_sequence, len(unique_chars) - 1):
        sequence_start = i - before_sequence
        current = i + 1  # to include current in slice
        subset = unique_chars[sequence_start:current]

        if len(''.join(set(subset))) == sequence_length:  # set keeps only unique
            total_count += 1
            # if this hits, we found the start-of-packet location
            break
        else:
            total_count += 1
    return total_count


def first_assignment(f: str) -> int:
    required_length = 4
    return find_sequence(create_list_from_input(f), required_length)


def second_assignment(f: str) -> int:
    required_length = 14
    return find_sequence(create_list_from_input(f), required_length)


puzzle_input = 'resources/day6_input.txt'
print(f'answer to assignment 1 is: {first_assignment(puzzle_input)}')
print(f'answer to assignment 2 is: {second_assignment(puzzle_input)}')
