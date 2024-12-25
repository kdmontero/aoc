import os
import time


if __name__ == '__main__':
    print("Advent of Code 2024 - Day 15: Warehouse Woes")

    with open('day15.txt') as f:
        map_, ins = f.read().strip().split('\n\n')
        instructions = ins.replace('\n', '')
        instructions_length = len(instructions)

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

    def is_movable_then_move(y: int, x: int, dir: str) -> bool:
        obj = grid1[y][x]
        if obj == '#':
            return False
        elif obj == '.':
            return True
            
        if dir == '^':
            if is_movable_then_move(y - 1, x, dir):
                grid1[y][x] = '.'
                grid1[y - 1][x] = obj
                return True
        elif dir == 'v':
            if is_movable_then_move(y + 1, x, dir):
                grid1[y][x] = '.'
                grid1[y + 1][x] = obj
                return True
        elif dir == '>':
            if is_movable_then_move(y, x + 1, dir):
                grid1[y][x] = '.'
                grid1[y][x + 1] = obj
                return True
        elif dir == '<':
            if is_movable_then_move(y, x - 1, dir):
                grid1[y][x] = '.'
                grid1[y][x - 1] = obj
                return True

        return False

    def run_part_1(
        instructions: str,
        cur_y: int,
        cur_x: int,
        animate: bool = False
    ) -> None:

        for i, instruction in enumerate(instructions):

            if animate:
                os.system('clear')
                print(f'Steps Remaining: {instructions_length - i - 1}')
                print_grid(grid1)
                time.sleep(.001)

            if is_movable_then_move(cur_y, cur_x, instruction):
                if instruction == '^':
                    cur_y -= 1
                elif instruction == 'v':
                    cur_y += 1
                elif instruction == '<':
                    cur_x -= 1
                elif instruction == '>':
                    cur_x += 1

    run_part_1(instructions, cur_y, cur_x)

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

    def move(y: int, x: int, dir: str) -> None:
        obj = grid2[y][x]
        if obj in '.#':
            return
            
        if dir == '^':
            if obj == '[':
                move(y - 1, x, dir)
                move(y - 1, x + 1, dir)
                grid2[y - 1][x] = obj
                grid2[y - 1][x + 1] = ']'
                grid2[y][x] = '.'
                grid2[y][x + 1] = '.'
            elif obj == ']':
                move(y - 1, x, dir)
                move(y - 1, x - 1, dir)
                grid2[y - 1][x] = obj
                grid2[y - 1][x - 1] = '['
                grid2[y][x] = '.'
                grid2[y][x - 1] = '.'
            elif obj == '@':
                move(y - 1, x, dir)
                grid2[y][x] = '.'
                grid2[y - 1][x] = obj
        elif dir == 'v':
            if obj == '[':
                move(y + 1, x, dir)
                move(y + 1, x + 1, dir)
                grid2[y + 1][x] = obj
                grid2[y + 1][x + 1] = ']'
                grid2[y][x] = '.'
                grid2[y][x + 1] = '.'
            elif obj == ']':
                move(y + 1, x, dir)
                move(y + 1, x - 1, dir)
                grid2[y + 1][x] = obj
                grid2[y + 1][x - 1] = '['
                grid2[y][x] = '.'
                grid2[y][x - 1] = '.'
            elif obj == '@':
                move(y + 1, x, dir)
                grid2[y][x] = '.'
                grid2[y + 1][x] = obj
        elif dir == '>':
            move(y, x + 1, dir)
            grid2[y][x] = '.'
            grid2[y][x + 1] = obj
        elif dir == '<':
            move(y, x - 1, dir)
            grid2[y][x] = '.'
            grid2[y][x - 1] = obj

    def is_movable(y: int, x: int, dir: str) -> bool:
        obj = grid2[y][x]
        if obj == '#':
            return False
        elif obj == '.':
            return True
            
        if dir == '^':
            if obj == '[':
                if is_movable(y - 1, x, dir) and is_movable(y - 1, x + 1, dir):
                    return True
            elif obj == ']':
                if is_movable(y - 1, x, dir) and is_movable(y - 1, x - 1, dir):
                    return True
            elif obj == '@':
                if is_movable(y - 1, x, dir):
                    return True
        elif dir == 'v':
            if obj == '[':
                if is_movable(y + 1, x, dir) and is_movable(y + 1, x + 1, dir):
                    return True
            elif obj == ']':
                if is_movable(y + 1, x, dir) and is_movable(y + 1, x - 1, dir):
                    return True
            elif obj == '@':
                if is_movable(y + 1, x, dir):
                    return True
        elif dir == '>':
            if is_movable(y, x + 1, dir):
                return True
        elif dir == '<':
            if is_movable(y, x - 1, dir):
                return True

        return False

    def run_part_2(
        instructions: str,
        cur_y: int,
        cur_x: int,
        animate: bool = False
    ) -> None:

        for i, instruction in enumerate(instructions):

            if animate:
                os.system('clear')
                print(f'Steps Remaining: {instructions_length - i - 1}')
                print_grid(grid2)
                time.sleep(.001)
            
            if is_movable(cur_y, cur_x, instruction):
                move(cur_y, cur_x, instruction)
                if instruction == '^':
                    cur_y -= 1
                elif instruction == 'v':
                    cur_y += 1
                elif instruction == '<':
                    cur_x -= 1
                elif instruction == '>':
                    cur_x += 1

    run_part_2(instructions, cur_y, cur_x)

    print(f'Part 2: {get_gps(grid2)}') # 1337648

