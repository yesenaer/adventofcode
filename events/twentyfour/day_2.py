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
    with open(RESOURCES / 'day2_input.txt') as file:
        for line in file:
            report = split_to_int(line)
            try:
                faulty_index = None
                # increasing
                if report[0] < report [1]:
                    for i in range(1,len(report)):
                        current = report[i]
                        previous = report[i-1]
                        if not previous < current: # should increase
                            faulty_index = i
                            break
                        if not (current - previous) <= 3: # with max 3
                            faulty_index = i
                            break

                    
                # decreasing
                elif report[0] > report[1]:
                    for i in range(1, len(report)):
                        current = report[i]
                        previous = report[i-1]
                        if not previous > current: # should decrease
                            faulty_index = i  
                            break
                        if not (previous - current) <= 3:  # with max 3
                            faulty_index = i
                            break
                    
                else:
                    faulty_index = 0 
                
                if faulty_index is None:
                    total_safe_reports += 1 
                    continue
                elif faulty_index == 0 or faulty_index > 1: 
                    report.pop(faulty_index)
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
                # elif faulty_index == 1: 
                #     print(report)
                #     zero = report[:].pop(0)
                #     one = report[:].pop(1)
                #     try: 
                #         if one[0] < one[1]:
                #             for i in range(1,len(one)):
                #                 current = one[i]
                #                 previous = one[i-1]
                #                 assert previous < current  # should increase
                #                 assert (current - previous) <= 3 # with max 3
                #             total_safe_reports += 1
                #         # decreasing
                #         elif one[0] > one[1]:
                #             for i in range(1, len(one)):
                #                 current = one[i]
                #                 previous = one[i-1]
                #                 assert previous > current  # should decrease
                #                 assert (previous - current) <= 3  # with max 3
                #             total_safe_reports += 1
                #     except:
                #         if zero[0] < zero[1]:
                #             for i in range(1,len(zero)):
                #                 current = zero[i]
                #                 previous = zero[i-1]
                #                 assert previous < current  # should increase
                #                 assert (current - previous) <= 3 # with max 3
                #             total_safe_reports += 1
                #         # decreasing
                #         elif zero[0] > zero[1]:
                #             for i in range(1, len(zero)):
                #                 current = zero[i]
                #                 previous = zero[i-1]
                #                 assert previous > current  # should decrease
                #                 assert (previous - current) <= 3  # with max 3
                #             total_safe_reports += 1
                else:
                    continue  # not increasing/decreasing != safe
            except:
                continue  # failed asserts land here      
    return total_safe_reports


print(f'answer to assignment 1 is: {first_assignment()}')
print(f'answer to assignment 2 is: {second_assignment()}')  # between 708 and 765    so its about the pop(0) and pop(1) 