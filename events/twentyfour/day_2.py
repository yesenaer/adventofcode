from pathlib import Path

RESOURCES = Path(__file__).parent / 'resources'


def split_to_int(line):
    report = line.split()
    for i in range(len(report)):
        report[i] = int(report[i])
    return report


def first_assignment():
    total_safe_reports = 0
    with open(RESOURCES / 'day2_input.txt') as file:
        for line in file:
            report = split_to_int(line)
            try:
                # increasing
                if report[0] < report [1]:
                    for i in range(1,len(report)):
                        current = report[i]
                        previous = report[i-1]
                        assert previous < current  # should increase
                        assert (current - previous) <= 3 # with max 3
                    total_safe_reports += 1
                # decreasing
                elif report[0] > report[1]:
                    for i in range(1, len(report)):
                        current = report[i]
                        previous = report[i-1]
                        assert previous > current  # should decrease
                        assert (previous - current) <= 3  # with max 3
                    total_safe_reports += 1
                else:
                    continue  # not increasing/decreasing != safe
            except:
                continue  # failed asserts land here      
    return total_safe_reports


def second_assignment():
    total_safe_reports = 0
    return total_safe_reports


print(f'answer to assignment 1 is: {first_assignment()}')
print(f'answer to assignment 2 is: {second_assignment()}')