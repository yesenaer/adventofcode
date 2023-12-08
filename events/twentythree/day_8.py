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
    with open(RESOURCES_DIR / 'day8_input.txt') as file:
        pass
    return 0


print(f'answer to assignment 1 is: {first_assignment()}')
print(f'answer to assignment 2 is: {second_assignment()}')
