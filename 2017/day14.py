from collections import deque
from day10 import KnotHash
from day12 import group_qty

if __name__ == '__main__':
    print("Advent of Code 2017 - Day 14: Disk Defragmentation")

    INPUT = 'vbqugkhl'

    # part 1

    disk_rows_hash = []

    for row in range(128):
        lengths = KnotHash.get_lengths(f'{INPUT}-{row}')
        row = KnotHash(deque(range(256)), lengths, 0, 0)
        disk_rows_hash.append(row.final_knot_hash())
        
    disk = []
    def convert_to_bits(hex_digit):
        bits = bin(int(hex_digit, 16))[2:]
        bits = '0'*(4 - len(bits)) + bits
        return bits

    for row in disk_rows_hash:
        disk_row = ''
        for hex_digit in row:
            disk_row += convert_to_bits(hex_digit)
        disk.append(disk_row)

    used_squares = 0
    for row in disk:
        used_squares += row.count('1')

    print(f'Part 1: {used_squares}') # 8148


    # part 2
    
    used = set()
    for r in range(128):
        for c in range(128):
            if disk[r][c] == '1':
                used.add((r, c))
                
    data_map = {}

    def connect(node1, node2):
        if node1 in data_map:
            data_map[node1].add(node2)
        else:
            data_map[node1] = {node2}

        if node2 in data_map:
            data_map[node2].add(node1)
        else:
            data_map[node2] = {node1}

    for (r, c) in used:
        if (r, c+1) in used:
            connect((r, c), (r, c+1))
        if (r, c-1) in used:
            connect((r, c), (r, c-1))
        if (r+1, c) in used:
            connect((r, c), (r+1, c))
        if (r-1, c) in used:
            connect((r, c), (r-1, c))
        connect((r, c), (r, c))

    print(f'Part 2: {group_qty(data_map)}') # 1180
