import itertools

print("Advent of Code 2016 - Day 24: Air Duct Spelunking")

with open('day24.txt') as f:
    grid = {}
    points = []
    positions = {}
    given_grid = f.read().splitlines()
    for y in range(len(given_grid)):
        for x in range(len(given_grid[0])):
            grid[(y,x)] = given_grid[y][x]
            if given_grid[y][x] not in {'#', '.'}:
                positions[given_grid[y][x]] = (y, x)
                points.append(given_grid[y][x])

lengths = {} 
# {
#   start1: {
#       dest1: length of start1 to dest1, 
#       dest2: length of start1 to dest2,
#       ...
#       },
#   start2: {
#       dest1: length of start2 to dest1,
#       dest2: lenght of start2 to dest2,
#       ...
#       },
#   ...
# }


def neighbors(y, x):
    return [(y+1, x), (y-1, x), (y, x+1), (y, x-1)]


def add_lengths(start, destination, length):
    if start not in lengths:
        lengths[start] = {destination: length}
    else:
        lengths[start][destination] = length


def bfs(start):
    queue = {positions[start]}
    seen = set()
    steps = 0

    while queue:
        temp_queue = set()
        for node in queue:
            if node in seen:
                continue

            for adj in neighbors(*node):
                if all((
                    grid.get(adj) not in {'#', None},
                    adj not in seen,
                )):
                    temp_queue.add(adj)

                    if grid.get(adj) != '.':
                        add_lengths(start, grid.get(adj), steps + 1)
                        add_lengths(grid.get(adj), start, steps + 1)

            seen.add(node)

        steps += 1
        queue = temp_queue


def get_total_distance(path, with_return=False):
    starting = path.pop(0)
    first_start = starting
    distance = 0
    while path:
        destination = path.pop(0)
        distance += lengths[starting][destination]
        starting = destination

    if with_return:
        distance += lengths[destination][first_start]

    return distance


for point in points:
    bfs(point)

shortest_route = 100_000_000
shortest_route_return = 100_000_000

for path in itertools.permutations(lengths.keys()):
    total = get_total_distance(list(path))
    shortest_route = min(shortest_route, total)
    
    total_return = get_total_distance(list(path), True)
    shortest_route_return = min(shortest_route_return, total_return)

print(f'Part 1: {shortest_route}') # 428 - part 1
print(f'Part 2: {shortest_route_return}') # 680 - part 2
