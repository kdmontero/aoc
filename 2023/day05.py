from typing import List

class Converter:
    def __init__(self, conversion: List[List[int]]) -> None:
        arranged = []
        for dest, source, range_ in conversion:
            arranged.append([source, dest, range_])
        arranged.sort()
        self.conversion = arranged

    def convert(self, num: int) -> int:
        for source, dest, range_ in self.conversion:
            if source > num:
                return num
            if num in range(source, source + range_):
                return num - source + dest
        return num


if __name__ == '__main__':
    print('Advent of Code 2023 - Day 05')

    with open('day05.txt') as f:
        s, map1, map2, map3, map4, map5, map6, map7 = f.read().split('\n\n')

    seeds = [int(num) for num in s.split()[1:]]
    seed_soil = Converter(
        [[int(num) for num in line.split()]
        for line in map1.splitlines()[1:]]
    )
    soil_fert = Converter(
        [[int(num) for num in line.split()]
        for line in map2.splitlines()[1:]]
    )
    fert_water = Converter(
        [[int(num) for num in line.split()]
        for line in map3.splitlines()[1:]]
    )
    water_light = Converter(
        [[int(num) for num in line.split()]
        for line in map4.splitlines()[1:]]
    )
    light_temp = Converter(
        [[int(num) for num in line.split()]
        for line in map5.splitlines()[1:]]
    )
    temp_humid = Converter(
        [[int(num) for num in line.split()]
        for line in map6.splitlines()[1:]]
    )
    humid_loc = Converter(
        [[int(num) for num in line.split()]
        for line in map7.splitlines()[1:]]
    )

    def seed_to_location(seed: int) -> int:
        soil = seed_soil.convert(seed)
        fert = soil_fert.convert(soil)
        water = fert_water.convert(fert)
        light = water_light.convert(water)
        temp = light_temp.convert(light)
        humid = temp_humid.convert(temp)
        loc = humid_loc.convert(humid)
        return loc

    # part 1

    locations = []
    for seed in seeds:
        locations.append(seed_to_location(seed))


    print(f'Part 1: {min(locations)}') # 662197086


    # part 2

    min_location = 999_999_999_999_999
    '''
    for i in range(0, len(seeds), 2):
        start, range_ = seeds[i], seeds[i+1]
        print(i, start, range_)
        for seed in range(start, start + range_):
            min_location = min(min_location, seed_to_location(seed))
    '''
    
    print(f'Part 2: {min_location}') #
