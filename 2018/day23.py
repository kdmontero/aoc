import re


if __name__ == '__main__':
    print("Advent of Code 2018 - Day 23: Experimental Emergency Teleportation")

    with open('day23.txt') as f:
        max_r = 0
        strongest = None
        nanobots = {}
        pattern = re.compile(r'(-?\d+)')

        for i, line in enumerate(f.read().strip().splitlines()):
            nums = pattern.findall(line)
            x, y, z, r = [int(num) for num in nums]
            nanobots[i] = [x, y, z, r]

            if max_r < r:
                max_r = r
                strongest = i


    # part 1

    max_x, max_y, max_z, max_r = nanobots[strongest]

    count = 0
    for i, nanobot in nanobots.items():
        x, y, z, _ = nanobot
        if abs(max_x - x) + abs(max_y - y) + abs(max_z - z) <= max_r:
            count += 1

    print(f'Part 1: {count}') # 319


    # part 2

    print(f'Part 2: {0}') #

