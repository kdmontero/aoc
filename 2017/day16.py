from collections import deque

if __name__ == '__main__':
    print("Advent of Code 2017 - Day 16: Permutation Promenade")

    PROGRAM = 'abcdefghijklmnop'
    with open('day16.txt') as f:
        ins = []
        for move in f.read().split(','):
            if move[0] == 's':
                ins.append(['s', int(move[1:])])

            elif move[0] == 'x':
                a, b = move[1:].split('/')
                ins.append(['x', int(a), int(b)])

            elif move[0] == 'p':
                ins.append(list(move.replace('/', '')))

    def dance(program, move):
        if move[0] == 's':
            program = deque(program)
            program.rotate(move[1])
            return list(program)

        elif move[0] == 'x':
            a, b = move[1], move[2]
            program[a], program[b] = program[b], program[a]
            return program

        elif move[0] == 'p':
            a = program.index(move[1])
            b = program.index(move[2])
            program[a], program[b] = program[b], program[a]
            return program


    def complete_dance(program, ins, loop):
        p = list(program)
        for i in range(loop):
            for move in ins:
                p = dance(p, move)

        return ''.join(p)


    # part 1
    print(f'Part 1: {"".join(complete_dance(PROGRAM, ins, 1))}')
    # kgdchlfniambejop


    # part 2

    def find_cycle(program, ins):
        p = list(program)
        for i in range(1_000_000_000):
            for move in ins:
                p = dance(p, move)

            if p == list(program):
                break

        return i + 1

    cycle = find_cycle(PROGRAM, ins)
    loop = 1_000_000_000 % cycle

    print(f'Part 2: {"".join(complete_dance(PROGRAM, ins, loop))}')
    # fjpmholcibdgeakn
