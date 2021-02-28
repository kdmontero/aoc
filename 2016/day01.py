from collections import deque

print('Advent of Code 2016 - Day 01')
with open('day01.txt') as f:
    doc = f.read().split(', ')

def change_dir(turn):
    if turn == 'R':
        directions.rotate(-1)
    elif turn == 'L':
        directions.rotate(1)
    return directions[0]

def change_pos(move, cur_dir):
    if cur_dir == 'N':
        cur_pos[1] += move
    elif cur_dir == 'S':
        cur_pos[1] -= move
    elif cur_dir == 'E':
        cur_pos[0] += move
    elif cur_dir == 'W':
        cur_pos[0] -= move

directions = deque(['N', 'E', 'S', 'W'])
cur_pos = [0,0]
visited = {(0,0)}
found = None

for ins in doc:
    cur_dir = change_dir(ins[0])
    for _ in range(int(ins[1:])):
        change_pos(1, cur_dir)
        if tuple(cur_pos) in visited and not found:
            found = cur_pos[:]
        elif tuple(cur_pos) not in visited and not found:
            visited.add(tuple(cur_pos))

print(f'Part 1: {abs(cur_pos[0]) + abs(cur_pos[1])}') # 246 - part 1
print(f'Part 2: {abs(found[0]) + abs(found[1])}') # 124 - part 2
