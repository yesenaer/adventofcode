from pathlib import Path


RESOURCES_DIR = Path(__file__).parent / 'resources'


def first_assignment():
    result = 0
    with open(RESOURCES_DIR / 'day4_input.txt') as file:
        for line in file:
            splitted = line.split(':')
            card_name = splitted[0]
            numbers = splitted[1].split('|')
            winners = numbers[0].split()
            our_numbers = numbers[1].split()
            winning_numbers_in_line = []
            for x in our_numbers:
                if x in winners:
                    winning_numbers_in_line.append(x)
            if len(winning_numbers_in_line) > 0:
                points = pow(2, len(winning_numbers_in_line)-1)
                result += points

    return result


def second_assignment():
    result = 0
    card_counts = {}
    for i in range(202):
        card_counts[i] = 0

    with open(RESOURCES_DIR / 'day4_input.txt') as file:
        for line in file:

            splitted = line.split(':')
            card_name = splitted[0]
            card_id = int(card_name.replace('Card', '').strip())
            card_counts[card_id] += 1
            numbers = splitted[1].split('|')
            winners = numbers[0].split()
            our_numbers = numbers[1].split()
            winning_numbers_in_line = []
            for x in our_numbers:
                if x in winners:
                    winning_numbers_in_line.append(x)
            if len(winning_numbers_in_line) > 0:
                for y in range(1, len(winning_numbers_in_line) + 1):
                    update_id = card_id + y
                    if update_id <= 202:
                        card_counts[update_id] += card_counts[card_id] * 1
    for z in card_counts:
        result += card_counts[z]
    return result


print(f'answer to assignment 1 is: {first_assignment()}')  
print(f'answer to assignment 2 is: {second_assignment()}')
