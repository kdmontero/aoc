import collections

print("Advent of Code 2015 - Day 18: Like a GIF For Your Yard")
with open('day18.txt') as f:
    board = f.read().splitlines()

H = len(board)
W = len(board[0])

# part 1
lights = set()
for y in range(H):
    for x in range(W):
        if board[y][x] == '#':
            lights.add((y, x))

for _ in range(100):
    lighted_n = collections.Counter()
    for y, x in lights:
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if dy == dx == 0:
                    continue
                else:
                    lighted_n[(y+dy, x+dx)] += 1

    new_light = set()
    for (y, x), value in lighted_n.items():
        if y < 0 or x < 0 or y == H or x == W:
            continue
        if value in {2, 3} and (y, x) in lights:
            new_light.add((y, x))
        elif value == 3 and (y, x) not in lights:
            new_light.add((y, x))
    lights = new_light

print(f'Part 1: {len(lights)}') # 768


# part 2
lights = {(0, 0), (H-1, 0), (0, W-1), (H-1, W-1)}
for y in range(H):
    for x in range(W):
        if board[y][x] == '#':
            lights.add((y, x))

for _ in range(100):
    lighted_n = collections.Counter()
    for y, x in lights:
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if dy == dx == 0:
                    continue
                else:
                    lighted_n[(y+dy, x+dx)] += 1

    new_light = {(0, 0), (H-1, 0), (0, W-1), (H-1, W-1)}
    for (y, x), value in lighted_n.items():
        if y < 0 or x < 0 or y == H or x == W:
            continue
        if value in {2, 3} and (y, x) in lights:
            new_light.add((y, x))
        elif value == 3 and (y, x) not in lights:
            new_light.add((y, x))
    lights = new_light

print(f'Part 2: {len(lights)}') # 781
