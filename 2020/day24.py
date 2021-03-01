from collections import Counter

print('Advent of Code 2020 - Day 24')
with open('day24.txt') as f:
    instructions = [ins for ins in f.read().splitlines()]

# part 1
def parser(instruction):
    directions = []
    i = 0
    while i < len(instruction):
        if instruction[i] in {'e', 'w'}:
            directions.append(instruction[i])
            i += 1
        elif instruction[i] in {'s', 'n'}:
            directions.append(instruction[i:i+2])
            i += 2
    return(directions)

def move(y, x, step):
    if step == 'e':
        x += 2
    elif step == 'w':
        x -= 2
    elif step == 'ne':
        y -= 1
        x += 1
    elif step == 'nw':
        y -= 1
        x -= 1
    elif step == 'se':
        y += 1
        x += 1
    elif step == 'sw':
        y += 1
        x -= 1
    return y, x

black = set()
for ins in instructions:
    y, x = 0, 0
    for step in parser(ins):
        y, x = move(y, x, step)
    if (y, x) not in black:
        black.add((y, x))
    else:
        black.remove((y, x))

print(f'Part 1: {len(black)}') # 287


# part 2
for _ in range(100):
    floor = Counter()
    for tile in black:
        y, x = tile
        floor[(y, x+2)] += 1
        floor[(y, x-2)] += 1
        floor[(y+1, x+1)] += 1
        floor[(y-1, x-1)] += 1
        floor[(y+1, x-1)] += 1
        floor[(y-1, x+1)] += 1
    
    new_black = set()
    for tile, n in floor.items():
        if n == 2:
            new_black.add(tile)
    
    for tile in black:
        if floor[tile] == 1:
            new_black.add(tile)
    black = new_black

print(f'Part 2: {len(black)}') # 3636
