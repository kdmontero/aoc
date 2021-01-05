import os
import time

with open('day15.txt') as f:
    intcode = [int(num) for num in f.read().split(',')]
intcode += [0]*1000

class RepairDroid:
    DROID = '@'
    PATH = '.'
    WALL = '#'
    OXYGEN = 'O'
    START = 'S'

    def __init__(self):
        self.relbase = 0
        self.found = None # steps it take to found the oxygen from initial position
        self.program = intcode[:]
        self.min_x = self.min_y = 0
        self.max_x = self.max_y = 1
        self.index = 0
        self.x = 0
        self.y = 0
        self.map = {(self.y, self.x): 0} # dict of no. of steps
        self.direction = 'UP'
        self.steps = 0
        self.maze = [[' ']*50 for _ in range(50)]
        self.maze[self.y][self.x] = RepairDroid.START

    @property
    def next_move(self):
        moveset = {
            'UP': 1,
            'DOWN': 2,
            'LEFT': 3,
            'RIGHT': 4
        }
        return moveset[self.direction]

    def check(self, command):
        opcode = lambda num: num%100
        mode1 = lambda num: num%1000 // 100 if num >= 100 else 0
        mode2 = lambda num: num%10000 // 1000 if num >= 1000 else 0
        mode3 = lambda num: num%100000 // 10000 if num >= 10000 else 0

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
                    module[module[i+1]] = command
                elif mode1(module[i]) == 2:
                    module[module[i+1]+self.relbase] = command
                i += 2
            elif opcode(module[i]) == 4:
                if mode1(module[i]) == 0:
                    status = module[module[i+1]]
                elif mode1(module[i]) == 1:
                    status = module[i+1]
                elif mode1(module[i]) == 2:
                    status = module[module[i+1]+self.relbase]              
                self.index = i + 2
                return status
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

    def turn_CW(self):
        if self.direction == 'UP':
            self.direction = 'RIGHT'
        elif self.direction == 'DOWN':
            self.direction = 'LEFT'
        elif self.direction == 'LEFT':
            self.direction = 'UP'
        elif self.direction == 'RIGHT':
            self.direction = 'DOWN'
        return

    def turn_CCW(self):
        if self.direction == 'UP':
            self.direction = 'LEFT'
        elif self.direction == 'DOWN':
            self.direction = 'RIGHT'
        elif self.direction == 'LEFT':
            self.direction = 'DOWN'
        elif self.direction == 'RIGHT':
            self.direction = 'UP'
        return

    def is_right_wall(self):
        if any((
            self.direction == 'UP' and self.maze[self.y][self.x+1] == RepairDroid.WALL,
            self.direction == 'DOWN' and self.maze[self.y][self.x-1] == RepairDroid.WALL,
            self.direction == 'RIGHT' and self.maze[self.y+1][self.x] == RepairDroid.WALL,
            self.direction == 'LEFT' and self.maze[self.y-1][self.x] == RepairDroid.WALL
        )):
            return True
        return False

    def print_maze(self):
        os.system("clear")
        for line in self.maze:
            print(''.join(line))

    def reset_steps(self):
        self.maze = [[' ']*(self.x_range) for _ in range(self.y_range)]
        self.steps = 0
        self.map = {(self.y, self.x): 0} 
        self.maze[self.y][self.x] = RepairDroid.START

    def set_offset_range(self):
        self.x_offset = -self.min_x
        self.y_offset = -self.min_y
        self.x_range = self.max_x - self.min_x + 1
        self.y_range = self.max_y - self.min_y + 1

    def explore(self, show_animation=False, stop_when_found=False):
        i = 0
        self.found = None
        while i < 3000:
            i += 1
            self.min_y = min(self.y-1, self.min_y)
            self.min_x = min(self.x-1, self.min_x)
            self.max_y = max(self.y+1, self.max_y)
            self.max_x = max(self.x+1, self.max_x)
            if not self.is_right_wall():
                self.turn_CW()
            command = self.next_move
            status = self.check(command)
            if status == 0:
                if command == 1:
                    self.maze[self.y-1][self.x] = RepairDroid.WALL
                elif command == 2:
                    self.maze[self.y+1][self.x] = RepairDroid.WALL
                elif command == 3:
                    self.maze[self.y][self.x-1] = RepairDroid.WALL
                elif command == 4:
                    self.maze[self.y][self.x+1] = RepairDroid.WALL
                self.turn_CCW()
            elif status == 1:
                if self.maze[self.y][self.x] not in {RepairDroid.OXYGEN, RepairDroid.START}:
                    self.maze[self.y][self.x] = RepairDroid.PATH
                if command == 1:
                    self.y -= 1
                elif command == 2:
                    self.y += 1
                elif command == 3:
                    self.x -= 1
                elif command == 4:
                    self.x += 1
                if (self.y, self.x) not in self.map:
                    self.steps += 1
                    self.map[(self.y, self.x)] = self.steps
                else:
                    self.steps = self.map[(self.y, self.x)]
                if self.maze[self.y][self.x] not in {RepairDroid.OXYGEN, RepairDroid.START}:
                    self.maze[self.y][self.x] = RepairDroid.DROID
            elif status == 2:
                self.maze[self.y][self.x] = RepairDroid.PATH
                if command == 1:
                    self.y -= 1
                elif command == 2:
                    self.y += 1
                elif command == 3:
                    self.x -= 1
                elif command == 4:
                    self.x += 1
                self.steps += 1
                self.maze[self.y][self.x] = RepairDroid.OXYGEN
                self.found = self.steps
            if show_animation:
                self.print_maze()
                time.sleep(0.015)
            if stop_when_found and self.found:
                break

# part 1
droid = RepairDroid()
droid.explore()
# Find first the offset since we do not know the starting position
# of the droid relative to the whole maze 
droid.set_offset_range()

show_part_1 = False # toogle here to see animation
droid.y, droid.x = droid.y_offset, droid.x_offset
droid.reset_steps()
droid.program = intcode[:] # return to original starting point
droid.explore(show_part_1, True)
oxygen_steps = droid.found
print(f'Part 1: {oxygen_steps}')


# part 2
show_part_2 = False # toogle here to see animation
droid.reset_steps()
droid.explore(show_part_2)
if show_part_2:
    print(f'Part 1: {oxygen_steps}')
print(f'Part 2: {max(droid.map.values())}')


# # Part 1 animation
# droid = RepairDroid()
# droid.explore()
# droid.set_offset_range()
# droid.y, droid.x = droid.y_offset, droid.x_offset
# droid.reset_steps()
# droid.program = intcode[:] # return to original starting point
# droid.explore(True)