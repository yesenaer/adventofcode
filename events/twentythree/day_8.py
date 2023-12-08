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
    """Initially used the file again to parse and add to dataframe"""
    """
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
    """

    """2. Checked for the specific locations that contained an A at the end:
    
        These are the following six: GRA, AAA, XVA, JVA, SXA, NBA
        
        For these locations, i checked when they would land at a location ending in 'Z'. 
        
        When i let them continue past the first one, i noticed they are looping on that exact number    
        Using this loop i found out that all have a recurring end of destination with Z
                # gra at 15517   -> loops every 15,517
                # aaa at 19199   -> loops every 19,199
                # xva at 20777   -> loops every 20,777
                # jva at 11309   -> loops every 11,309
                # sxa at 17621   -> loops every 17,621
                # nba at 13939   -> loops every 13,939
    """
    # current_location = 'GRA'  # did this for all 6 ending in A
    # for i in range(0, 1000):
    #     for direction in rl_instructions:
    #         cdf = df.loc[df['node'] == current_location]
    #         new_dest = cdf[direction].to_string(index=False)
    #         result += 1
    #         if new_dest[2] == 'Z':
    #             print(f'found a Z at end of dest at {result=} for {new_dest=}')
    #         current_location = new_dest

    """ 3. I tried running code that checked when all would be dividable by an int (meaning they met at Z). 
        however this became a brute force way that was not finishing soon, so i started investigating how its called 
        when you find the lowest dividable number for both, this is called Least Common Multiple (LCM).
        it is calculated by using the Prime Factorisation of both numbers and adding those up 
        (duplicate primes are only used once).
        gra = 15517 -> 59 x 263
        aaa = 19199 -> 73 x 263 
        xva = 20777 -> 79 x 263
        jva = 11309 -> 43 x 263
        sxa = 17621 -> 67 x 263
        nba = 13939 -> 53 x 263
        
        using all of those once, you get result = 59 * 73 * 79 * 43 * 67 * 53 * 263
    """
    result = 59 * 73 * 79 * 43 * 67 * 53 * 263
    return result

    # see here my failed attempt at running till they meet
    # result = 0
    # GRA = False # had one for each
    # gra = 15517 # had an entry for all
    # while not (GRA and the others):
    #     result += 1
    #     if (result / gra).is_integer():
    #         # print(f'gra is int at {result=}')
    #         GRA = True
    #     else:
    #         GRA = False


print(f'answer to assignment 1 is: {first_assignment()}')
print(f'answer to assignment 2 is: {second_assignment()}')
