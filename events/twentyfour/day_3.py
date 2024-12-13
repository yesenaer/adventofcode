from pathlib import Path
import re

RESOURCES = Path(__file__).parent / 'resources'


def first_assignment():
    multiplication_results = 0
    
    # process input and calculate results
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
    
    # process input into one full command
    full_command = "do()"  # starting condition
    with open(RESOURCES / 'day3_input.txt') as file:
        for line in file:
            line = line.replace("\r", "").replace("\n", "")
            full_command += line 

    # have the condition change start a new line 
    full_command = full_command.replace("don't()", "\ndon't()")
    full_command = full_command.replace("do()", "\ndo()")

    # conclude with writing updated commands to file
    with open(RESOURCES / 'day3_output.txt', "w") as output:
        output.write(full_command)
    
    # use updated commands to again process multiplications, as long as line is do()
    with open(RESOURCES / 'day3_output.txt') as file:
        for line in file:
            if line.startswith("don't()"):
                # should not process
                continue
            else:
                # processes the line for multiplications
                hits = re.findall('m{1}u{1}l{1}\(\d{1,3}\,\d{1,3}\)', line)
                for hit in hits:
                    digit = (hit.replace('mul(', '').replace(')', '')).split(',')
                    result = int(digit[0]) * int(digit[1])
                    multiplication_results += result  

    return multiplication_results


print(f'answer to assignment 1 is: {first_assignment()}') 
print(f'answer to assignment 2 is: {second_assignment()}') 