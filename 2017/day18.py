from collections import defaultdict

if __name__ == '__main__':
    print('Advent of Code 2017 - Day 18')

    with open('day18.txt') as f:
        instructions = [line.split() for line in f.read().splitlines()]

    reg = defaultdict(int)
    
    def get_val(char):
        try:
            return int(char)
        except ValueError:
            return reg[char]
            
    # part 1

    i = 0
    sound = None
    while i < len(instructions):
        ins = instructions[i]

        if ins[0] == 'snd':
            sound = get_val(ins[1])

        elif ins[0] == 'set':
            reg[ins[1]] = get_val(ins[2])

        elif ins[0] == 'add':
            reg[ins[1]] += get_val(ins[2])

        elif ins[0] == 'mul':
            reg[ins[1]] *= get_val(ins[2])

        elif ins[0] == 'mod':
            reg[ins[1]] %= get_val(ins[2])

        elif ins[0] == 'rcv':
            if get_val(ins[1]) != 0:
                recover = sound
                break

        elif ins[0] == 'jgz':
            if get_val(ins[1]) > 0:
                i += get_val(ins[2])
                continue

        i += 1

    print(f'Part 1: {recover}') # 1187


    # part 2

    print(f'Part 2: ') #
