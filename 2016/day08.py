import collections

print('Advent of Code 2016 - Day 08')
with open('day08.txt') as f:
    instructions = []
    for line in f.read().splitlines():
        if line.startswith('rect'):
            ins, parameters = line.split(' ')
            parameters = [int(x) for x in parameters.split('x')]
        elif line.startswith('rotate row'):
            line = line.replace('rotate row y=', '')
            parameters = [int(x) for x in line.split(' by ')]
            ins = 'row'
        elif line.startswith('rotate col'):
            line = line.replace('rotate column x=', '')
            parameters = [int(x) for x in line.split(' by ')]
            ins = 'col'
        instructions.append([ins] + parameters)

def rect(screen, width, length):
    for y in range(length):
        for x in range(width):
            screen[y][x] = '#'
    return screen

def rotate_row(screen, row, shift):
    temp_row = collections.deque(screen[row])
    temp_row.rotate(shift)
    screen[row] = list(temp_row)
    return screen

def rotate_col(screen, col, shift):
    screen = [list(c) for c in zip(*screen)]
    temp_col = collections.deque(screen[col])
    temp_col.rotate(shift)
    screen[col] = list(temp_col)
    return [list(c) for c in zip(*screen)]

# part 1
screen = [[' '] * 50 for _ in range(6)]

for ins in instructions:
    if ins[0] == 'rect':
        screen = rect(screen, ins[1], ins[2])
    elif ins[0] == 'row':
        screen = rotate_row(screen, ins[1], ins[2])
    elif ins[0] == 'col':
        screen = rotate_col(screen, ins[1], ins[2])

pixel_on = 0
for line in screen:
    pixel_on += line.count('#')

print(f'Part 1: {pixel_on}') # 110


# part 2
print('Part 2:') # ZJHRKCPLYJ
for line in screen:
    print(''.join(line))
