import functools

if __name__ == '__main__':
    print('Advent of Code 2022 - Day 13')

    with open('day13.txt') as f:
        pairs = []
        for pair_block in f.read().split('\n\n'):
            p1, p2 = pair_block.splitlines()
            p1 = eval(p1)
            p2 = eval(p2)
            pairs.append([p1, p2])


    # part 1
    
    def compare(p1: int | list[int], p2: int | list[int]) -> int:
        try:
            if p1 == p2:
                return 0
            else:
                return 1 if p1 < p2 else -1
        except TypeError:
            if isinstance(p1, int):
                return compare([p1], p2)
            elif isinstance(p2, int):
                return compare(p1, [p2])
            else:
                for pp1, pp2 in zip(p1, p2):
                    if compare(pp1, pp2) == 0:
                        continue
                    else:
                        return compare(pp1, pp2)
                else:
                    if len(p1) < len(p2):
                        return 1
                    return -1


    total = 0
    for i, pair in enumerate(pairs, 1):
        if compare(*pair) == 1:
            total += i
        
    print(f'Part 1: {total}') # 6484


    # part 2

    packets = [[[2]], [[6]]]
    for pair in pairs:
        packets.extend(pair)

    packets.sort(key=functools.cmp_to_key(compare), reverse=True)
    index1 = packets.index([[2]]) + 1 
    index2 = packets.index([[6]]) + 1

    print(f'Part 2: {index1 * index2}') # 19305
