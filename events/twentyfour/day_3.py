from pathlib import Path
import re

RESOURCES = Path(__file__).parent / 'resources'



def first_assignment():
    multiplication_results = 0
    with open(RESOURCES / 'day3_input.txt') as file:
        for line in file:
            hits = re.findall('m{1}u{1}l{1}\(\d{1,3}\,\d{1,3}\)', line)
            for hit in hits:
                digit = (hit.replace('mul(', '').replace(')', '')).split(',')
                result = int(digit[0]) * int(digit[1])
                multiplication_results += result             
    return multiplication_results


def second_assignment():
    multiplication_results = 0
    return multiplication_results


print(f'answer to assignment 1 is: {first_assignment()}') 
print(f'answer to assignment 2 is: {second_assignment()}') 