from collections import Counter

with open('day17.txt') as f:
    given_active_cubes = set()
    lines = f.read().split('\n')
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] == '#':
                given_active_cubes.add((0, 0, y, x))

# part 1
active_cubes = given_active_cubes.copy()
for _ in range(6):
    dimension = Counter() # dict of pos: n, where n = active neighbors
    for (w, z, y, x) in active_cubes:    
        for zi in range(z-1, z+2):
            for yi in range(y-1, y+2):
                for xi in range(x-1, x+2):
                    if (zi, yi, xi) == (z, y, x):
                        continue
                    dimension[(w, zi, yi, xi)] += 1

    new_active_cubes = set()
    for pos, n in dimension.items():
        if n == 3:
            new_active_cubes.add(pos)

    for pos in active_cubes:
        if dimension[pos] == 2:
            new_active_cubes.add(pos)

    active_cubes = new_active_cubes
    
print(f'Part 1: {len(active_cubes)}') # 232


# part 2
active_cubes = given_active_cubes.copy()
for _ in range(6):
    dimension = Counter() # dict of pos: n, where n = active neighbors
    for (w, z, y, x) in active_cubes:
        for wi in range(w-1, w+2):
            for zi in range(z-1, z+2):
                for yi in range(y-1, y+2):
                    for xi in range(x-1, x+2):
                        if (wi, zi, yi, xi) == (w, z, y, x):
                            continue
                        dimension[(wi, zi, yi, xi)] += 1

    new_active_cubes = set()
    for pos, n in dimension.items():
        if n == 3:
            new_active_cubes.add(pos)

    for pos in active_cubes:
        if dimension[pos] == 2:
            new_active_cubes.add(pos)

    active_cubes = new_active_cubes

print(f'Part 2: {len(active_cubes)}') # 1620