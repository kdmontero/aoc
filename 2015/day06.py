print("Advent of Code 2015 - Day 06: Probably a Fire Hazard")
with open('day06.txt') as f:
    instructions = []
    for ins in list(f.read().splitlines()):
        temp = []
        if ins.startswith('turn on'):
            temp.append('on')
        elif ins.startswith('turn off'):
            temp.append('off')
        elif ins.startswith('toggle'):
            temp.append('toggle')
        ins = ins.replace('turn on ', '').replace('turn off ', ''
            ).replace('toggle ', '')
        corner1, corner2 = [[int(num) for num in corner.split(',')] 
            for corner in ins.split(' through ')]
        temp.append(corner1)
        temp.append(corner2)
        instructions.append(temp)


# part 1
display = [[0]*1000 for _ in range(1000)]
for ins in instructions:
    action, start, end = ins
    if action == 'on':
        for y in range(start[0], end[0]+1):
            for x in range(start[1], end[1]+1):
                display[y][x] = 1
    elif action == 'off':
        for y in range(start[0], end[0]+1):
            for x in range(start[1], end[1]+1):
                display[y][x] = 0
    elif action == 'toggle':
        for y in range(start[0], end[0]+1):
            for x in range(start[1], end[1]+1):
                display[y][x] = int(not(display[y][x]))

lighted1 = 0
for line in display:
    lighted1 += sum(line)

print(f'Part 1: {lighted1}') # 400410


# part 2
display = [[0]*1000 for _ in range(1000)]
for ins in instructions:
    action, start, end = ins
    if action == 'on':
        for y in range(start[0], end[0]+1):
            for x in range(start[1], end[1]+1):
                display[y][x] += 1
    elif action == 'off':
        for y in range(start[0], end[0]+1):
            for x in range(start[1], end[1]+1):
                display[y][x] = max(0, display[y][x]-1)
    elif action == 'toggle':
        for y in range(start[0], end[0]+1):
            for x in range(start[1], end[1]+1):
                display[y][x] += 2

lighted2 = 0
for line in display:
    lighted2 += sum(line)

print(f'Part 2: {lighted2}') # 15343601
