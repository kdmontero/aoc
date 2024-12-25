import os
import time
import copy

print("Advent of Code 2019 - Day 15: Oxygen System")
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
        self.oxygen_steps = 0
        self.program = intcode[:]
        self.min_x = self.min_y = 0
        self.max_x = self.max_y = 0
        self.index = 0
        self.x = 0
        self.y = 0
        self.map = {(0, 0): [RepairDroid.START, 0]} # dict char and steps
        self.steps = 0
        self.moves = []

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

    @property
    def maze(self):
        x_offset = self.max_x-self.min_x
        y_offset = self.max_y-self.min_y
        maze = [[' ']*(x_offset+1) for _ in range((y_offset+1))]
        for (y, x), (char, _) in self.map.items():
            if y == self.y and x == self.x:
                maze[y-self.min_y][x-self.min_x] = RepairDroid.DROID
            else:
                maze[y-self.min_y][x-self.min_x] = char
        return maze

    def print_maze(self):
        os.system("clear")
        for line in self.maze:
            print(''.join(line))
        time.sleep(0.02)

    def turn_back(self): # turn back 1 step
        previous_move = self.moves.pop()
        if previous_move == 1:
            move = 2
            self.y += 1
        elif previous_move == 2:
            move = 1
            self.y -= 1
        elif previous_move == 3:
            move = 4
            self.x += 1
        elif previous_move == 4:
            move = 3
            self.x -= 1
        return move

    def all_n_visited(self):
        if all((
            (self.y+1, self.x) in self.map,
            (self.y-1, self.x) in self.map,
            (self.y, self.x+1) in self.map,
            (self.y, self.x-1) in self.map
        )):
            return True
        return False

    def explore(self, show_animation=False):
        mapped = False
        while not mapped:
            if (self.y-1, self.x) not in self.map:
                command = 1
                self.y -= 1
                self.min_y = min(self.min_y, self.y)
            elif (self.y, self.x+1) not in self.map:
                command = 4
                self.x += 1
                self.max_x = max(self.max_x, self.x)
            elif (self.y+1, self.x) not in self.map:
                command = 2
                self.y += 1
                self.max_y = max(self.max_y, self.y)
            elif (self.y, self.x-1) not in self.map:
                command = 3
                self.x -= 1
                self.min_x = min(self.min_x, self.x)
            else:
                while self.all_n_visited():
                    if self.moves:
                        moveback = self.turn_back()
                        self.check(moveback)
                        self.steps = self.map[(self.y, self.x)][1]
                        if show_animation:
                            self.print_maze()
                    else:
                        mapped = True
                        break
                continue

            self.moves.append(command)
            status = self.check(command)
            if status == 0:
                self.map[(self.y, self.x)] = [RepairDroid.WALL, 'INF']
                self.turn_back()
            elif status == 1:
                self.steps += 1
                self.map[(self.y, self.x)] = [RepairDroid.PATH, self.steps]
            elif status == 2:
                self.steps += 1
                self.map[(self.y, self.x)] = [RepairDroid.OXYGEN, self.steps]
                self.oxygen_steps = self.steps

            if show_animation:
                self.print_maze()


# part 1
show_animation = False # CHANGE HERE TO SEE THE ANIMATION
droid = RepairDroid()
droid.explore(show_animation)
droid.x, droid.y = 0, 0

visited = {}
stack = [(0, 0, 0)]
while True:
    y, x, steps = stack.pop()
    droid.y, droid.x = y, x
    if (y, x) not in visited:
        visited[(y,x)] = steps
    else:
        continue

    if show_animation:
        droid.print_maze()

    if droid.map[(y, x)][0] == RepairDroid.OXYGEN:
        oxygen_steps = steps
        break
    neighbors = [(y+1, x), (y-1, x), (y, x+1), (y, x-1)]
    for neighbor in neighbors:
        if (droid.map[neighbor][0] in {RepairDroid.PATH, RepairDroid.OXYGEN} and
        neighbor not in visited):
            stack.append((*neighbor, steps+1))


# part 2
queue = [(droid.y, droid.x)]
time_filled = 0
while queue:
    temp_queue = []
    for y, x in queue:
        droid.y, droid.x = y, x
        droid.map[(y,x)][0] = RepairDroid.OXYGEN
        neighbors = [(y+1, x), (y-1, x), (y, x+1), (y, x-1)]
        for neighbor in neighbors:
            if droid.map[neighbor][0] in {RepairDroid.PATH, RepairDroid.START}:
                temp_queue.append(neighbor)
    if show_animation:
        droid.print_maze()
    
    queue = temp_queue
    if temp_queue:
        time_filled += 1

print(f'Part 1: {oxygen_steps}')
print(f'Part 2: {time_filled}')
