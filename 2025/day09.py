from itertools import combinations


if __name__ == '__main__':
    print("Advent of Code 2025 - Day 09: Movie Theater")

    with open('day09.txt') as f:
        tiles: set[tuple[int, int]] = set()
        for line in f.read().strip().splitlines():
            x, y = line.split(',')
            tiles.add((int(x), int(y)))


    # part 1

    max_area = 0
    for (x1, y1), (x2, y2) in combinations(tiles, 2):
        length = abs(x1 - x2) + 1
        height = abs(y1 - y2) + 1
        max_area = max(max_area, length * height)

    print(f'Part 1: {max_area}') # 4715966250


    # part 2

    print(f'Part 2: {0}') #

