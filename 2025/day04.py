if __name__ == '__main__':
    print("Advent of Code 2025 - Day 04: Printing Department")

    Coord = tuple[int, int]

    with open('day04.txt') as f:
        paper_grid: set[Coord] = set()
        for y, line in enumerate(f.read().strip().splitlines()):
            for x, char in enumerate(line):
                if char == '@':
                    paper_grid.add((y, x))

    def check_adj(y: int, x: int) -> bool:
        adj_rolls = 0
        for dy in (y-1, y, y+1):
            for dx in (x-1, x, x+1):
                if dy == y and dx == x:
                    continue
                if (dy, dx) in paper_grid:
                    adj_rolls += 1

        return adj_rolls < 4

    # part 1

    removed_rolls = 0
    for i, j in paper_grid:
        removed_rolls += check_adj(i, j)

    print(f'Part 1: {removed_rolls}') # 1540


    # part 2

    max_removed = 0
    while True:
        for_removal: set[Coord] = set()
        for i, j in paper_grid:
            if check_adj(i, j):
                for_removal.add((i, j))

        if len(for_removal) == 0:
            break

        max_removed += len(for_removal)
        paper_grid -= for_removal

    print(f'Part 2: {max_removed}') # 8972

