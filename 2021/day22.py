import re


if __name__ == '__main__':
    print("Advent of Code 2021 - Day 22: Reactor Reboot")

    with open('day22.txt') as f:
        steps = []
        pattern = re.compile(r'([-\d]+)')
        for line in f.read().strip().splitlines():
            action, coords = line.split()
            boundaries = pattern.findall(coords)
            x1, x2, y1, y2, z1, z2 = [int(num) for num in boundaries]
            steps.append([action, x1, x2, y1, y2, z1, z2])


    # part 1
    grid = [[[0] * 101 for _ in range(101)] for _ in range(101)]
    for action, x1, x2, y1, y2, z1, z2 in steps:
        x1, x2 = max(x1, -50), min(x2, 50)
        y1, y2 = max(y1, -50), min(y2, 50)
        z1, z2 = max(z1, -50), min(z2, 50)
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                for z in range(z1, z2 + 1):
                    if action == 'on':
                        grid[x+50][y+50][z+50] = 1
                    elif action == 'off':
                        grid[x+50][y+50][z+50] = 0

    turn_on = 0
    for area in grid:
        for line in area:
            turn_on += sum(line)

    print(f'Part 1: {turn_on}') # 610196


    # part 2

    print(f'Part 2: {0}') #

