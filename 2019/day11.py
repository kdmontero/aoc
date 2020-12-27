with open('day11.txt') as f:
    intcode = [int(num) for num in f.read().split(',')]
intcode += [0]*1000

class Robot:
    def __init__(self):
        self.relbase = 0
        self.is_running = True
        self.color = None
        self.turn = None
        self.direction = 'UP'
        self.program = intcode[:]
        self.index = 0
        self.x = 0
        self.y = 0
    
    def run(self, input_color):
        opcode = lambda num: int(str(num)[-2:])
        mode1 = lambda num: int(str(num)[-3]) if len(str(num))>=3 else 0
        mode2 = lambda num: int(str(num)[-4]) if len(str(num))>=4 else 0
        mode3 = lambda num: int(str(num)[-5]) if len(str(num))>=5 else 0

        self.color = None
        self.turn = None
        i = self.index
        module = self.program
        while True:
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
                    module[module[i+1]] = input_color
                elif mode1(module[i]) == 2:
                    module[module[i+1]+self.relbase] = input_color
                i += 2
            elif opcode(module[i]) == 4:
                if mode1(module[i]) == 0:
                    if self.color == None:
                        self.color = module[module[i+1]]
                    else:
                        self.turn = module[module[i+1]]
                        self.index = i + 2
                        return
                elif mode1(module[i]) == 1:
                    if self.color == None:
                        self.color = module[i+1]
                    else:
                        self.turn = module[i+1]
                        self.index = i + 2
                        return
                elif mode1(module[i]) == 2:
                    if self.color == None:
                        self.color = module[module[i+1]+self.relbase]
                    else:
                        self.turn = module[module[i+1]+self.relbase]
                        self.index = i + 2
                        return
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
                self.is_running = False
                return
            else:
                print("Program is not working")
                return 

    def CW(self):
        if self.direction == 'UP':
            self.direction = 'RIGHT'
            self.x += 1
        elif self.direction == 'DOWN':
            self.direction = 'LEFT'
            self.x -= 1
        elif self.direction == 'LEFT':
            self.direction = 'UP'
            self.y -= 1
        elif self.direction == 'RIGHT':
            self.direction = 'DOWN'
            self.y += 1
        return

    def CCW(self):
        if self.direction == 'UP':
            self.direction = 'LEFT'
            self.x -= 1
        elif self.direction == 'DOWN':
            self.direction = 'RIGHT'
            self.x += 1
        elif self.direction == 'LEFT':
            self.direction = 'DOWN'
            self.y += 1
        elif self.direction == 'RIGHT':
            self.direction = 'UP'
            self.y -= 1
        return


# part 1
hull = {}
bot1 = Robot()
cur_pos = (bot1.y, bot1.x)
bot1.run(0)

while bot1.is_running:
    hull[cur_pos] = bot1.color
    if bot1.turn == 0:
        bot1.CCW()
    elif bot1.turn == 1:
        bot1.CW()
    cur_pos = (bot1.y, bot1.x)
    if cur_pos in hull:
        input_color = hull[cur_pos]
    else:
        input_color = 0
    bot1.run(input_color)

print(f'Part 1: {len(hull)}') # 2511


# part 2
bot2 = Robot()
cur_pos = (bot2.y, bot2.x)
bot2.run(1)
hull = {}
WHITE = '#'
BLACK = ' '
y_max = x_max = 0

while bot2.is_running:
    hull[cur_pos] = bot2.color
    y_max = max(y_max, bot2.y)
    x_max = max(x_max, bot2.x)
    if bot2.turn == 0:
        bot2.CCW()
    elif bot2.turn == 1:
        bot2.CW()
    cur_pos = (bot2.y, bot2.x)
    if cur_pos in hull:
        input_color = hull[cur_pos]
    else:
        input_color = 0
    bot2.run(input_color)

panel = []
for y in range(y_max+1):
    line = ""
    for x in range(x_max+1):
        if not hull.get((y, x)):
            line += BLACK
        else:
            line += WHITE
    panel.append(line)

print(f'Part 2: ') # HJKJKGPH
print(*panel, sep='\n')