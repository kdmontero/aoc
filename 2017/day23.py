from collections import defaultdict, deque

class Program:
    def __init__(self, a, instructions):
        self.instructions = instructions
        self.reg = defaultdict(int)
        self.reg['a'] = a
        self.i = 0
        self.mul_count = 0
        
    def get_val(self, char):
        try:
            return int(char)
        except ValueError:
            return self.reg[char]

    def run(self):
        while self.i < len(self.instructions):
            ins, register, value = self.instructions[self.i]

            if ins == 'set':
                self.reg[register] = self.get_val(value)

            elif ins == 'sub':
                self.reg[register] -= self.get_val(value)

            elif ins == 'mul':
                self.reg[register] *= self.get_val(value)
                self.mul_count += 1

            elif ins == 'jnz':
                if self.get_val(register) != 0:
                    self.i += self.get_val(value)
                    continue

            elif ins == 'nop':
                pass

            # check if 'b' is composite
            elif ins == 'check':
                for d in range(2, self.reg['b']):
                    if self.reg['b'] % d == 0:
                        self.reg['f'] = 0
                        break

            self.i += 1


if __name__ == '__main__':
    print("Advent of Code 2017 - Day 23: Coprocessor Conflagration")

    with open('day23.txt') as f:
        instructions = [line.split() for line in f.read().splitlines()]


    # part 1
    
    p1 = Program(0, instructions)
    p1.run()
    print(f'Part 1: {p1.mul_count}') # 3025


    # part 2
    
    # change these lines 9 to 23
    # set e 2
    # set g d
    # mul g e
    # sub g b
    # jnz g 2
    # set f 0
    # sub e -1
    # set g e
    # sub g b
    # jnz g -8
    # sub d -1
    # set g d
    # sub g b
    # jnz g -13

    instructions[9] = ['check', 0, 0]
    for line in range(10, 24):
        instructions[line] = ['nop', 0, 0]

    p2 = Program(1, instructions)
    p2.run()

    print(f'Part 2: {p2.reg["h"]}') # 915
