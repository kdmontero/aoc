import time

INPUT = 1350
TARGET = (31, 39)


def is_space(x, y):
    num = x*x + 3*x + 2*x*y + y + y*y + INPUT
    count = bin(num).lstrip('0b').count('1')
    return True if count % 2 == 0 else False

def get_neighbors(x, y):
    n = []
    for dx in [-1, 1]:
        if x+dx < 0:
            continue
        n.append((x+dx, y))
    for dy in [-1, 1]:
        if y+dy < 0:
            continue
        n.append((x, y+dy))
    return n

def print_maze(maze):
    SPACE = ' '
    WALL = '#'
    UNDEFINED = '*'

    length = max(maze, key=lambda a:a[0])[0] + 1
    width = max(maze, key=lambda a:a[1])[1] + 1
    grid = [[UNDEFINED] * width for _ in range(length)]
    for (x, y), space in maze.items():
        if space:
            grid[x][y] = SPACE
        else:
            grid[x][y] = WALL

    for line in grid:
        print(''.join(line))


queue = {(1,1)}
maze = {}
count = 0
found = False
steps = 0

while queue and (not found or steps <= 50):
    next_queue = set()

    for node in queue:
        if node == TARGET:
            found = steps

        maze[node] = is_space(*node)
        for n in get_neighbors(*node):
            if n not in maze and is_space(*n):
                next_queue.add(n)

    if steps <= 50:
        count += len(next_queue)
    queue = next_queue
    steps += 1
    continue


print(f'Part 1: {found}') # 94 - part 1

print(f'Part 2: {count}') # 124 - part 2
