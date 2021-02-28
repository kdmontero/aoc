import hashlib

print('Advent of Code 2016 - Day 17')
INPUT = 'qljzarfv'
OPEN = {'b', 'c', 'd', 'e', 'f'}
DIRECTIONS = ['U', 'D', 'L', 'R']

# part 1
queue = [[0, 0, '']]
shortest_path = ''
max_steps = 0

while queue:
    next_queue = []
    for node in queue:
        y, x, path = node

        if y == x == 3:
            if not shortest_path:
                shortest_path = path
            max_steps = max(max_steps, len(path))
            continue

        keys = hashlib.md5((INPUT + path).encode()).hexdigest()[:4]
        is_door_open = list(map(lambda x: x in OPEN, keys))
        open_doors = [door for door, key in zip(DIRECTIONS, is_door_open) if key]

        for door in open_doors:
            next_y, next_x = y, x
            if door == 'U' and y > 0:
                next_y -= 1
            elif door == 'D' and y < 3:
                next_y += 1
            elif door == 'L' and x > 0:
                next_x -= 1
            elif door == 'R' and x < 3:
                next_x += 1
            else:
                continue
            next_queue.append([next_y, next_x, path + door])

    queue = next_queue

print(f'Part 1: {shortest_path}') # DRLRDDURDR - part 1

print(f'Part 2: {max_steps}') # 500 - part 2
