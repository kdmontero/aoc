from typing import Optional
from functools import lru_cache


if __name__ == '__main__':
    print('Advent of Code 2018 - Day 11')

    with open('day11.txt') as f:
        serial_no = int(f.read())
    
    @lru_cache()
    def get_fuel_power(x: int, y: int) -> int:
        global serial_no
        rack_id = x + 10
        return ((((rack_id * y + serial_no) * rack_id) % 1000) // 100) - 5
    
    @lru_cache()
    def get_grid_power(x: int, y: int, square: Optional[int] = 3) -> int:
        if square == 0:
            return 0

        power = get_fuel_power(x, y)
        for s in range(square):
            power += get_fuel_power(x, y+s)
            power += get_fuel_power(x+s, y)
        power += get_grid_power(x+1, y+1, square-1)
        return power
    
    max_grid_power = 0
    coords1 = None
    for x in range(1, 299):
        for y in range(1, 299):
            grid_power = get_grid_power(x, y)
            if grid_power > max_grid_power:
                max_grid_power = grid_power
                coords1 = f'{x},{y}'

    print(f'Part 1: {coords1}') # 21,61


    @lru_cache
    def get_square_power(x: int, y: int) -> tuple[int, int]:
        max_square = 300 - max(x, y) + 1
        max_power = 0
        square = 0
        for s in range(1, max_square + 1):
            power = get_grid_power(x, y, s)
            if power > max_power:
                max_power = power
                square = s
        return power, square

    max_square_power = 0
    coords2 = None
    for x in range(1, 301):
        for y in range(1, 301):
            print(x, y)
            square_power, square = get_square_power(x, y)
            if square_power > max_square_power:
                max_square_power = square_power
                coords2 = f'{x},{y},{square}'

    print(f'Part 2: {coords2}') #