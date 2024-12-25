print("Advent of Code 2019 - Day 05: Sunny with a Chance of Asteroids")
with open('day05.txt') as given:
    program = [int(num) for num in given.read().split(',')]

def run(program, input_num):
    # opcode = lambda num: int(str(num)[-2:])
    # mode1 = lambda num: int(str(num)[-3]) if len(str(num))>=3 else 0
    # mode2 = lambda num: int(str(num)[-4]) if len(str(num))>=4 else 0

    opcode = lambda num: num%100
    mode1 = lambda num: num%1000 // 100 if num >= 100 else 0
    mode2 = lambda num: num%10000 // 1000 if num >= 1000 else 0

    i=0
    while i < len(program)+1:
        if opcode(program[i]) == 1:
            if mode1(program[i]) == 1:
                parameter1 = program[i+1]
            elif mode1(program[i]) == 0:
                parameter1 = program[program[i+1]]
            if mode2(program[i]) == 1:
                parameter2 = program[i+2]
            elif mode2(program[i]) == 0:
                parameter2 = program[program[i+2]]
            program[program[i+3]] = parameter1 + parameter2
            i += 4
        elif opcode(program[i]) == 2:
            if mode1(program[i]) == 1:
                parameter1 = program[i+1]
            elif mode1(program[i]) == 0:
                parameter1 = program[program[i+1]]
            if mode2(program[i]) == 1:
                parameter2 = program[i+2]
            elif mode2(program[i]) == 0:
                parameter2 = program[program[i+2]]
            program[program[i+3]] = parameter1 * parameter2
            i += 4
        elif opcode(program[i]) == 3:
            program[program[i+1]] = input_num
            i += 2
        elif opcode(program[i]) == 4:
            output = program[program[i+1]]
            i += 2
        elif opcode(program[i]) == 5:
            if mode1(program[i]) == 1:
                parameter1 = program[i+1]
            elif mode1(program[i]) == 0:
                parameter1 = program[program[i+1]]
            if mode2(program[i]) == 1:
                parameter2 = program[i+2]
            elif mode2(program[i]) == 0:
                parameter2 = program[program[i+2]]
            if parameter1 != 0:
                i = parameter2
            else:
                i += 3
        elif opcode(program[i]) == 6:
            if mode1(program[i]) == 1:
                parameter1 = program[i+1]
            elif mode1(program[i]) == 0:
                parameter1 = program[program[i+1]]
            if mode2(program[i]) == 1:
                parameter2 = program[i+2]
            elif mode2(program[i]) == 0:
                parameter2 = program[program[i+2]]
            if parameter1 == 0:
                i = parameter2
            else:
                i += 3
        elif opcode(program[i]) == 7:
            if mode1(program[i]) == 1:
                parameter1 = program[i+1]
            elif mode1(program[i]) == 0:
                parameter1 = program[program[i+1]]
            if mode2(program[i]) == 1:
                parameter2 = program[i+2]
            elif mode2(program[i]) == 0:
                parameter2 = program[program[i+2]]
            if parameter1 < parameter2:
                program[program[i+3]] = 1
            else:
                program[program[i+3]] = 0
            i += 4
        elif opcode(program[i]) == 8:
            if mode1(program[i]) == 1:
                parameter1 = program[i+1]
            elif mode1(program[i]) == 0:
                parameter1 = program[program[i+1]]
            if mode2(program[i]) == 1:
                parameter2 = program[i+2]
            elif mode2(program[i]) == 0:
                parameter2 = program[program[i+2]]
            if parameter1 == parameter2:
                program[program[i+3]] = 1
            else:
                program[program[i+3]] = 0
            i += 4
        elif opcode(program[i]) == 99:
            return output
        else:
            print('Program not working')
            break

program1 = program[:]
input1 = 1
print(f'Part 1: {run(program1, input1)}') # 7692125

program2 = program[:]
input2 = 5
print(f'Part 2: {run(program2, input2)}') # 14340395
