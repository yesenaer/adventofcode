
def first_assignment():
    with open('resources/day1_input.txt') as file:
        depth = int(file.readline())
        increase_count = 0
        answer = lambda i, depth: 1 if (i > depth) else 0

        for line in file:
            increase_count += answer(int(line), depth)
            depth = int(line)

        print(increase_count)


def second_assignment():
    with open('resources/day1_input.txt') as file:
        agg_list = []
        increase_count = 0
        first = int(file.readline())
        second = int(file.readline())
        answer = lambda current, previous: 1 if (current > previous) else 0

        for line in file:
            third = int(line)
            window = sum([first, second, third])
            if len(agg_list) >= 1:
                increase_count += answer(window, agg_list[-1])
            agg_list.append(window)
            first = second
            second = third
        print(increase_count)


first_assignment()
second_assignment()
