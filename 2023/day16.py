if __name__ == '__main__':
    print('Advent of Code 2023 - Day 16')

    with open('day16.txt') as f:
        grid = {}
        for row, line in enumerate(f.read().splitlines()):
            for col, char in enumerate(line):
                grid[(row, col)] = char
        height, width = row, col
    
    def get_next_pos(y: int, x: int, way: str) -> list[tuple[int, int, str]]:
        '''
        y, x: current position
        way: direction of beam going to the current position (inlet)
        '''
        tile = grid[(y, x)]
        if way == 'up':
            if tile in '|.':
                return [(y-1, x, 'up')]
            elif tile == '-':
                return [(y, x-1, 'left'), (y, x+1, 'right')]
            elif tile == '/':
                return [(y, x+1, 'right')]
            elif tile == '\\':
                return [(y, x-1, 'left')]
        elif way == 'down':
            if tile in '|.':
                return [(y+1, x, 'down')]
            elif tile == '-':
                return [(y, x-1, 'left'), (y, x+1, 'right')]
            elif tile == '/':
                return [(y, x-1, 'left')]
            elif tile == '\\':
                return [(y, x+1, 'right')]
        elif way == 'right':
            if tile in '-.':
                return [(y, x+1, 'right')]
            elif tile == '|':
                return [(y-1, x, 'up'), (y+1, x, 'down')]
            elif tile == '/':
                return [(y-1, x, 'up')]
            elif tile == '\\':
                return [(y+1, x, 'down')]
        elif way == 'left':
            if tile in '-.':
                return [(y, x-1, 'left')]
            elif tile == '|':
                return [(y-1, x, 'up'), (y+1, x, 'down')]
            elif tile == '/':
                return [(y+1, x, 'down')]
            elif tile == '\\':
                return [(y-1, x, 'up')]

    def get_energized(start_y: int, start_x: int, way: str) -> int:
        beam_states = set()
        queue = [(start_y, start_x, way)]
        while queue:
            new_queue = []
            for cur_tile in queue:
                if cur_tile in beam_states:
                    continue
                beam_states.add(cur_tile)

                for next_tile in get_next_pos(*cur_tile):
                    next_y, next_x, _ = next_tile
                    if grid.get((next_y, next_x)):
                        new_queue.append(next_tile)

            queue = new_queue
        
        energized = set()
        for y, x, _ in beam_states:
            energized.add((y, x))

        return len(energized)


    # part 1
    total_energized1 = get_energized(0, 0, 'right')
    print(f'Part 1: {total_energized1}') # 8389


    # part 2
    max_energized = 0
    for y in range(height + 1):
        for x in range(width + 1):
            if y == 0:
                max_energized = max(max_energized, get_energized(y, x, 'down'))
            if y == height:
                max_energized = max(max_energized, get_energized(y, x, 'up'))
            if x == 0:
                max_energized = max(max_energized, get_energized(y, x, 'right'))
            if x == width:
                max_energized = max(max_energized, get_energized(y, x, 'left'))
    print(f'Part 2: {max_energized}') # 8564