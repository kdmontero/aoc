import heapq as hq
from collections import defaultdict
from collections.abc import Mapping


if __name__ == '__main__':
    print("Advent of Code 2022 - Day 24: Blizzard Basin")

    with open('day24.txt') as f:
        walkable = set()
        init_blizz = defaultdict(str)
        START = END = None
        for y, line in enumerate(f.read().strip().splitlines()):
            for x, char in enumerate(line):
                if char == '#':
                    continue
                walkable.add((y, x))

                if START is None:
                    START = (y, x)
                END = (y, x)

                if char in '^v<>':
                    init_blizz[(y, x)] += char
        LENGTH = y - 1
        WIDTH = x - 1

    bstates = {0: init_blizz}
    
    def get_next_state(
        blizzards: Mapping[tuple[int, int], str]
    ) -> Mapping[tuple[int, int], str]:

        next_blizzards = defaultdict(str)
        for (y, x), blizzard in blizzards.items():
            for dir in blizzard:
                if dir == '^':
                    ny = ((((y - 1) - 1) + LENGTH) % LENGTH) + 1
                    nx = x
                elif dir == 'v':
                    ny = ((((y - 1) + 1) + LENGTH) % LENGTH) + 1
                    nx = x
                elif dir == '<':
                    ny = y
                    nx = ((((x - 1) - 1) + WIDTH) % WIDTH) + 1
                elif dir == '>':
                    ny = y
                    nx = ((((x - 1) + 1) + WIDTH) % WIDTH) + 1

                next_blizzards[(ny, nx)] += dir

        return next_blizzards

    def get_bliz_state(
        iteration: int,
    ) -> Mapping[tuple[int, int], str]:

        if iteration in bstates:
            return bstates[iteration]

        max_state = max(bstates)
        blizzards = bstates[max_state]

        for i in range(max_state + 1, iteration + 1):
            blizzards = get_next_state(blizzards)
            bstates[i] = blizzards

        return blizzards

    def get_n(minutes: int, y: int, x: int) -> list[tuple[int, int, int]]:
        neighbors = []
        blizzard = get_bliz_state(minutes + 1)

        for dy in range(-1, 2):
            for dx in range(-1, 2):
                if dy != 0 and dx != 0:
                    continue
                ny = y + dy
                nx = x + dx

                if (ny, nx) not in walkable:
                    continue

                if blizzard[(ny, nx)] == '':
                    neighbors.append((minutes + 1, ny, nx))

        return neighbors

    def get_min_time(
        start_time: int,
        start_pos: tuple[int, int],
        end_pos: tuple[int, int]
    ) -> int:

        dist = defaultdict(lambda: float('inf'))
        dist[(start_time, *start_pos)] = 0
        heap = [(start_time, *start_pos)]
        while heap:
            minutes, y, x = hq.heappop(heap)
            if (y, x) == end_pos:
                return minutes

            for nminutes, ny, nx in get_n(minutes, y, x):
                if dist[(nminutes, ny, nx)] > nminutes:
                    dist[(nminutes, ny, nx)] = nminutes
                    hq.heappush(heap, (nminutes, ny, nx))

    time1 = get_min_time(0, START, END)
    print(f'Part 1: {time1}') # 260

    time2 = get_min_time(time1, END, START)
    time3 = get_min_time(time2, START, END)
    print(f'Part 2: {time3}') # 747

