print('Advent of Code 2019 - Day 19')
with open('day19.txt') as given:
    intcode = [int(num) for num in given.read().split(',')]

intcode += [0]*10000

class TractorBeam:
    def __init__(self):
        self.relbase = 0
        self.index = 0
        self.program = intcode[:]
    
    def check(self, y, x):
        opcode = lambda num: num%100
        mode1 = lambda num: num%1000 // 100 if num >= 100 else 0
        mode2 = lambda num: num%10000 // 1000 if num >= 1000 else 0
        mode3 = lambda num: num%100000 // 10000 if num >= 10000 else 0

        i = self.index
        module = self.program
        input_list = [x, y]

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
                i += 2
                self.index = i
                return output
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
                return
            else:
                print("Program is not working")
                return


# part 1
path = [[' ']*50 for _ in range(50)]
affected = 0
first_beam_x = first_beam_y = 0
y = x = x_ref = 0
while y < 50:
    if not TractorBeam().check(y, x):
        if x >= 50:
            x = x_ref
        else:    
            x += 1
            continue
    else:
        if not (first_beam_x and first_beam_y) and (y, x) != (0, 0):
            first_beam_x = x
            first_beam_y = y
        affected += 1
        x_ref = x
        x += 1
        while x < 50:
            if TractorBeam().check(y, x):
                affected += 1
            else:
                x = x_ref
                break
            x += 1
    y += 1

print(f'Part 1: {affected}') # 183


# part 2
x = first_beam_x
y = first_beam_y
while True:
    if TractorBeam().check(y, x):
        if x < 100 or y < 100:
            pass
        elif TractorBeam().check(y-99, x) and TractorBeam().check(y-99, x+99):
            y -= 99
            break
        y += 1
    else:
        x += 1

print(f'Part 2: {x*10000+y}') # 11221248
