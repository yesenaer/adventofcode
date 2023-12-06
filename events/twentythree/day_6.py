from pathlib import Path


RESOURCES_DIR = Path(__file__).parent / 'resources'


def get_distances(time: str):
    time = int(time)
    results = []
    [results.append((t, (t*(time-t)))) for t in range(time)]
    return results


def first_assignment():
    with open(RESOURCES_DIR / 'day6_input.txt') as file:
        result = 1
        time = file.readline()
        distance = file.readline()
        winners = []
        times = time.replace('Time:', '').split()
        distances = distance.replace('Distance:', '').split()

        for index, i in enumerate(times):
            times_won = 0
            results = get_distances(i)
            for j in results:
                if j[1] > int(distances[index]):
                    times_won += 1
            winners.append(times_won)

        for winner in winners:
            result *= winner

    return result


def second_assignment():
    with open(RESOURCES_DIR / 'day6_input.txt') as file:
        input_time = file.readline()
        input_distance = file.readline()
        time = input_time.replace('Time:', '').replace(' ', '')
        distance = int(input_distance.replace('Distance:', '').replace(' ', ''))
        times_won = 0
        results = get_distances(time)
        for j in results:
            if j[1] > distance:
                times_won += 1

    return times_won


print(f'answer to assignment 1 is: {first_assignment()}')
print(f'answer to assignment 2 is: {second_assignment()}')
