import heapq as hq
from collections import defaultdict
from functools import lru_cache


if __name__ == '__main__':
    print("Advent of Code 2018 - Day 22: Mode Maze")

    with open('day22.txt') as f:
        depth_info, target_info = f.read().strip().splitlines()
        _, depth = depth_info.split()
        _, target = target_info.split()
        DEPTH = int(depth)
        target_x, target_y = [int(num) for num in target.split(',')]
        TARGET = (target_x, target_y)


    # part 1

    @lru_cache(maxsize=None)
    def geo_index(coords: tuple[int, int]) -> int:
        x, y = coords
        if coords == (0, 0) or coords == TARGET:
            return 0
        elif y == 0:
            return x * 16807
        elif x == 0:
            return y * 48271
        else:
            erosion_level_n1 = (geo_index((x - 1, y)) + DEPTH) % 20183
            erosion_level_n2 = (geo_index((x, y - 1)) + DEPTH) % 20183
            return erosion_level_n1 * erosion_level_n2

    grid = {} # {(x, y): A}, where A is the risk level
    def get_type(coords: tuple[int, int]) -> int:
        '''0: rocky, 1: wet, 2: narrow'''
        if coords in grid:
            return grid[coords]

        erosion_level = (geo_index(coords) + DEPTH) % 20183
        risk_level = erosion_level % 3
        grid[coords] = risk_level
        return risk_level


    total_risk_level = 0
    for y in range(target_y + 1):
        for x in range(target_x + 1):
            total_risk_level += get_type((x, y))

    print(f'Part 1: {total_risk_level}') # 8090


    # part 2
    # got clues from reddit:to insert upper bound on the grid (5x the target
    # seems enough), to remove limit in lru_cache, clearer implementation 
    # of djikstra

    def get_grid_4n(x: int, y: int) -> list[tuple[int, int, int]]:
        grid_n = []
        for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            nx = x + dx
            ny = y + dy

            if nx < 0 or ny < 0 or nx >= target_x * 5 or ny >= target_y * 5:
                continue

            ntype = get_type((nx, ny))
            grid_n.append([nx, ny, ntype])

        return grid_n

    # the type is matched to the invalid item of that type
    # ROCKY = NEITHER = 0
    # WET = TORCH = 1
    # NARROW = GEAR = 2

    def get_n(
        minutes: int,
        x: int,
        y: int,
        item: str
    ) -> list[tuple[int, int, int, int]]:

        neighbors = []
        cur_type = get_type((x, y))
        
        other_item_choices = {0, 1, 2} - {cur_type}
        other_item = (other_item_choices - {item}).pop()
        neighbors.append([minutes + 7, x, y, other_item])

        for nx, ny, ntype in get_grid_4n(x, y):
            if ntype != item:
                neighbors.append([minutes + 1, nx, ny, item])

        return neighbors

    # MOST CLEAR IMPLEMENTATION OF DJIKSTRA
    queue = [(0, 0, 0, 1)]
    times = defaultdict(lambda: float('inf'))
    times[(0, 0, 1)] = 0

    while True:
        current = hq.heappop(queue)
        minutes, x, y, item = current

        if (x, y, item) == (*TARGET, 1):
            break
        if times[(x, y, item)] < minutes:
            continue
        for nminutes, nx, ny, nitem in get_n(minutes, x, y, item):
            if nminutes < times[(nx, ny, nitem)]:
                hq.heappush(queue, (nminutes, nx, ny, nitem))
                times[(nx, ny, nitem)] = nminutes

    print(f'Part 2: {minutes}') # 992

