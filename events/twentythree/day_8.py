from pathlib import Path
import pandas as pd

RESOURCES_DIR = Path(__file__).parent / 'resources'


def first_assignment():
    result = 0
    rows = []
    with open(RESOURCES_DIR / 'day8_input.txt') as file:
        rl_instructions = file.readline().strip()
        for line in file:
            line = line.strip()
            if not line:
                continue

            parts = line.split('=')
            node = parts[0].strip()
            rl_elements = parts[1].strip().replace('(', '').replace(')', '').split(',')
            left = rl_elements[0].strip()
            right = rl_elements[1].strip()

            row = {'node': node, 'L': left, 'R': right}
            rows.append(row)
    df = pd.DataFrame(data=rows, columns=['node', 'L', 'R'])
    df.set_index(['node'])

    current_location = 'AAA'
    found_zzz = False
    while not found_zzz:
        for direction in rl_instructions:
            cdf = df.loc[df['node'] == current_location]
            new_dest = cdf[direction].to_string(index=False)
            result += 1
            if new_dest == 'ZZZ':
                found_zzz = True
                break
            else:
                current_location = new_dest

    return result


def second_assignment():
    result = 0
    rows = []
    with open(RESOURCES_DIR / 'day8_input.txt') as file:
        rl_instructions = file.readline().strip()
        for line in file:
            line = line.strip()
            if not line:
                continue

            parts = line.split('=')
            node = parts[0].strip()
            rl_elements = parts[1].strip().replace('(', '').replace(')', '').split(',')
            left = rl_elements[0].strip()
            right = rl_elements[1].strip()

            row = {'node': node, 'L': left, 'R': right}
            rows.append(row)
    df = pd.DataFrame(data=rows, columns=['node', 'L', 'R'])
    df.set_index(['node'])

    # current_location = 'GRA'  # did this for all 6 ending in A
    # for i in range(0, 1000):
    #     for direction in rl_instructions:
    #         cdf = df.loc[df['node'] == current_location]
    #         new_dest = cdf[direction].to_string(index=False)
    #         result += 1
    #         if new_dest[2] == 'Z':
    #             print(f'found a Z at end of dest at {result=} for {new_dest=}')
    #             """"
    #             Using this loop i found out that all have a recurring end of destination with Z
    #             # gra at 15517   -> loops every 15,517
    #             # aaa at 19199   -> loops every 19,199
    #             # xva at 20777   -> loops every 20,777
    #             # jva at 11309   -> loops every 11,309
    #             # sxa at 17621   -> loops every 17,621
    #             # nba at 13939   -> loops every 13,939
    #
    #             T1 = (1-x) * T2
    #             T2 = (1+x) * T1
    #             """
            # current_location = new_dest

    return result



# print(f'answer to assignment 1 is: {first_assignment()}')
print(f'answer to assignment 2 is: {second_assignment()}')
