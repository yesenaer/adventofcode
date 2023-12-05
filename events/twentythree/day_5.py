from pathlib import Path


RESOURCES_DIR = Path(__file__).parent / 'resources'


class Seed:
    id: int
    soil: int
    fertilizer: int
    water: int
    light: int
    temperature: int
    humidity: int
    location: int

    def __init__(self, id: int):
        self.id = id
        self.soil = -1
        self.fertilizer = -1
        self.water = -1
        self.light = -1
        self.temperature = -1
        self.humidity = -1
        self.location = -1

    def find_linked_value(self, key: str, mapping: dict):
        key = key.strip()
        result = None
        if key not in vars(self):
            raise Exception(f'{key} is not a var in this class')

        x = {'soil': self.id, 'fertilizer': self.soil, 'water': self.fertilizer, 'light': self.water, 'temperature': self.light, 'humidity': self.temperature, 'location': self.humidity}

        for index, value in enumerate(mapping['source_start']):
            if x[key] == value:
                direct_result = mapping['dest_start'][index]
                self.__setattr__(key, direct_result)
                break
            elif x[key] >= value and x[key] <= (value + (mapping['range'][index]-1)):
                # print(f'{self.id} in range {mapping["source_start"][index]} and {mapping["range"][index]}')
                diff = x[key] - value

                c_result = mapping['dest_start'][index] + diff
                # print(f' {x[key]} {key} {mapping["dest_start"][index]}  {diff=} {c_result}')
                # print(f'setting {key} as {c_result=}')
                self.__setattr__(key, c_result)
                break
        # exactly same as id
            else:
                key_result = x[key]
                # print(f'key result {key_result}')
                self.__setattr__(key, key_result)

#
# some_seed = Seed(55)
# some_seed.find_linked_value('light', {'dest_start': [50, 52], 'source_start': [98, 50], 'range': [2, 48]})
def first_assignment():
    with open(RESOURCES_DIR / 'day5_input.txt') as file:
        seeds_line = file.readline().replace('seeds:', '')
        seeds_list = [Seed(int(x)) for x in seeds_line.split()]
        mappings = {}
        current_map = ''
        for line in file:
            line = line.strip()
            if not line:
                continue
            if ' map:' in line:
                name = line.replace(' map:', '')
                current_map = name
                mappings[current_map] = {'dest_start': [], 'source_start': [], 'range': [] }
            else:
                splits = line.split()
                mappings[current_map]['dest_start'].append(int(splits[0]))
                mappings[current_map]['source_start'].append(int(splits[1]))
                mappings[current_map]['range'].append(int(splits[2]))

        total = calculate_lowest_location(mappings, seeds_list)
    return total


def calculate_lowest_location(mappings, seeds_list):
    total = 10000000000000000000
    for seed in seeds_list:
        for map in mappings:
            map_name = map.split('-')[2]
            seed.find_linked_value(key=map_name, mapping=mappings[map])
            if map_name == 'location':
                if seed.location < total:
                    total = seed.location

        # print(vars(seed))
    return total


def second_assignment():
    with open(RESOURCES_DIR / 'day5_input.txt') as file:
        seeds_line = file.readline().replace('seeds:', '')
        seeds_list = []
        splits = seeds_line.split()
        for index, j in enumerate(splits):
            if index % 2 == 0:
                print(f'{index} -> {j}')
                for i in range(int(j), int(j)+int(splits[index+1])):
                    seeds_list.append(Seed(int(i)))


        mappings = {}
        current_map = ''
        for line in file:
            line = line.strip()
            if not line:
                continue
            if ' map:' in line:
                name = line.replace(' map:', '')
                current_map = name
                mappings[current_map] = {'dest_start': [], 'source_start': [], 'range': [] }
            else:
                splits = line.split()
                mappings[current_map]['dest_start'].append(int(splits[0]))
                mappings[current_map]['source_start'].append(int(splits[1]))
                mappings[current_map]['range'].append(int(splits[2]))
        total = calculate_lowest_location(mappings, seeds_list)
    return total


# print(f'answer to assignment 1 is: {first_assignment()}')  # 30692976 is too low
print(f'answer to assignment 2 is: {second_assignment()}')
