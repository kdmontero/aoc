import heapq as hq
import os
import time
from copy import deepcopy


if __name__ == '__main__':
    print('Advent of Code 2024 - Day 16: Reindeer Maze')

    with open('day16.txt') as f:
        tracks = set()
        start_dir = '>'
        start_y = start_x = des_y = des_x = None
        for y, line in enumerate(f.read().strip().splitlines()):
            for x, char in enumerate(line):
                if char == '#':
                    continue
                elif char == 'S':
                    start_y = y
                    start_x = x
                elif char == 'E':
                    des_y = y
                    des_x = x

                tracks.add((y, x))
    
    # part 1

    def get_n(
        steps: int,
        y: int,
        x: int,
        dir: str
    ) -> list[tuple[int, int, str, int]]:

        neighbors = []
        if dir == '^':
            if (y, x - 1) in tracks:
                neighbors.append((steps + 1000, y, x, '<'))
            if (y - 1, x) in tracks:
                neighbors.append((steps + 1, y - 1, x, dir))
            if (y, x + 1) in tracks:
                neighbors.append((steps + 1000, y, x, '>'))
        elif dir == 'v':
            if (y, x - 1) in tracks:
                neighbors.append((steps + 1000, y, x, '<'))
            if (y + 1, x) in tracks:
                neighbors.append((steps + 1, y + 1, x, dir))
            if (y, x + 1) in tracks:
                neighbors.append((steps + 1000, y, x, '>'))
        elif dir == '>':
            if (y + 1, x) in tracks:
                neighbors.append((steps + 1000, y, x, 'v'))
            if (y, x + 1) in tracks:
                neighbors.append((steps + 1, y, x + 1, dir))
            if (y - 1, x) in tracks:
                neighbors.append((steps + 1000, y, x, '^'))
        elif dir == '<':
            if (y + 1, x) in tracks:
                neighbors.append((steps + 1000, y, x, 'v'))
            if (y, x - 1) in tracks:
                neighbors.append((steps + 1, y, x - 1, dir))
            if (y - 1, x) in tracks:
                neighbors.append((steps + 1000, y, x, '^'))

        return neighbors

    visited = {}
    found_end = False
    queue = [(0, start_y, start_x, start_dir)]
    hq.heapify(queue)
    while not found_end:
        cur_steps, cur_y, cur_x, cur_dir = hq.heappop(queue)
        for nsteps, ny, nx, ndir in get_n(cur_steps, cur_y, cur_x, cur_dir):
            if (ny, nx, ndir) in visited:
                if nsteps < visited[(ny, nx, ndir)]:
                    visited[(ny, nx, ndir)] = nsteps
                else:
                    continue
            if (nsteps, ny, nx, ndir) not in queue:
                hq.heappush(queue, (nsteps, ny, nx, ndir))
        visited[(cur_y, cur_x, cur_dir)] = cur_steps
        if (cur_y, cur_x) == (des_y, des_x):
            found_end = True
            
    min_score = cur_steps
    print(f'Part 1: {min_score}') # 115500


    # part 2


    print(f'Part 2: {0}') #

