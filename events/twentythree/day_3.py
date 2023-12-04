from pathlib import Path


RESOURCES_DIR = Path(__file__).parent / 'resources'


class Digit:
    value: int
    part: bool
    line_nr: int
    index: list  # f.e. [2, 3, 4] for the indexes of the digit in the line

    def __init__(self, value, part, line_nr, index) -> None:
        self.value = int(value)
        self.part = part
        self.line_nr = line_nr 
        self.index = index 


class Symbol:
    value: str
    line_nr: int 
    index: int 

    def __init__(self, value, line_nr, index) -> None:
        self.value = value
        self.line_nr = line_nr
        self.index = index

    def is_adjacent(self, line_nr: int, index_value: int, checked_value: int) -> bool:
        if line_nr not in (self.line_nr, self.line_nr - 1, self.line_nr + 1): 
            return False
        if index_value in (self.index, self.index - 1, self.index + 1):
            return True
        return False
        


def first_assignment():
    digits, symbols = parse_first_assignment_input()
    sum = 0

    for line_nr in digits: 
        for digit in digits[line_nr]: 
            for index in digit.index:
                for symbol in symbols[digit.line_nr-1]:
                    if symbol.is_adjacent(digit.line_nr, index, digit.value):
                        if digit.part == False:
                            sum += digit.value
                        digit.part = True
                for symbol in symbols[digit.line_nr]:
                    if symbol.is_adjacent(digit.line_nr, index, digit.value):
                        if digit.part == False:
                            sum += digit.value
                        digit.part = True
                for symbol in symbols[digit.line_nr + 1]:
                    if symbol.is_adjacent(digit.line_nr, index, digit.value):
                        if digit.part == False:
                            sum += digit.value
                        digit.part = True

    return sum

def parse_first_assignment_input(filename='day3_input.txt', extra: int = 140):
    digits = {-1: []}
    symbols = {-1: [], extra: []}
    with open(RESOURCES_DIR / filename) as file:
        chars = set()
        line_nr = 0
        for line in file: 
            index = 0
            symbols[line_nr] = []
            digits[line_nr] = []
            digit_value = ''
            digit_index = []
            for char in line: 
                if char not in  ('.', '\n') and not char.isdigit():
                    chars.add(char)
                    symbol = Symbol(value=char, line_nr=line_nr, index=index)
                    symbols[line_nr].append(symbol)
                if char.isdigit():
                    digit_value += char
                    digit_index.append(index)
                if char in ('.', '\r', '\n') or char in chars:
                    if len(digit_value) > 0:
                        digit = Digit(value=digit_value, part=False, line_nr=line_nr, index=digit_index)
                        digits[line_nr].append(digit)
                        digit_value = ''
                        digit_index = []
                index += 1
            
            line_nr += 1
    return digits, symbols


def tests_first():
    digits, symbols = parse_first_assignment_input('day3_test_input.txt', extra=12)
    sum = 0

    for line_nr in digits: 
        for digit in digits[line_nr]: 
            for index in digit.index:
                for symbol in symbols[digit.line_nr-1]:
                    if symbol.is_adjacent(digit.line_nr, index, digit.value):
                        if digit.part == False:
                            sum += digit.value
                        digit.part = True
                for symbol in symbols[digit.line_nr]:
                    if symbol.is_adjacent(digit.line_nr, index, digit.value):
                        if digit.part == False:
                            sum += digit.value
                        digit.part = True
                for symbol in symbols[digit.line_nr + 1]:
                    if symbol.is_adjacent(digit.line_nr, index, digit.value):
                        if digit.part == False:
                            sum += digit.value
                        digit.part = True

    for line_nr in digits: 
        for digit in digits[line_nr]:
            if not digit.part:
                print(f'excluded {digit.line_nr}  {digit.value} at {digit.index}')

    return sum

def second_assignment():
    digits, symbols = parse_first_assignment_input('day3_input.txt')
    stars = {}
    gear_ratios = 0

    for line_nr in digits: 
        for digit in digits[line_nr]: 
            for index in digit.index:
                
                for symbol in symbols[digit.line_nr-1]:
                    name = f'{symbol.line_nr}_{symbol.index}'
                    if symbol.value == '*' and symbol.is_adjacent(digit.line_nr, index, digit.value):
                        existing = stars.get(name, set())
                        existing.add(digit)
                        stars[name] = existing
                for symbol in symbols[digit.line_nr]:
                    name = f'{symbol.line_nr}_{symbol.index}'
                    if symbol.value == '*' and symbol.is_adjacent(digit.line_nr, index, digit.value):
                        existing = stars.get(name, set())
                        existing.add(digit)
                        stars[name] = existing
                for symbol in symbols[digit.line_nr + 1]:
                    name = f'{symbol.line_nr}_{symbol.index}'
                    if symbol.value == '*' and symbol.is_adjacent(digit.line_nr, index, digit.value):
                        existing = stars.get(name, set())
                        existing.add(digit)
                        stars[name] = existing

    for star in stars:
        if len(stars[star]) == 2:
            items = []
            for x in stars[star]:
                items.append(x.value)
            ratio = items[0] * items[1]
            gear_ratios += ratio

    return gear_ratios


print(f'answer to assignment 1 is: {first_assignment()}')  
# print(f'answer to assignment 1 tests is: {tests_first()}')  
print(f'answer to assignment 2 is: {second_assignment()}') 
