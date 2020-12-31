import os
import time

with open('day17.txt') as given:
	intcode = [int(num) for num in given.read().split(',')]

intcode += [0]*10000

class ASCII:
    def __init__(self):
        self.relbase = 0
        self.index = 0
        self.program = intcode[:]
        self.camera = ''
    
    @property
    def scaffold(self):
        return [list(line) for line in self.camera.strip().splitlines()]

    def run(self, main=None, A=None, B=None, C=None, show_visualization=False):
        opcode = lambda num: int(str(num)[-2:])
        mode1 = lambda num: int(str(num)[-3]) if len(str(num))>=3 else 0
        mode2 = lambda num: int(str(num)[-4]) if len(str(num))>=4 else 0
        mode3 = lambda num: int(str(num)[-5]) if len(str(num))>=5 else 0

        if main == A == B == C == None:
            input_list = []
        else:
            input_list = main + A + B + C

        if show_visualization:
            input_list += [121, 10]
        else:
            input_list += [110, 10]

        i = self.index
        module = self.program
        new_line = 0
        while i < len(module)+1:
            if opcode(module[i]) == 1:
                if mode1(module[i]) == 1:
                    parameter1 = module[i+1]
                elif mode1(module[i]) == 0:
                    parameter1 = module[module[i+1]]
                elif mode1(module[i]) == 2:
                    parameter1 = module[module[i+1]+self.relbase]
                if mode2(module[i]) == 1:
                    parameter2 = module[i+2]
                elif mode2(module[i]) == 0:
                    parameter2 = module[module[i+2]]
                elif mode2(module[i]) == 2:
                    parameter2 = module[module[i+2]+self.relbase]
                if mode3(module[i]) == 1:
                    parameter3 = i+3
                    module[parameter3] = parameter1 + parameter2
                elif mode3(module[i]) == 0:
                    parameter3 = module[i+3]
                    module[parameter3] = parameter1 + parameter2
                elif mode3(module[i]) == 2:
                    parameter3 = module[i+3]+self.relbase
                    module[parameter3] = parameter1 + parameter2
                i += 4
            elif opcode(module[i]) == 2:
                if mode1(module[i]) == 1:
                    parameter1 = module[i+1]
                elif mode1(module[i]) == 0:
                    parameter1 = module[module[i+1]]
                elif mode1(module[i]) == 2:
                    parameter1 = module[module[i+1]+self.relbase]
                if mode2(module[i]) == 1:
                    parameter2 = module[i+2]
                elif mode2(module[i]) == 0:
                    parameter2 = module[module[i+2]]
                elif mode2(module[i]) == 2:
                    parameter2 = module[module[i+2]+self.relbase]
                if mode3(module[i]) == 1:
                    parameter3 = i+3
                    module[parameter3] = parameter1 * parameter2
                elif mode3(module[i]) == 0:
                    parameter3 = module[i+3]
                    module[parameter3] = parameter1 * parameter2
                elif mode3(module[i]) == 2:
                    parameter3 = module[i+3]+self.relbase
                    module[parameter3] = parameter1 * parameter2
                i += 4
            elif opcode(module[i]) == 3:
                if mode1(module[i]) == 0:
                    module[module[i+1]] = input_list.pop(0)
                elif mode1(module[i]) == 2:
                    module[module[i+1]+self.relbase] = input_list.pop(0)
                i += 2
            elif opcode(module[i]) == 4:
                if mode1(module[i]) == 0:
                    output = module[module[i+1]]
                elif mode1(module[i]) == 1:
                    output = module[i+1]
                elif mode1(module[i]) == 2:
                    output = module[module[i+1]+self.relbase]
                self.camera += chr(output)
                if output == 10:
                    new_line += 1
                    if new_line == 2 and show_visualization:
                        os.system('clear')
                        print(self.camera)
                        time.sleep(0.01)
                        self.camera = ''
                        new_line == 0
                else:
                    new_line = 0
                i += 2
            elif opcode(module[i]) == 5:
                if mode1(module[i]) == 1:
                    parameter1 = module[i+1]
                elif mode1(module[i]) == 0:
                    parameter1 = module[module[i+1]]
                elif mode1(module[i]) == 2:
                    parameter1 = module[module[i+1]+self.relbase]
                if mode2(module[i]) == 1:
                    parameter2 = module[i+2]
                elif mode2(module[i]) == 0:
                    parameter2 = module[module[i+2]]
                elif mode2(module[i]) == 2:
                    parameter2 = module[module[i+2]+self.relbase]
                if parameter1 != 0:
                    i = parameter2
                else:
                    i += 3
            elif opcode(module[i]) == 6:
                if mode1(module[i]) == 1:
                    parameter1 = module[i+1]
                elif mode1(module[i]) == 0:
                    parameter1 = module[module[i+1]]
                elif mode1(module[i]) == 2:
                    parameter1 = module[module[i+1]+self.relbase]
                if mode2(module[i]) == 1:
                    parameter2 = module[i+2]
                elif mode2(module[i]) == 0:
                    parameter2 = module[module[i+2]]
                elif mode2(module[i]) == 2:
                    parameter2 = module[module[i+2]+self.relbase]
                if parameter1 == 0:
                    i = parameter2
                else:
                    i += 3
            elif opcode(module[i]) == 7:
                if mode1(module[i]) == 1:
                    parameter1 = module[i+1]
                elif mode1(module[i]) == 0:
                    parameter1 = module[module[i+1]]
                elif mode1(module[i]) == 2:
                    parameter1 = module[module[i+1]+self.relbase]
                if mode2(module[i]) == 1:
                    parameter2 = module[i+2]
                elif mode2(module[i]) == 0:
                    parameter2 = module[module[i+2]]
                elif mode2(module[i]) == 2:
                    parameter2 = module[module[i+2]+self.relbase]
                if mode3(module[i]) == 0:
                    parameter3 = module[i+3]
                elif mode3(module[i]) == 2:
                    parameter3 = module[i+3]+self.relbase
                if parameter1 < parameter2:
                    module[parameter3] = 1
                else:
                    module[parameter3] = 0
                i += 4
            elif opcode(module[i]) == 8:
                if mode1(module[i]) == 1:
                    parameter1 = module[i+1]
                elif mode1(module[i]) == 0:
                    parameter1 = module[module[i+1]]
                elif mode1(module[i]) == 2:
                    parameter1 = module[module[i+1]+self.relbase]
                if mode2(module[i]) == 1:
                    parameter2 = module[i+2]
                elif mode2(module[i]) == 0:
                    parameter2 = module[module[i+2]]
                elif mode2(module[i]) == 2:
                    parameter2 = module[module[i+2]+self.relbase]
                if mode3(module[i]) == 0:
                    parameter3 = module[i+3]
                elif mode3(module[i]) == 2:
                    parameter3 = module[i+3]+self.relbase
                if parameter1 == parameter2:
                    module[parameter3] = 1
                else:
                    module[parameter3] = 0
                i += 4
            elif opcode(module[i]) == 9:
                if mode1(module[i]) == 0:
                    self.relbase += module[module[i+1]]
                elif mode1(module[i]) == 1:
                    self.relbase += module[i+1]
                elif mode1(module[i]) == 2:
                    self.relbase += module[module[i+1]+self.relbase]
                i += 2
            elif opcode(module[i]) == 99:
                return output
            else:
                print("Program is not working")
                return


