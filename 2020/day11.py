from copy import deepcopy

with open('day11.txt') as f:
    original = {}
    lines = [line for line in f.read().split('\n')]
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            original[(y, x)] = lines[y][x]

# part 1
layout = deepcopy(original)
def reposition1(y, x):
    if layout[(y, x)] in {'#','L'}:
        a = layout[(y-1, x-1)] if (y-1, x-1) in layout else '.'
        b = layout[(y-1, x)] if (y-1, x) in layout else '.'
        c = layout[(y-1, x+1)] if (y-1, x+1) in layout else '.'
        d = layout[(y, x-1)] if (y, x-1) in layout else '.'
        e = layout[(y, x+1)] if (y, x+1) in layout else '.'
        f = layout[(y+1, x-1)] if (y+1, x-1) in layout else '.'
        g = layout[(y+1, x)] if (y+1, x) in layout else '.'
        h = layout[(y+1, x+1)] if (y+1, x+1) in layout else '.'
        adjacent = [a,b,c,d,e,f,g,h]
        if layout[(y, x)] == 'L' and '#' not in adjacent:
            new_layout[(y, x)] = '#'
        elif layout[(y, x)] == '#' and adjacent.count('#') >= 4:
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
        occupied1 += reposition1(*grid)
    if new_layout == layout:
        stabilized = True
    else:
        layout = new_layout
        new_layout = {}

print(f'Part 1: {occupied1}')


# part 2
def check_N(y, x):
    while True:
        try:
            N = layout[(y-1, x)]
            if N in {'#', 'L'}:
                return N
            else:
                y -= 1
        except:
            return '.'

def check_S(y, x):
    while True:
        try:
            S = layout[(y+1, x)]
            if S in {'#', 'L'}:
                return S
            else:
                y += 1
        except:
            return '.'

def check_E(y, x):
    while True:
        try:
            E = layout[(y, x+1)]
            if E in {'#', 'L'}:
                return E
            else:
                x += 1
        except:
            return '.'

def check_W(y, x):
    while True:
        try:
            W = layout[(y, x-1)]
            if W in {'#', 'L'}:
                return W
            else:
                x -= 1
        except:
            return '.'

def check_NW(y, x):
    while True:
        try:
            NW = layout[(y-1, x-1)]
            if NW in {'#', 'L'}:
                return NW
            else:
                x, y = x-1, y-1
        except:
            return '.'

def check_NE(y, x):
    while True:
        try:
            NE = layout[(y-1, x+1)]
            if NE in {'#', 'L'}:
                return NE
            else:
                x, y = x+1, y-1
        except:
            return '.'

def check_SE(y, x):
    while True:
        try:
            SE = layout[(y+1, x+1)]
            if SE in {'#', 'L'}:
                return SE
            else:
                x, y = x+1, y+1
        except:
            return '.'

def check_SW(y, x):
    while True:
        try:
            SW = layout[(y+1, x-1)]
            if SW in {'#', 'L'}:
                return SW
            else:
                x, y = x-1, y+1
        except:
            return '.'

def reposition2(y, x):
    a = check_N(y, x)
    b = check_E(y, x)
    c = check_S(y, x)
    d = check_W(y, x)
    e = check_NE(y, x)
    f = check_SE(y, x)
    g = check_SW(y, x)
    h = check_NW(y, x)
    adjacent = [a,b,c,d,e,f,g,h]
    if layout[(y, x)] == 'L' and '#' not in adjacent:
        new_layout[(y, x)] = '#'
    elif layout[(y, x)] == '#' and adjacent.count('#') >= 5:
        new_layout[(y, x)] = 'L'
    else:
        new_layout[(y, x)] = layout[(y, x)]
    if new_layout[(y, x)] == '#':
        return 1
    return 0

layout = deepcopy(original)
new_layout = {}
stabilized = False
while not stabilized:
    occupied2 = 0
    for grid in layout:
        occupied2 += reposition2(*grid)
    if new_layout == layout:
        stabilized = True
    else:
        layout = new_layout
        new_layout = {}

print(f'Part 2: {occupied2}')