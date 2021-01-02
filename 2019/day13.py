import os

with open('day13.txt') as given:
	intcode = [int(num) for num in given.read().split(',')]

intcode += [0]*1000

class Arcade:
    SPACE = ' '
    BALL = 'o'
    PADDLE = '='
    BLOCKS = '#'
    WALL = 'I'
    board_height = 25 # found thru trial and error
    board_width = 36 # found thru trial and error

    def __init__(self):
        self.relbase = 0
        self.program = intcode[:]
        self.index = 0
        self.ball = 0 # x coordinate of paddle
        self.paddle = 0 # x coordinate of paddle
        self.score = 0
        self.blocks = 0
        self.board = [[Arcade.SPACE]*Arcade.board_width
            for _ in range(Arcade.board_height)]

    def run(self, show_animation=False):
        opcode = lambda num: num % 100
        mode1 = lambda num: divmod(num%1000, 100)[0] if num >= 100 else 0
        mode2 = lambda num: divmod(num%10000, 1000)[0] if num >= 1000 else 0
        mode3 = lambda num: divmod(num%100000, 10000)[0] if num >= 10000 else 0

        char = {
            0: Arcade.SPACE,
            1: Arcade.WALL,
            2: Arcade.BLOCKS,
            3: Arcade.PADDLE,
            4: Arcade.BALL
        }

        sequence = []
        i = self.index
        module = self.program
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
                    module[module[i+1]] = self.ball - self.paddle
                elif mode1(module[i]) == 2:
                    module[module[i+1]+self.relbase] = self.ball - self.paddle
                i += 2
            elif opcode(module[i]) == 4:
                if mode1(module[i]) == 0:
                    sequence.append(module[module[i+1]])
                elif mode1(module[i]) == 1:
                    sequence.append(module[i+1])
                elif mode1(module[i]) == 2:
                    sequence.append(module[module[i+1]+self.relbase])
                
                if len(sequence) == 3:
                    x, y, obj = sequence
                    if obj == 3:
                        self.paddle = x
                    elif obj == 4:
                        self.ball = x

                    if y == 0 and x == -1:
                        if self.score != obj:
                            self.blocks -= 1
                        self.score = obj
                    else:
                        self.board[y][x] = char[obj]
                    if show_animation:
                        self.print_board()
                    sequence = []
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
                return
            else:
                print("Program is not working")
                return

    def print_board(self):
        os.system("clear")
        text_width = len(f"Score is {self.score} Blocks {self.blocks}")
        spaces = Arcade.board_width - text_width
        print(f"Score is {self.score} {' '*spaces}Blocks {self.blocks}")
        for h in range(len(self.board)):
            print(''.join(self.board[h]))

    def count_blocks(self):
        total = 0
        for line in self.board:
            total += line.count(Arcade.BLOCKS)
        self.blocks = total
        return total

# part 1
arcade1 = Arcade()
arcade1.run()
arcade1.count_blocks()
print(f'Part 1: {arcade1.blocks}') # 213


# part 2
show_animation = False # edit here to show or hide animation
arcade2 = Arcade()
arcade2.program[0] = 2
arcade2.blocks = arcade1.blocks
arcade2.run(show_animation)
if show_animation:
    print(f'Part 1: {arcade1.blocks}') # 213
print(f'Part 2: {arcade2.score}') # 11441