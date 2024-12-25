from typing import Optional, Tuple


if __name__ == '__main__':
    print("Advent of Code 2018 - Day 11: Chronal Charge")

    with open('day11.txt') as f:
        serial_no = int(f.read())
    
    # part 1
    fuel_powers = {}
    grid_powers = {}

    def get_fuel_power(x: int, y: int) -> int:
        if (x, y) in fuel_powers:
            pass
        
        else:
            global serial_no
            rack_id = x + 10
            power = ((((rack_id * y + serial_no) * rack_id) % 1000) // 100) - 5
            fuel_powers[(x, y)] = power
        return fuel_powers[(x, y)]

    
    def get_grid_power(x: int, y: int) -> int:
        if (x, y) in grid_powers:
            pass

        elif (x-1, y) in grid_powers:
            power = sum([
                grid_powers[(x-1, y)],
                get_fuel_power(x+2, y), 
                get_fuel_power(x+2, y+1),
                get_fuel_power(x+2, y+2),
                -get_fuel_power(x-1, y),
                -get_fuel_power(x-1, y+1),
                -get_fuel_power(x-1, y+2)
            ])
            
        elif (x, y-1) in grid_powers:
            power = sum([
                grid_powers[(x, y-1)],
                get_fuel_power(x, y+2),
                get_fuel_power(x+1, y+2),
                get_fuel_power(x+2, y+2),
                -get_fuel_power(x, y-1),
                -get_fuel_power(x+1, y-1),
                -get_fuel_power(x+2, y-1)
            ])

        else:
            power = 0
            for dx in range(x, x+3):
                for dy in range(y, y+3):
                    power += get_fuel_power(dx, dy)

        grid_powers[(x, y)] = power
        return grid_powers[(x, y)]
    
    max_grid_power = 0
    coords1 = None
    for x in range(1, 299):
        for y in range(1, 299):
            grid_power = get_grid_power(x, y)
            if grid_power > max_grid_power:
                max_grid_power = grid_power
                coords1 = f'{x},{y}'

    print(f'Part 1: {coords1}') # 21,61


    # part 2
    square_powers = {}
    col_powers = {}
    row_powers = {}

    def get_square_power(
        x1: int, y1: int, x2: int, y2: int
    ) -> Tuple[int, int, int]:
        if (x1, y1, x2, y2) in square_powers:
            return square_powers[(x1, y1, x2, y2)]

        global max_power, max_grid
        size = x2 - x1 + 1
        if x1 == x2 and y1 == y2:
             power = get_fuel_power(x1, y1)

        else:
            power = sum([
                get_square_power(x1, y1, x2-1, y2-1)[3],
                get_col_power(x2, y1, y2-1),
                get_row_power(y2, x1, x2-1),
                get_fuel_power(x2, y2)
            ])

        if power > max_power:
            max_power = power
            max_grid = x1, y1, size

        square_powers[(x1, y1, x2, y2)] = (x1, y1, size, power)
        return square_powers[(x1, y1, x2, y2)]

    def get_col_power(x: int, y1: int, y2: int) -> int:
        if (x, y1, y2) in col_powers:
            pass
        elif y1 == y2:
            col_powers[(x, y1, y2)] = get_fuel_power(x, y1)
        elif (x, y1+1, y2) in col_powers:
            power = col_powers[(x, y1+1, y2)] + get_fuel_power(x, y1)
            col_powers[(x, y1, y2)] = power
        else:
            col_powers[(x, y1,y2)] = sum([
                get_col_power(x, y1, y2-1),
                get_fuel_power(x, y2)
            ])
        return col_powers[(x, y1,y2)]
    
    def get_row_power(y: int, x1: int, x2: int) -> int:
        if (y, x1, x2) in row_powers:
            pass
        elif x1 == x2:
            row_powers[(y, x1, x2)] = get_fuel_power(x1, y)
        elif (y, x1+1, x2) in row_powers:
            power = row_powers[(y, x1+1, x2)] + get_fuel_power(x1, y)
            row_powers[(y, x1, x2)] = power
        else:
            row_powers[(y, x1, x2)] = sum([
                get_row_power(y, x1, x2-1),
                get_fuel_power(x2, y)
            ])
        return row_powers[(y, x1, x2)]

    max_power = 0
    max_grid = None
    
    for x in range(300, 0, -1):
        for y in range(300, 0, -1):
            size = min(300 - x, 300 - y)
            get_square_power(x, y, x + size, y + size)

    coords2 = f'{max_grid[0]},{max_grid[1]},{max_grid[2]}'
    print(f'Part 2: {coords2}') # 232,251,12
