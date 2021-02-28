import time
import os

print('Advent of Code 2016 - Day 13')
INPUT = 1350
TARGET = (31, 39)
DELAY = 0.05

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

def get_char(x, y, maze):
    SPACE = '.'
    WALL = '#'
    UNDEFINED = ' '
    START = 'S'
    END = 'O'

    if (x, y) == (1, 1):
        return START
    elif (x, y) == TARGET:
        return END
    elif (x, y) not in maze:
        return UNDEFINED
    elif maze[(x, y)]:
        return SPACE
    else:
        return WALL

def print_maze(maze):
    length = max(maze, key=lambda a:a[1])[1] + 1
    width = max(maze, key=lambda a:a[0])[0] + 1
    os.system("clear")

    for y in range(length):
        for x in range(width):
            print(get_char(x, y, maze), end="")
        print('')
    
    time.sleep(DELAY)

def solve(show):
    queue = {(1,1)}
    maze = {TARGET: True}
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
                if n not in maze or n == TARGET:
                    if is_space(*n):
                        next_queue.add(n)
                    else:
                        maze[n] = False

        if show:
            print_maze(maze)

        if steps <= 50:
            count += len(next_queue)
        queue = next_queue
        steps += 1

    return found, count

show = False # set to False to hide animation, True for otherwise
found, count = solve(show)

print(f'Part 1: {found}') # 94 - part 1
print(f'Part 2: {count}') # 124 - part 2
