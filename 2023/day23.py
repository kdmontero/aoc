from typing import Tuple, Set, Optional
from collections import defaultdict


if __name__ == '__main__':
    print("Advent of Code 2023 - Day 23: A Long Walk")

    with open('day23.txt') as f:
        grid = {}
        lines = f.read().splitlines()
        for col, line in enumerate(lines):
            for row, char in enumerate(line):
                if char != '#':
                    grid[(col,row)] = char
                    if col == 0:
                        start = (col, row)
                    elif col == len(lines) - 1:
                        end = (col, row)

    # part 1
    def find_n1(
        current: Optional[Tuple[int, int]], 
        prev: Tuple[int, int]
    ) -> Set[Tuple[int, int]]:
        y, x = current
        
        if grid[current] == '^':
            return {(y-1, x)} - {prev}
        elif grid[current] == 'v':
            return {(y+1, x)} - {prev}
        elif grid[current] == '<':
            return {(y, x-1)} - {prev}
        elif grid[current] == '>':
            return {(y, x+1)} - {prev}

        neighbors = set()
        for ny, nx in [[y-1, x], [y+1, x], [y, x-1], [y, x+1]]:
            if (ny, nx) in grid:
                neighbors.add((ny, nx))
        return neighbors - {prev}

    max_step1 = 0
    stack = [(start, None, 0, set())]
    while stack:
        current, prev, step, visited = stack.pop()
        visited.add(current)
        if current == end:
            max_step1 = max(max_step1, step)

        for neighbor in find_n1(current, prev):
            stack.append((neighbor, current, step + 1, visited))

    print(f'Part 1: {max_step1}') # 2438


    # part 2
    def find_n2(
        current: Optional[Tuple[int, int]], 
        prev: Tuple[int, int]
    ) -> Set[Tuple[int, int]]:
        y, x = current
        
        neighbors = set()
        for ny, nx in [[y-1, x], [y+1, x], [y, x-1], [y, x+1]]:
            if (ny, nx) in grid:
                neighbors.add((ny, nx))
        return neighbors - {prev}

    def find_next_intersection(
        current: Optional[Tuple[int, int]], 
        prev: Tuple[int, int]
    ) -> Tuple[int, int, int]:

        global start, end
        step = 1
        while True:
            neighbors = find_n2(current, prev)
            if len(neighbors) != 1 or current in [start, end]:
                break
            step += 1
            current, prev = neighbors.pop(), current
        return (current, step)
                
    opt_grid = defaultdict(dict)
    visited = set()
    queue = [start]
    while queue:
        new_queue = []
        for node in queue:
            if node in visited:
                continue

            neighbors = find_n2(node, None)
            for neighbor in neighbors:
                n, step = find_next_intersection(neighbor, node)
                opt_grid[node][n] = step
                opt_grid[n][node] = step
                
                if n not in visited:
                    new_queue.append(n)

            visited.add(node)
        queue = new_queue

    max_step2 = 0
    stack = [(start, None, 0, set())]
    while stack:
        current, prev, step, visited = stack.pop()
        if current in visited:
            continue
        visited.add(current)
        if current == end:
            max_step2 = max(max_step2, step)

        for neighbor, nstep in opt_grid[current].items():
            stack.append((neighbor, current, step + nstep, visited.copy()))

    print(f'Part 2: {max_step2}') # 6658
