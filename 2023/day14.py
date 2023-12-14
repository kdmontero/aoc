from copy import deepcopy


if __name__ == '__main__':
    print('Advent of Code 2023 - Day 14')

    with open('s.txt') as f:
        orig_platform = []
        for row, line in enumerate(f.read().splitlines()):
            orig_platform.append(list(line))
        orig_platform = tuple(tuple(line) for line in orig_platform)
        print(orig_platform)


    def tilt_north(platform: list[list[str]]) -> list[list[str]]:
        platform = [list(line) for line in platform]
        height = len(platform)
        width = len(platform[0])
        for col in range(width):
            marker = None
            for row in range(height):
                if marker is None and platform[row][col] == '.':
                        marker = row
                        continue

                if marker is not None:
                    if platform[row][col] == '#':
                        marker = None
                    elif platform[row][col] == 'O':
                        platform[row][col] = '.'
                        platform[marker][col] = 'O'
                        for next_stone in range(marker + 1, row + 1):
                            if platform[next_stone][col] == '.':
                                marker = next_stone
                                break
        return tuple(tuple(line) for line in platform)
    
    def rotate_cw(platform: list[list[str]]) -> list[list[str]]:
        rotated = []
        for col in range(len(platform[0])):
            new_row = []
            for row in range(len(platform) - 1, -1, -1):
                new_row.append(platform[row][col])
            rotated.append(new_row)
        return tuple(tuple(line) for line in rotated)

    def rotate_ccw(platform: list[list[str]]) -> list[list[str]]:
        rotated = []
        for col in range(len(platform[0]) - 1, -1, -1):
            new_row = []
            for row in range(len(platform)):
                new_row.append(platform[row][col])
            rotated.append(new_row)
        return tuple(tuple(line) for line in rotated)

    def tilt_west(platform: list[list[str]]) -> list[list[str]]:
        platform = rotate_cw(platform)
        platform = tilt_north(platform)
        platform = rotate_ccw(platform)
        return platform

    def tilt_south(platform: list[list[str]]) -> list[list[str]]:
        platform = rotate_cw(rotate_cw(platform))
        platform = tilt_north(platform)
        platform = rotate_cw(rotate_cw(platform))
        return platform

    def tilt_east(platform: list[list[str]]) -> list[list[str]]:
        platform = rotate_ccw(platform)
        platform = tilt_north(platform)
        platform = rotate_cw(platform)
        return platform
    
    def tilt_cycle(platform: list[list[str]]) -> list[list[str]]:
        platform = tilt_north(platform)
        platform = tilt_west(platform)
        platform = tilt_south(platform)
        platform = tilt_east(platform)
        return platform

    def north_support(platform: list[list[str]]) -> int:
        total_load = 0
        height = len(platform)
        for load, row in enumerate(platform):
            for char in row:
                if char == 'O':
                    total_load += height - load
        return total_load

    
    # part 1

    platform1 = deepcopy(orig_platform)
    total_load1 = north_support(tilt_north(platform1))
    print(f'Part 1: {total_load1}') # 106378

    # a = '....O#O...OO'
    # platform.clear()
    # for i, char in enumerate(a):
    #     platform[(i, 0)] = char
    # height = i + 1
    # width = 1
    
    def print_platform(w, h):
        for y in range(h):
            s = ''
            for x in range(w):
                s += platform[(y, x)]
            print(s)

    # print_platform(width, height)

    # part 2

    platform2 = deepcopy(orig_platform)
    visited = {}
    i = 1
    while platform2 not in visited:
        platform2 = tilt_cycle(platform2)
        visited[platform2] = i
        i += 1
    first_seen = visited[platform2]
    cyclic = i - first_seen
    final_state = ((1_000_000_000 - first_seen) % cyclic) + first_seen
    for key, value in visited.items():
        if value == final_state:
            final_platform = value
            break

    print(final_platform)
    total_load2 = north_support(final_platform)

    print(f'Part 2: {total_load2}') #