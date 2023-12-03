import re


if __name__ == '__main__':
    print('Advent of Code 2023 - Day 03')

    with open('day03.txt') as f:
        map_ = {}
        lines = []

        for y, line in enumerate(f.read().splitlines()):
            lines.append(line)
            for x, char in enumerate(line):
                map_[y, x] = char
    

    # part 1

    def is_part_num(y, x):
        for j in [-1, 0, 1]:
            for k in [-1, 0, 1]:
                if j == k == 0:
                    continue
                
                neighbor = map_.get((y + j, x + k))
                if not neighbor:
                    continue

                if neighbor not in '1234567890.':
                    return True
        return False

    total1 = 0
    pattern = re.compile(r'(\d+)')
    for y, line in enumerate(lines):
        nums = pattern.finditer(line)
        for num in nums:
            for x in range(num.start(1), num.end(1)):
                if is_part_num(y, x):
                    total1 += int(num.group(1))
                    break
            else:
                continue

    print(f'Part 1: {total1}') # 531561


    # part 2

    def asterisks_neighbor(y, x):
        asterisks = []
        for j in [-1, 0, 1]:
            for k in [-1, 0, 1]:
                if j == k == 0:
                    continue
                neighbor = map_.get((y + j, x + k))
                if neighbor == '*':
                    asterisks.append((y + j, x + k))
        return asterisks

    asterisk_map = {}
    pattern = re.compile(r'(\d+)')
    for y, line in enumerate(lines):
        nums = pattern.finditer(line)
        for num in nums:
            for x in range(num.start(1), num.end(1)):
                for asterisk in asterisks_neighbor(y, x):
                    if asterisk not in asterisk_map:
                        asterisk_map[asterisk] = [num]
                    elif num not in asterisk_map[asterisk]:
                        asterisk_map[asterisk].append(num)

    total2 = 0
    for _, asterisks in asterisk_map.items():
        if len(asterisks) == 2:
            pn1, pn2 = asterisks
            total2 += int(pn1.group(1)) * int(pn2.group(1))

    print(f'Part 2: {total2}') # 83279367
