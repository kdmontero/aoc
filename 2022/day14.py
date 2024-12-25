import copy

if __name__ == '__main__':
    print("Advent of Code 2022 - Day 14: Regolith Reservoir")

    with open('day14.txt') as f:
        cave = {}
        depth = 0
        for line in f.read().splitlines():
            corners = line.split(' -> ')
            for i in range(len(corners) - 1):
                start, end = corners[i], corners[i+1]
                start_x, start_y = [int(num) for num in start.split(',')]
                end_x, end_y = [int(num) for num in end.split(',')]
                depth = max(depth, end_y, start_y)

                if start_x == end_x:
                    if start_y < end_y:
                        for y in range(start_y, end_y+1):
                            cave[(start_x, y)] = '#'
                    else:
                        for y in range(end_y, start_y+1):
                            cave[(start_x, y)] = '#'

                elif start_y == end_y:
                    if start_x < end_x:
                        for x in range(start_x, end_x+1):
                            cave[(x, start_y)] = '#'
                    else:
                        for x in range(end_x, start_x+1):
                            cave[(x, start_y)] = '#'


    # part 1

    cave1 = copy.deepcopy(cave)
    sand_count1 = 0
    endless = False
    sand_count1 = 0
    endless = False

    while not endless:
        cur_x, cur_y = 500, 0
        while True:
            if cur_y > depth:
                endless = True
                break
            if cave1.get((cur_x, cur_y+1)) is None:
                cur_x, cur_y = cur_x, cur_y+1
                continue
            if cave1.get((cur_x-1, cur_y+1)) is None:
                cur_x, cur_y = cur_x-1, cur_y+1
                continue
            if cave1.get((cur_x+1, cur_y+1)) is None:
                cur_x, cur_y = cur_x+1, cur_y+1
                continue

            cave1[(cur_x, cur_y)] = 'o'
            sand_count1 += 1
            break

    print(f'Part 1: {sand_count1}') # 638


    # part 2

    cave2 = copy.deepcopy(cave)
    left_bound = 500 - (depth + 3)
    right_bound = 500 + (depth + 3)
    for x in range(left_bound, right_bound+1):
        cave2[(x, depth+2)] = '#'
    sand_count2 = 0
    filled = False

    while not filled:
        cur_x, cur_y = 500, 0
        while True:
            if cave2.get((cur_x, cur_y+1)) is None:
                cur_x, cur_y = cur_x, cur_y+1
                continue
            if cave2.get((cur_x-1, cur_y+1)) is None:
                cur_x, cur_y = cur_x-1, cur_y+1
                continue
            if cave2.get((cur_x+1, cur_y+1)) is None:
                cur_x, cur_y = cur_x+1, cur_y+1
                continue

            sand_count2 += 1
            cave2[(cur_x, cur_y)] = 'o'
            if (cur_x, cur_y) == (500, 0):
                filled = True
                break
            break

    print(f'Part 2: {sand_count2}') # 31722
