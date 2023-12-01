
def first_assignment():
    with open('resources/day2_input.txt') as file:
        depth = 0
        horizontal = 0

        for line in file:
            command = line.split()
            if command[0] == "forward":
                horizontal += int(command[1])
            elif command[0] == "down":
                depth += int(command[1])
            elif command[0] == "up":
                depth -= int(command[1])

        print(f'{depth=} and {horizontal=}')
        print(f'multiplied={depth*horizontal}')


def second_assignment():
    with open('resources/day2_input.txt') as file:
        depth = 0
        horizontal = 0
        aim = 0

        for line in file:
            command = line.split()
            if command[0] == "down":
                aim += int(command[1])
            elif command[0] == "up":
                aim -= int(command[1])
            elif command[0] == "forward":
                horizontal += int(command[1])
                depth += aim * int(command[1])

        print(f'{depth=} and {horizontal=} and {aim=}')
        print(f'multiplied={depth*horizontal}')


second_assignment()
