import itertools

print('Advent of Code 2015 - Day 09')
with open('day09.txt') as f:
    paths = {}
    for line in f.read().splitlines():
        way, distance = line.split(' = ')
        place1, place2 = way.split(' to ')
        if place1 not in paths:
            paths[place1] = {place2: int(distance)}
        else:
            paths[place1][place2] = int(distance)
        if place2 not in paths:
            paths[place2] = {place1: int(distance)}
        else:
            paths[place2][place1] = int(distance)

def get_total_distance(path: list) -> int:
    starting = path.pop(0)
    distance = 0
    while path:
        destination = path.pop(0)
        distance += paths[starting][destination]
        starting = destination
    return distance

min_total = 100000
max_total = 0

for path in itertools.permutations(paths.keys()):
    total = get_total_distance(list(path))
    min_total = min(min_total, total)
    max_total = max(max_total, total)

print(f'Part 1: {min_total}') # 207 part 1
print(f'Part 2: {max_total}') # 804 part 2
