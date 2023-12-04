from pathlib import Path


RESOURCES_DIR = Path(__file__).parent / 'resources'



def first_assignment():
    result = 0
    with open(RESOURCES_DIR / 'day4_input.txt') as file:
        for line in file:
            splitted = line.split(':')
            card_name = splitted[0]
            print(card_name)
            numbers = splitted[1].split('|')
            winners = numbers[0].split()
            our_numbers = numbers[1].split()

            # print(winners)
            # print(our_numbers)
            winning_numbers_in_line = []
            for x in our_numbers:
                if x in winners:
                    winning_numbers_in_line.append(x)
            print(winning_numbers_in_line)
            if len(winning_numbers_in_line) > 0:
                points = pow(2, len(winning_numbers_in_line)-1)
                print(points)
                result += points
            else: print('0')
        

    return result


def second_assignment():
    result = 0
    return result


print(f'answer to assignment 1 is: {first_assignment()}')  
print(f'answer to assignment 2 is: {second_assignment()}') 
