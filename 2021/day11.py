import copy

if __name__ == '__main__':
    print('Advent of Code 2021 - Day 11')

    with open('day11.txt') as f:
        given_octopus = {}
        for y, line in enumerate(f.read().splitlines()):
            for x, octo in enumerate(line):
                given_octopus[(y, x)] = int(octo)


    # part 1

    octopus = copy.deepcopy(given_octopus)
    for_flash = []
    def get_n(y, x):
        neighbors = []
        for dy in [-1, 0, +1]:
            for dx in [-1, 0, +1]:
                if (dy, dx) == (0, 0):
                    continue
                neighbors.append((y+dy, x+dx))
        return neighbors

    def level_up():
        for octo in octopus:
            octopus[octo] += 1
            if octopus[octo] > 9:
                for_flash.append(octo)

    flashes = 0
    for _ in range(100):
        new_octopus = {}
        level_up()

        while for_flash:
            octo = for_flash.pop()
            if octo not in octopus:
                continue
            flashes += 1
            new_octopus[octo] = 0
            del octopus[octo]

            for n in get_n(*octo):
                if n in octopus:
                    octopus[n] += 1
                    if octopus[n] > 9:
                        for_flash.append(n)

        octopus.update(new_octopus)

    print(f'Part 1: {flashes}') # 1669

    
    # part 2

    octopus = copy.deepcopy(given_octopus)
    steps = 0
    while True:
        new_octopus = {}
        level_up()

        while for_flash:
            octo = for_flash.pop()
            if octo not in octopus:
                continue
            flashes += 1
            new_octopus[octo] = 0
            del octopus[octo]

            for n in get_n(*octo):
                if n in octopus:
                    octopus[n] += 1
                    if octopus[n] > 9:
                        for_flash.append(n)

        octopus.update(new_octopus)
        steps += 1
        if set(octopus.values()) == {0}:
            break

    print(f'Part 2: {steps}') # 351
