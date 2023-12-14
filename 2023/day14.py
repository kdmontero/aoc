from copy import deepcopy
from typing import Sequence


if __name__ == '__main__':
    print('Advent of Code 2023 - Day 14')

    with open('day14.txt') as f:
        orig_platform = []
        for row, line in enumerate(f.read().splitlines()):
            orig_platform.append(list(line))

    def tilt_north(platform: list[list[str]]) -> list[list[str]]:
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
        return platform
    
    def rotate_cw(platform: list[list[str]]) -> list[list[str]]:
        rotated = []
        for col in range(len(platform[0])):
            new_row = []
            for row in range(len(platform) - 1, -1, -1):
                new_row.append(platform[row][col])
            rotated.append(new_row)
        return rotated

    def rotate_ccw(platform: list[list[str]]) -> list[list[str]]:
        rotated = []
        for col in range(len(platform[0]) - 1, -1, -1):
            new_row = []
            for row in range(len(platform)):
                new_row.append(platform[row][col])
            rotated.append(new_row)
        return rotated

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

    def get_north_load(platform: Sequence[Sequence[str]]) -> int:
        total_load = 0
        height = len(platform)
        for load, row in enumerate(platform):
            for char in row:
                if char == 'O':
                    total_load += height - load
        return total_load

    # for debugging
    def print_platform(platform: Sequence[Sequence[str]]) -> None:
        for y in range(len(platform)):
            row = ''
            for x in range(len(platform[0])):
                row += platform[y][x]
            print(row)
            
    
    # part 1

    platform1 = deepcopy(orig_platform)
    total_load1 = get_north_load(tilt_north(platform1))
    print(f'Part 1: {total_load1}') # 106378


    # part 2

    def platform_to_tuple(platform: list[list[str]]) -> tuple[tuple[str]]:
        return tuple(tuple(line) for line in platform)

    platform2 = deepcopy(orig_platform)
    visited = {}

    i = 0
    while platform_to_tuple(platform2) not in visited.values():
        visited[i] = platform_to_tuple(platform2)
        platform2 = tilt_cycle(platform2)
        i += 1

    for index, platform in visited.items():
        if platform == platform_to_tuple(platform2):
            first_repeat = index
    
    cycle = i - first_repeat
    final_state = ((1_000_000_000 - first_repeat) % cycle) + first_repeat
    final_platform = visited[final_state]

    total_load2 = get_north_load(final_platform)

    print(f'Part 2: {total_load2}') # 90795