# part 1
bot1 = ASCII()
bot1.run()
total = 0
for y, line in enumerate(bot1.scaffold):
    if y in {0, len(bot1.scaffold)-1}:
        continue
    for x, char in enumerate(line):
        if x in {0, len(line)-1}:
            continue
        if char == bot1.scaffold[y-1][x] == bot1.scaffold[y+1][x] == bot1.scaffold[y][x-1] == bot1.scaffold[y][x+1] == '#':
            total += (x * y)

print(f'Part 1: {total}') # 5788


# part 2
def convert_to_input(routine):
    input_list = []
    for i in list(routine):
        input_list.append(ord(i))
    input_list += [10]
    return input_list

bot2 = ASCII()
bot2.program[0] = 2

M = 'A,B,A,B,C,B,C,A,B,C'
A = 'R,4,R,10,R,8,R,4'
B = 'R,10,R,6,R,4'
C = 'R,4,L,12,R,6,L,12'

main = convert_to_input(M)
pattern_A = convert_to_input(A)
pattern_B = convert_to_input(B)
pattern_C = convert_to_input(C)
show_visualization = False # change this to see the robot's path

dust = bot2.run(main, pattern_A, pattern_B, pattern_C, show_visualization)

if show_visualization:
    print(f'Part 1: {total}') # 5788
print(f'Part 2: {dust}') # 648545
print(f'Main Pattern: {M}')
print(f'Pattern A: {A}')
print(f'Pattern B: {B}')
print(f'Pattern C: {C}')