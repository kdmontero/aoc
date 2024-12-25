from collections import defaultdict
from itertools import combinations


if __name__ == '__main__':
    print("Advent of Code 2024 - Day 08: Resonant Collinearity")

    with open('day08.txt') as f:
        scan = defaultdict(set)
        for y, line in enumerate(f.read().strip().splitlines()):
            for x, char in enumerate(line):
                if char == '.':
                    continue
                scan[char].add((y, x))

        height, width = y, x


    antinodes_part1 = set()
    antinodes_part2 = set()
    for antennas in scan.values():
        for (ante1y, ante1x), (ante2y, ante2x) in combinations(antennas, 2):
            rise = ante2y - ante1y
            run = ante2x - ante1x
            antinodes_part2.add((ante1y, ante1x))
            antinodes_part2.add((ante2y, ante2x))

            antinode1y = ante1y - rise
            antinode1x = ante1x - run
            antinode2y = ante2y + rise
            antinode2x = ante2x + run

            if 0 <= antinode1y <= height and 0 <= antinode1x <= width:
                antinodes_part1.add((antinode1y, antinode1x))

            if 0 <= antinode2y <= height and 0 <= antinode2x <= width:
                antinodes_part1.add((antinode2y, antinode2x))

            while (0 <= antinode1y <= height) and (0 <= antinode1x <= width):
                antinodes_part2.add((antinode1y, antinode1x))
                antinode1y = antinode1y - rise
                antinode1x = antinode1x - run

            while (0 <= antinode2y <= height) and (0 <= antinode2x <= width):
                antinodes_part2.add((antinode2y, antinode2x))
                antinode2y = antinode2y + rise
                antinode2x = antinode2x + run

    print(f'Part 1: {len(antinodes_part1)}') # 329

    print(f'Part 2: {len(antinodes_part2)}') # 1190

