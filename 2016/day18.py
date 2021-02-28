print('Advent of Code 2016 - Day 18')
with open('day18.txt') as f:
    row1 = f.readline()

def get_tile(three_tile_above):
    trap_indicator = {'.^^', '^^.', '..^', '^..'}
    return '.' if three_tile_above not in trap_indicator else '^'

def count_safe_tiles(rows):

    current_row = row1
    safe_tiles = row1.count('.')

    for _ in range(rows-1):
        next_row = ''

        for i in range(len(row1)):
            if i == 0:
                next_row += get_tile('.' + current_row[i:i+2])
            elif i == len(row1) - 1:
                next_row += get_tile(current_row[i-1:i+1] + '.')
            else:
                next_row += get_tile(current_row[i-1:i+2])
            
        safe_tiles += next_row.count('.')
        current_row = next_row

    return safe_tiles

print(f'Part 1: {count_safe_tiles(40)}') # 1961 - part 1

print(f'Part 2: {count_safe_tiles(400_000)}') # 20000795 - part 2
