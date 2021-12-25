import copy

if __name__ == '__main__':
    print('Advent of Code 2021 - Day 08')
    
    '''
      0:      1:      2:      3:      4:
     aaaa    ....    aaaa    aaaa    ....
    b    c  .    c  .    c  .    c  b    c
    b    c  .    c  .    c  .    c  b    c
     ....    ....    dddd    dddd    dddd
    e    f  .    f  e    .  .    f  .    f
    e    f  .    f  e    .  .    f  .    f
     gggg    ....    gggg    gggg    ....

      5:      6:      7:      8:      9:
     aaaa    aaaa    aaaa    aaaa    aaaa
    b    .  b    .  .    c  b    c  b    c
    b    .  b    .  .    c  b    c  b    c
     dddd    dddd    ....    dddd    dddd
    .    f  e    f  .    f  e    f  .    f
    .    f  e    f  .    f  e    f  .    f
     gggg    gggg    ....    gggg    gggg
    '''

    with open('day08.txt') as f:
        output_list = []
        signal_list = []
        for line in f.read().splitlines():
            signal, output = line.split(' | ')
            output_list.append([o for o in output.split(' ')])
            signal_list.append([s for s in signal.split(' ')])

    # part 1

    easy_digits = 0
    for output in output_list:
        easy_digits += len([i for i in output if len(i) in {2, 3, 4, 7}])

    print(f'Part 1: {easy_digits}') # 397

    
    # part 2

    def decode(given_patterns):
        patterns = copy.deepcopy(given_patterns)
        decoded = {}

        def set_value(digit, display):
            decoded[digit] = display
            patterns.remove(display)
        
        # find easy digits: 1, 4, 7, 8
        for pattern in patterns[:]:
            if len(pattern) == 2:
                set_value(1, pattern)
            elif len(pattern) == 4:
                set_value(4, pattern)
            elif len(pattern) == 3:
                set_value(7, pattern)
            elif len(pattern) == 7:
                set_value(8, pattern)
            else:
                continue

        # find 6
        for pattern in patterns[:]:
            if len(pattern) == 6 and not set(decoded[1]).issubset(set(pattern)):
                set_value(6, pattern)
                break

        # find 5, segment_e
        for pattern in patterns[:]:
            if len(pattern) == 5 and len(set(decoded[6]) - set(pattern)) == 1:
                segment_e = (set(decoded[6]) - set(pattern)).pop()
                set_value(5, pattern)
                break

        # find 9
        for pattern in patterns[:]:
            if set(pattern) == set(decoded[8].replace(segment_e, '')):
                set_value(9, pattern)
                break

        # find 0
        for pattern in patterns[:]:
            if len(pattern) == 6:
                set_value(0, pattern)
                break

        # find 2
        for pattern in patterns[:]:
            if segment_e in pattern:
                set_value(2, pattern)
                break

        # find 3
        set_value(3, patterns[0])

        return decoded

    
    total = 0
    for output, display in zip(output_list, signal_list):
        decoded = decode(display)

        for i, digit in enumerate(output):
            for k, v in decoded.items():
                if set(digit) == set(v):
                    total += 10**(3-i) * k
                    break

    print(f'Part 2: {total}') # 1027422
