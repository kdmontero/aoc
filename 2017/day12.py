print('Advent of Code 2017 - Day 12')

with open('day12.txt') as f:
    pipes = {}
    for line in f.read().splitlines():
        key, values = line.split(' <-> ')
        connections = [int(v) for v in values.split(', ')]
        pipes[int(key)] = connections


# part 1

def programs_with(pipe_num):
    visited = set()
    queue = {pipe_num}

    while queue:
        temp_queue = set()
        for pipe in queue:
            for connection in pipes[pipe]:
                if connection not in visited:
                    temp_queue.add(connection)
            visited.add(pipe)
        queue = temp_queue
    return visited

print(f'Part 1: {len(programs_with(0))}') # 141


# part 2

groups = 0
overall_visited = set()

for pipe in pipes:
    if pipe not in overall_visited:
        overall_visited |= programs_with(pipe)
        groups += 1

print(f'Part 2: {groups}') # 171
