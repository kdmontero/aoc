if __name__ == '__main__':
    print('Advent of Code 2022 - Day 10')

    with open('day10.txt') as f:
        program = []
        for line in f.read().splitlines():
            if line == 'noop':
                program.append('N')
            else:
                program.append(int(line.split()[1]))


    cycles = []
    for instruction in program:
        if isinstance(instruction, int):
            cycles.append(None)
            cycles.append(instruction)
        else:
            cycles.append(None)

    signal_strength = 0
    
    board = [[' ']*40 for _ in range(6)]

    i = 0
    X = 1

    while i < len(cycles):

        # part 1
        if i + 1 in {20, 60, 100, 140, 180, 220}:
            signal_strength += X * (i + 1)


        # part 2
        y, x = divmod(i, 40)
        if x in {X-1, X, X+1}:
            board[y][x] = '#'


        if cycles[i] is not None:
            X += cycles[i]
        i += 1

    print(f'Part 1: {signal_strength}') # 14060 - part 1

    print(f'Part 2:') # PAPKFKEJ - part 2
    for line in board:
        print(''.join(line))
