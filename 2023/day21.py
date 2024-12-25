if __name__ == '__main__':
    print("Advent of Code 2023 - Day 21: Step Counter")

    with open('day21.txt') as f:
        grid = set()
        for row, line in enumerate(f.read().splitlines()):
            for col, char in enumerate(line):
                if char == '#':
                    continue
                if char == 'S':
                    start_y, start_x = row, col
                grid.add((row, col))
    
    def get_n(y: int, x: int) -> list[tuple[int, int]]:
        neighbors = set()
        for ny, nx in [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]:
            if (ny, nx) in grid:
                neighbors.add((ny, nx))
        return neighbors


    # part 1
    visited = {(start_y, start_x)}
    for _ in range(64):
        new_visited = set()
        for y, x in visited:
            new_visited |= get_n(y, x)
        visited = new_visited

    print(f'Part 1: {len(visited)}') # 3762


    print(f'Part 2: {0} - Not Implemented') #