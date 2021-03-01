print('Advent of Code 2015 - Day 23')
with open('day23.txt') as f:
    instructions = []
    for line in f.read().splitlines():
        if line.startswith('jio') or line.startswith('jie'):
            command, register, offset = line.replace(',', '').split(' ')
            instructions.append((command, register, int(offset)))
        elif line.startswith('jmp'):
            command, offset = line.split(' ')
            instructions.append((command, int(offset)))
        else:
            command, register = line.split(' ')
            instructions.append((command, register))

def run_program(a, b, instructions):
    registers = {'a': a, 'b': b}
    try:
        i = 0
        while True:
            command = instructions[i][0]
            if command == 'hlf':
                registers[instructions[i][1]] /= 2
            elif command == 'tpl':
                registers[instructions[i][1]] *= 3
            elif command == 'inc':
                registers[instructions[i][1]] += 1
            elif command == 'jmp':
                i += instructions[i][1]
                continue
            elif command == 'jie' and registers[instructions[i][1]] % 2 == 0:
                i += instructions[i][2]
                continue
            elif command == 'jio' and registers[instructions[i][1]] == 1:
                i += instructions[i][2]
                continue
            i += 1
    except IndexError:
        return registers['b']

print(f'Part 1: {run_program(0, 0, instructions)}') # 255 - part 1
print(f'Part 2: {run_program(1, 0, instructions)}') # 334 - part 2
