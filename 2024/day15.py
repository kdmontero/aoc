import os
import time


if __name__ == '__main__':
    print('Advent of Code 2024 - Day 15: Warehouse Woes')

    with open('day15.txt') as f:
        map_, ins = f.read().strip().split('\n\n')
        instructions = ins.replace('\n', '')

    def print_grid(grid: list[list[str]]) -> None:
        map_ = [''.join(line) for line in grid]
        print(*map_, sep='\n')

    def get_gps(grid: list[list[str]]) -> int:
        gps = 0
        for y, line in enumerate(grid):
            for x, obj in enumerate(line):
                if obj in 'O[':
                    gps += y * 100 + x
        return gps


    # part 1

    grid1 = [list(line.strip()) for line in map_.splitlines()]

    for y, line in enumerate(grid1):
        for x, obj in enumerate(line):
            if obj == '@':
                cur_y, cur_x = y, x

    def move1(y: int, x: int, dir: str) -> bool:
        obj = grid1[y][x]
        if obj == '#':
            return False
        elif obj == '.':
            return True
            
        if dir == '^':
            if move1(y - 1, x, dir):
                grid1[y][x] = '.'
                grid1[y - 1][x] = obj
                return True
        elif dir == 'v':
            if move1(y + 1, x, dir):
                grid1[y][x] = '.'
                grid1[y + 1][x] = obj
                return True
        elif dir == '>':
            if move1(y, x + 1, dir):
                grid1[y][x] = '.'
                grid1[y][x + 1] = obj
                return True
        elif dir == '<':
            if move1(y, x - 1, dir):
                grid1[y][x] = '.'
                grid1[y][x - 1] = obj
                return True

        return False

    for instruction in instructions:
        if move1(cur_y, cur_x, instruction):
            if instruction == '^':
                cur_y -= 1
            elif instruction == 'v':
                cur_y += 1
            elif instruction == '<':
                cur_x -= 1
            elif instruction == '>':
                cur_x += 1

    print(f'Part 1: {get_gps(grid1)}') # 1318523


    # part 2

    grid2 = []
    for line in map_.splitlines():
        big_line = []
        for char in line:
            if char == '#':
                big_line += ['#', '#']
            elif char == 'O':
                big_line += ['[', ']']
            elif char == '.':
                big_line += ['.', '.']
            elif char == '@':
                big_line += ['@', '.']
        grid2.append(big_line)

    for y, line in enumerate(grid2):
        for x, obj in enumerate(line):
            if obj == '@':
                cur_y, cur_x = y, x

    def move2(y: int, x: int, dir: str) -> bool:
        obj = grid2[y][x]
        if obj == '#':
            return False
        elif obj == '.':
            return True
            
        if dir == '^':
            if obj == '[':
                if move2(y - 1, x, dir) and move2(y - 1, x + 1, dir):
                    grid2[y - 1][x] = obj
                    grid2[y - 1][x + 1] = ']'
                    grid2[y][x] = '.'
                    grid2[y][x + 1] = '.'
                    return True
            elif obj == ']':
                if move2(y - 1, x, dir) and move2(y - 1, x - 1, dir):
                    grid2[y - 1][x] = obj
                    grid2[y - 1][x - 1] = '['
                    grid2[y][x] = '.'
                    grid2[y][x - 1] = '.'
                    return True
            elif obj == '@':
                if move2(y - 1, x, dir):
                    grid2[y][x] = '.'
                    grid2[y - 1][x] = obj
                    return True
        elif dir == 'v':
            if obj == '[':
                if move2(y + 1, x, dir) and move2(y + 1, x + 1, dir):
                    grid2[y + 1][x] = obj
                    grid2[y + 1][x + 1] = ']'
                    grid2[y][x] = '.'
                    grid2[y][x + 1] = '.'
                    return True
            elif obj == ']':
                if move2(y + 1, x, dir) and move2(y + 1, x - 1, dir):
                    grid2[y + 1][x] = obj
                    grid2[y + 1][x - 1] = '['
                    grid2[y][x] = '.'
                    grid2[y][x - 1] = '.'
                    return True
            elif obj == '@':
                if move2(y + 1, x, dir):
                    grid2[y][x] = '.'
                    grid2[y + 1][x] = obj
                    return True
        elif dir == '>':
            if move2(y, x + 1, dir):
                grid2[y][x] = '.'
                grid2[y][x + 1] = obj
                return True
        elif dir == '<':
            if move2(y, x - 1, dir):
                grid2[y][x] = '.'
                grid2[y][x - 1] = obj
                return True

        return False

    for instruction in instructions:
        os.system('clear')
        print_grid(grid2)
        time.sleep(.1)
        
        if move2(cur_y, cur_x, instruction):
            if instruction == '^':
                cur_y -= 1
            elif instruction == 'v':
                cur_y += 1
            elif instruction == '<':
                cur_x -= 1
            elif instruction == '>':
                cur_x += 1

    print(f'Part 2: {get_gps(grid2)}') #

