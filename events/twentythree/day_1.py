def extract_digits_from_line(line: str) -> list[str]:
    return [char for char in line if char.isdigit()]  # just to mess with you


def replace_written_digits(line: str) -> str:
    digit_map = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8',
                 'nine': '9'}
    result = line
    indexes = []

    # looping for hits first, because some digits have overlapping values in their text
    for key in digit_map:
        if key in result:
            lowest_index = line.find(key)
            highest_index = line.rfind(key)

            indexes.append((lowest_index, digit_map[key]))
            if highest_index > lowest_index:  # only append if not same
                indexes.append((highest_index, digit_map[key]))

    indexes.sort()

    # only replacing first and last digit for now (and only first char) given assignment, could be extended to all
    if len(indexes) >= 1:
        result = result[:indexes[0][0]] + indexes[0][1] + result[indexes[0][0]+1:]
    if len(indexes) > 1:
        result = result[:indexes[-1][0]] + indexes[-1][1] + result[indexes[-1][0]+1:]
    return result


def first_assignment():
    calibration_value = 0
    with open('resources/day1_input.txt') as file:
        for line in file:
            digits_only = extract_digits_from_line(line)
            value = int(f'{digits_only[0]}{digits_only[-1]}')  # only get first and last, repeat first if only 1
            calibration_value += value
    return calibration_value


def second_assignment():
    calibration_value = 0
    with open('resources/day1_input.txt') as file:
        for line in file:
            fixed_line = replace_written_digits(line)
            written_digits_only = extract_digits_from_line(fixed_line)
            value = int(f'{written_digits_only[0]}{written_digits_only[-1]}')
            calibration_value += value
    return calibration_value


print(f'answer to assignment 1 is: {first_assignment()}')
print(f'answer to assignment 2 is: {second_assignment()}')
