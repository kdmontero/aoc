if __name__ == '__main__':
    print("Advent of Code 2023 - Day 11: Cosmic Expansion")

    with open('day11.txt') as f:
        orig_image = []
        for line in f.read().splitlines():
            row = []
            for char in list(line):
                row.append(char)
            orig_image.append(row)
    
    def find_total_distancee(image: list[list[str]], expansion: int) -> int:
        empty_rows = set()
        for row, line in enumerate(image):
            if set(line) == {'.'}:
                empty_rows.add(row)

        transposed = [list(line) for line in zip(*image)]
        empty_cols = set()
        for col, line in enumerate(transposed):
            if set(line) == {'.'}:
                empty_cols.add(col)
        expanded = [list(line) for line in zip(*transposed)]
        
        exp_map = []
        for row, line in enumerate(expanded):
            for col, char in enumerate(line):
                if char == '#':
                    exp_map.append([row, col])

        total = 0
        for i, (r1, c1) in enumerate(exp_map):
            for r2, c2 in exp_map[i+1:]:
                total += abs(r1 - r2) + abs(c1 - c2)
                if r1 > r2:
                    row_range = set(range(r2, r1))
                else:
                    row_range = set(range(r1, r2))
                
                if c1 > c2:
                    col_range = set(range(c2, c1))
                else:
                    col_range = set(range(c1, c2))
                
                total += len(empty_rows & row_range) * (expansion - 1)
                total += len(empty_cols & col_range) * (expansion - 1)
        
        return total

    
    # part 1

    total1 = find_total_distancee(orig_image, 2)
    print(f'Part 1: {total1}') # 9918828


    # part 2

    total2 = find_total_distancee(orig_image, 1_000_000)
    print(f'Part 2: {total2}') # 692506533832 