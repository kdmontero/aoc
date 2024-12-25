from typing import Optional
from copy import deepcopy


if __name__ == '__main__':
    print("Advent of Code 2023 - Day 13: Point of Incidence")

    with open('day13.txt') as f:
        patterns = []
        for raw_given in f.read().split('\n\n'):
            pattern = []
            for line in raw_given.splitlines():
                pattern.append(list(line))
            patterns.append(pattern)
    
    def find_h_mirror(pattern: list[list[str]], skip: Optional[int] = -1):
        length = len(pattern)
        for mirror in range(length - 1):
            if skip == mirror:
                continue
            for up, down in zip(range(mirror, -1, -1), range(mirror+1, length)):
                if pattern[up] != pattern[down]:
                    break
            else:
                return mirror + 1
        return 0
    
    def find_v_mirror(pattern: list[list[str]], skip: Optional[int] = -1):
        transposed = [list(col) for col in zip(*pattern)]
        return find_h_mirror(transposed, skip=skip)
    
    
    # part 1

    summarize1 = 0
    v_mirrors = []
    h_mirrors = []
    for pattern in patterns:
        h_mirror = find_h_mirror(pattern)
        v_mirror = find_v_mirror(pattern)
        h_mirrors.append(h_mirror)
        v_mirrors.append(v_mirror)
        summarize1 += (h_mirror * 100) + v_mirror

    print(f'Part 1: {summarize1}') # 30575


    # part 2

    summarize2 = 0
    for pattern, vm, hm in zip(patterns, v_mirrors, h_mirrors):
        for row, line in enumerate(pattern):
            if row == hm - 1:
                continue
            for col, char in enumerate(line):
                if col == vm - 1:
                    continue

                pattern_copy = deepcopy(pattern)
                if char == '.':
                    pattern_copy[row][col] = '#'
                elif char == '#':
                    pattern_copy[row][col] = '.'
                
                v_mirror = find_v_mirror(pattern_copy, vm - 1)
                h_mirror = find_h_mirror(pattern_copy, hm - 1)
                if v_mirror + h_mirror > 0:
                    summarize2 += (h_mirror * 100) + v_mirror
                    break
            else:
                continue
            break
        
    print(f'Part 2: {summarize2}') # 37478