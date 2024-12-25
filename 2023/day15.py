from collections import OrderedDict


if __name__ == '__main__':
    print("Advent of Code 2023 - Day 15: Lens Library")

    with open('day15.txt') as f:
        seq = [s for s in f.read().split(',')]

    def get_hash(string: str) -> int:
        result = 0
        for char in string:
            result += ord(char)
            result *= 17
            result = result % 256
        return result
    

    # part 1

    total = 0
    for string in seq:
        total += get_hash(string)
    
    print(f'Part 1: {total}') # 498538


    # part 2

    boxes = {num: OrderedDict() for num in range(256)}
    for string in seq:
        if '-' in string:
            op = '-'
            lens, focal = string.split('-')
        elif '=' in string:
            op = '='
            lens, focal = string.split('=')
        
        box = get_hash(lens)
        if op == '-':
            if lens in boxes[box]:
                del boxes[box][lens]
        elif op == '=':
            boxes[box][lens] = int(focal)
    
    power = 0
    for box, lenses in boxes.items():
        for i, (lens, focal) in enumerate(lenses.items(), 1):
            power += (box + 1) * (focal) * (i)

    print(f'Part 2: {power}') # 286278
