class Pipe:
    directions = {
        '|': {'up', 'down'},
        '-': {'left', 'right'},
        'L': {'up', 'right'},
        'J': {'up', 'left'},
        '7': {'down', 'left'},
        'F': {'down', 'right'},
    }

    def __init__(self, tile: str, inlet: str) -> None:
        self.tile = tile
        if inlet not in self.directions[self.tile]:
            raise NotImplementedError('Incorrect tile inlet')
        self.inlet = inlet
        self.outlet = (self.directions[self.tile] - {self.inlet}).pop()

if __name__ == '__main__':
    print('Advent of Code 2023 - Day 10')

    with open('day10.txt') as f:
        map_ = {}
        for row, line in enumerate(f.read().splitlines()):
            for col, tile in enumerate(line):
                map_[(row, col)] = tile
                if tile == 'S':
                    start_row, start_col = (row, col)
    

    # n_direction: [relative coordinates, set of tiles, entry for next tile]
    n_direction = { 
        'up': [(-1, 0), {'|', '7', 'F'}, 'down'],
        'down': [(1, 0), {'|', 'L', 'J'}, 'up'],
        'left': [(0, -1), {'-', 'L', 'F'}, 'right'],
        'right': [(0, 1), {'-', '7', 'J'}, 'left'],
    }

    y1, x1 = None, None
    y2, x2 = start_row, start_col
    area = 0 # compute area using triangle formula / shoelace formula

    for direction in n_direction:
        (drow, dcol), connected_tiles, inlet = n_direction[direction]
        neighbor = map_.get((start_row + drow, start_col + dcol))
        if neighbor in connected_tiles:
            cur_pipe = Pipe(neighbor, inlet)
            cur_row, cur_col = start_row + drow, start_col + dcol
            y1, y2 = y2, cur_row
            x1, x2 = x2, cur_col
            area += 0.5 * ((x1 * y2) - (x2 * y1))
            break

    steps = 1
    while True:
        (drow, dcol), _, next_inlet = n_direction[cur_pipe.outlet]
        cur_row, cur_col = cur_row + drow, cur_col + dcol
        next_tile = map_.get((cur_row, cur_col))
        steps += 1
        if True:
            y1, y2 = y2, cur_row
            x1, x2 = x2, cur_col
            area += 0.5 * ((x1 * y2) - (x2 * y1))
        if next_tile == 'S':
            break
        cur_pipe = Pipe(next_tile, next_inlet)

    print(f'Part 1: {steps//2}') # 6714 - part 1

    print(f'Part 2: {int(abs(area) - steps//2 + 1)}') # 429 - part 2