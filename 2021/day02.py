if __name__ == '__main__':
    print('Advent of Code 2021 - Day 02')

    with open('day02.txt') as f:
        commands = []
        for line in f.read().splitlines():
            command, step = line.split()
            commands.append([command, int(step)])

    # part 1

    horizontal1, depth1 = 0, 0
    for direction, step in commands:
        if direction == 'forward':
            horizontal1 += step
        elif direction == 'up':
            depth1 -= step
        elif direction == 'down':
            depth1 += step

    print(f'Part 1: {horizontal1 * depth1}') # 1855814


    # part 2

    horizontal2, depth2, aim = 0, 0, 0
    for direction, step in commands:
        if direction == 'forward':
            horizontal2 += step
            depth2 += aim * step
        elif direction == 'up':
            aim -= step
        elif direction == 'down':
            aim += step

    print(f'Part 2: {horizontal2 * depth2}') # 1845455714
