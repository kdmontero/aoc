from copy import deepcopy

print("Advent of Code 2020 - Day 11: Seating System")
with open('day11.txt') as f:
    original = {}
    lines = [line for line in f.read().split('\n')]
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            original[(y, x)] = lines[y][x]

# part 1
layout = deepcopy(original)
def get_adjacent1(y, x):
    a = layout.get((y-1, x-1))
    c = layout.get((y-1, x+1))
    d = layout.get((y, x-1))
    b = layout.get((y-1, x))
    e = layout.get((y, x+1))
    f = layout.get((y+1, x-1))
    g = layout.get((y+1, x))
    h = layout.get((y+1, x+1))
    return [a,b,c,d,e,f,g,h]

def reposition(y, x, get_adjacent, seats_to_empty):
    if layout[(y, x)] in {'#','L'}:
        adjacents = get_adjacent(y,x)
        if layout[(y, x)] == 'L' and '#' not in adjacents:
            new_layout[(y, x)] = '#'
        elif layout[(y, x)] == '#' and adjacents.count('#') >= seats_to_empty:
            new_layout[(y, x)] = 'L'
        else:
            new_layout[(y, x)] = layout[(y, x)]
        if new_layout[(y, x)] == '#':
            return 1
    else:
        new_layout[(y, x)] = layout[(y, x)]
    return 0

new_layout = {}
stabilized = False
while not stabilized:
    occupied1 = 0
    for grid in layout:
        occupied1 += reposition(*grid, get_adjacent1, 4)
    if new_layout == layout:
        stabilized = True
    else:
        layout = new_layout
        new_layout = {}

print(f'Part 1: {occupied1}') # 2319


# part 2
def check_N(y, x):
    N = layout.get((y-1, x))
    return N if N != '.' else check_N(y-1, x)

def check_S(y, x):
    S = layout.get((y+1, x))
    return S if S != '.' else check_S(y+1, x)

def check_E(y, x):
    E = layout.get((y, x+1))
    return E if E != '.' else check_E(y, x+1)

def check_W(y, x):
    W = layout.get((y, x-1))
    return W if W != '.' else check_W(y, x-1)

def check_NW(y, x):
    NW = layout.get((y-1, x-1))
    return NW if NW != '.' else check_NW(y-1, x-1)

def check_NE(y, x):
    NE = layout.get((y-1, x+1))
    return NE if NE != '.' else check_NE(y-1, x+1)

def check_SE(y, x):
    SE = layout.get((y+1, x+1))
    return SE if SE != '.' else check_SE(y+1, x+1)

def check_SW(y, x):
    SW = layout.get((y+1, x-1))
    return SW if SW != '.' else check_SW(y+1, x-1)

def get_adjacent2(y, x):
    a = check_N(y, x)
    b = check_E(y, x)
    c = check_S(y, x)
    d = check_W(y, x)
    e = check_NE(y, x)
    f = check_SE(y, x)
    g = check_SW(y, x)
    h = check_NW(y, x)
    return [a,b,c,d,e,f,g,h]

layout = deepcopy(original)
new_layout = {}
stabilized = False
while not stabilized:
    occupied2 = 0
    for grid in layout:
        occupied2 += reposition(*grid, get_adjacent2, 5)
    if new_layout == layout:
        stabilized = True
    else:
        layout = new_layout
        new_layout = {}

print(f'Part 2: {occupied2}') # 2117
