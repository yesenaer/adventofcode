def first_assignment():
    games = extract_games_as_dict()
    result = 0 
    for game in games: 
        possible = check_reveals_for_max(games[game], red=12, green=13, blue=14)
        if possible: 
            result += game
    return result


def check_reveals_for_max(game: dict, red: int, green: int, blue: int) -> bool: 
    for reveal in game: 
        if reveal['red'] > red or reveal['green'] > green or reveal['blue'] > blue:
            return False
    return True


def extract_games_as_dict():
    games = {}
    with open('resources/day2_input.txt') as file:
        for line in file: 
            splitted = line.split(':')
            id = int(splitted[0].replace('Game ', ''))
            reveals = splitted[1].strip().split(';')
            reveals_list = []
            for reveal in reveals:
                colors = reveal.split(',')
                for color in colors: 
                    reveal_dict = {}
                    red, green, blue = 0, 0, 0
                    if 'green' in color:
                        green = int(color.replace('green', '').strip())
                    if 'blue' in color:
                        blue = int(color.replace('blue', '').strip())
                    if 'red' in color:
                        red = int(color.replace('red', '').strip())
                    reveal_dict['green'] = green
                    reveal_dict['blue'] = blue
                    reveal_dict['red'] = red
                    reveals_list.append(reveal_dict)   
            games[id] = reveals_list
    return games


def second_assignment():
    games = extract_games_as_dict()
    result = 0
    for game in games: 
        score = calculate_power_for_minimal_needed_colors(games[game])
        result += score
    return result


def calculate_power_for_minimal_needed_colors(game: dict): 
    min_red = 0
    min_green = 0
    min_blue = 0
    for reveal in game: 
        if reveal['red'] > min_red:
            min_red = reveal['red']
        if reveal['green'] > min_green:
            min_green = reveal['green']
        if reveal['blue'] > min_blue:
            min_blue = reveal['blue']
    score = min_red * min_green * min_blue
    return score


print(f'answer to assignment 1 is: {first_assignment()}')
print(f'answer to assignment 2 is: {second_assignment()}')
