from collections import defaultdict, deque

class Program:
    def __init__(self, id_, instructions):
        self.id_ = id_
        self.instructions = instructions
        self.reg = defaultdict(int)
        self.reg['p'] = id_
        self.queue = deque([])
        self.i = 0
        self.send_qty = 0
        
    def get_val(self, char):
        try:
            return int(char)
        except ValueError:
            return self.reg[char]

    def send(self, other, value):
        other.queue.append(value)
        self.send_qty += 1

    def run(self, other, task=True): # task = True for part 2, False for part 1
        while self.i < len(self.instructions):
            ins = self.instructions[self.i]

            if ins[0] == 'snd':
                if task:
                    self.send(other, self.get_val(ins[1]))
                else:
                    self.sound = self.get_val(ins[1])

            elif ins[0] == 'set':
                self.reg[ins[1]] = self.get_val(ins[2])

            elif ins[0] == 'add':
                self.reg[ins[1]] += self.get_val(ins[2])

            elif ins[0] == 'mul':
                self.reg[ins[1]] *= self.get_val(ins[2])

            elif ins[0] == 'mod':
                self.reg[ins[1]] %= self.get_val(ins[2])

            elif ins[0] == 'rcv':
                if task:
                    if self.queue:
                        self.reg[ins[1]] = self.queue.popleft()
                    else:
                        break
                else:
                    if self.get_val(ins[1]) != 0:
                        self.recover = self.sound
                        break
                    
            elif ins[0] == 'jgz':
                if self.get_val(ins[1]) > 0:
                    self.i += self.get_val(ins[2])
                    continue

            self.i += 1


if __name__ == '__main__':
    print('Advent of Code 2017 - Day 18')

    with open('day18.txt') as f:
        instructions = [line.split() for line in f.read().splitlines()]
            

    # part 1
    p0 = Program(0, instructions)
    p0.run(Program(0, []), False)
    print(f'Part 1: {p0.recover}') # 1187


    # part 2
    def duet(p1, p2):
        i = 0
        while True:
            p1.run(p2)
            p2.run(p1)
            if not (p1.queue or p2.queue):
                break
            i += 1
        return p2.send_qty

    p1 = Program(0, instructions)
    p2 = Program(1, instructions)
    print(f'Part 2: {duet(p1, p2)}') # 5969
