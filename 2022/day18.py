if __name__ == '__main__':
    print('Advent of Code 2022 - Day 18')

    with open('day18.txt') as f:
        cubes = []
        for line in f.read().splitlines():
            x, y, z = [int(i) for i in line.split(',')]
            cubes.append([x, y, z])

    surface_area = 0
    for cube in cubes:
        x, y, z = cube
        for i in [-1, +1]:
            if [x+1, y, z] not in cubes:
                surface_area += 1
            if [x, y+1, z] not in cubes:
                surface_area += 1
            if [x, y, z+1] not in cubes:
                surface_area += 1

    print(f'Part 1: {surface_area}') # 3412


    print(f'Part 2: {0}') #
