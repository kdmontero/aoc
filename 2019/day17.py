import os
import time

print('Advent of Code 2019 - Day 17')
with open('day17.txt') as given:
	intcode = [int(num) for num in given.read().split(',')]

intcode += [0]*10000

class ASCII:
    def __init__(self):
        self.relbase = 0
        self.index = 0
        self.program = intcode[:]
        self.camera = ''
    
    def reset(self):
        self.relbase = 0
        self.index = 0
        self.program = intcode[:]
        self.camera = ''

    @property
    def scaffold(self):
        return [list(line) for line in self.camera.strip().splitlines()]

    def run(self, main=None, A=None, B=None, C=None, show_visualization=False):
        opcode = lambda num: num%100
        mode1 = lambda num: num%1000 // 100 if num >= 100 else 0
        mode2 = lambda num: num%10000 // 1000 if num >= 1000 else 0
        mode3 = lambda num: num%100000 // 10000 if num >= 10000 else 0

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
bot = ASCII()
bot.run()
total = 0
for y, line in enumerate(bot.scaffold):
    if y in {0, len(bot.scaffold)-1}:
        continue
    for x, char in enumerate(line):
        if x in {0, len(line)-1}:
            continue
        if (char == bot.scaffold[y-1][x] == bot.scaffold[y+1][x] == '#' and
            bot.scaffold[y][x-1] == bot.scaffold[y][x+1] == '#'):
                total += (x * y)

print(f'Part 1: {total}') # 5788


# part 2
class Map:
    def __init__(self, grid):
        self.grid = grid
        self.x = 0
        self.y = 0
        self.direction = '^'
        self.steps = 0
        self.movement = []
        self.is_halted = False
    
    def find_position(self):
        '''Finds current position and create a dict of the scaffold'''
        self.scaffold = set()
        for y in range(len(self.grid)):
            for x in range(len(self.grid[0])):
                if self.grid[y][x] in {'^', 'v', '<', '>', '#'}:
                    self.scaffold.add((y, x))
                if self.grid[y][x] in {'^', 'v', '<', '>'}:
                    self.x = x
                    self.y = y
                    self.direction = self.grid[y][x]
    
    def move_front(self):
        if self.direction == '^':
            self.y -= 1
        elif self.direction == 'v':
            self.y += 1
        elif self.direction == '<':
            self.x -= 1
        elif self.direction == '>':
            self.x += 1

    def turn(self):
        if self.direction == '^':
            if (self.y, self.x-1) in self.scaffold:
                self.direction = '<'
                self.movement.append('L')
            elif (self.y, self.x+1) in self.scaffold:
                self.direction = '>'
                self.movement.append('R')
            else:
                self.is_halted = True
        elif self.direction == 'v':
            if (self.y, self.x-1) in self.scaffold:
                self.direction = '<'
                self.movement.append('R')
            elif (self.y, self.x+1) in self.scaffold:
                self.direction = '>'
                self.movement.append('L')
            else:
                self.is_halted = True

        elif self.direction == '<':
            if (self.y-1, self.x) in self.scaffold:
                self.direction = '^'
                self.movement.append('R')
            elif (self.y+1, self.x) in self.scaffold:
                self.direction = 'v'
                self.movement.append('L')
            else:
                self.is_halted = True
        elif self.direction == '>':
            if (self.y-1, self.x) in self.scaffold:
                self.direction = '^'
                self.movement.append('L')
            elif (self.y+1, self.x) in self.scaffold:
                self.direction = 'v'
                self.movement.append('R')
            else:
                self.is_halted = True
    
    def can_move_front(self):
        if self.direction == '^' and (self.y-1, self.x) in self.scaffold:
            return True
        elif self.direction == 'v' and (self.y+1, self.x) in self.scaffold:
            return True
        elif self.direction == '<' and (self.y, self.x-1) in self.scaffold:
            return True
        elif self.direction == '>' and (self.y, self.x+1) in self.scaffold:
            return True
        else:
            if self.steps:    
                self.movement.append(str(self.steps))
                self.steps = 0
            return False

def convert_to_input(routine):
    input_list = []
    for i in list(routine):
        input_list.append(ord(i))
    input_list += [10]
    return input_list

def compress_string(string, patterns):  # not a good algorithm, one edge case won't work
    if len(patterns) == 3:
        if string == '':
            return patterns
        else:
            return False
    else:
        remaining = 3 - len(patterns)
        for i in range(min(21, len(string))-remaining+1,-1,-1):
            if string[i] == ',' and ('0' <= string[i-1] <= '9'):
                new_str = string.replace(string[:i+1],'')
                patterns[string[:i+1]] = len(patterns)
                check_pattern = compress_string(new_str, patterns)
                if not check_pattern:
                    del patterns[string[:i+1]]
                    continue
                else:
                    return check_pattern
            else:
                continue

bot_map = Map(bot.scaffold)
bot_map.find_position()        
while not bot_map.is_halted:
    if bot_map.can_move_front():
        bot_map.move_front()
        bot_map.steps += 1
    else:
        bot_map.turn()

legend = {
    0: 'A',
    1: 'B',
    2: 'C'
}

movements = ','.join(bot_map.movement) + ','
patterns = compress_string(movements, {})
main = ''
while movements:
    for pattern in patterns:
        if movements.startswith(pattern):
            main += legend[patterns[pattern]] + ','
            movements = movements[len(pattern):]
main = main.strip(',')

for pattern, function in patterns.items():
    if function == 0:
        A = pattern.strip(',')
    elif function == 1:
        B = pattern.strip(',')
    elif function == 2:
        C = pattern.strip(',')

main_routine = convert_to_input(main)
pattern_A = convert_to_input(A)
pattern_B = convert_to_input(B)
pattern_C = convert_to_input(C)
show_visualization = False # change this to see the robot's path

bot.reset()
bot.program[0] = 2
dust = bot.run(main_routine, pattern_A, pattern_B, pattern_C, show_visualization)

if show_visualization:
    print(f'Part 1: {total}') # 5788
print(f'Part 2: {dust}') # 648545
print(f'Main Pattern: {main}') # A,B,A,B,C,B,C,A,B,C
print(f'Pattern A: {A}') # R,4,R,10,R,8,R,4
print(f'Pattern B: {B}') # R,10,R,6,R,4
print(f'Pattern C: {C}') # R,4,L,12,R,6,L,12
