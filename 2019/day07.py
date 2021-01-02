import itertools

with open('day07.txt') as given:
    software = [int(num) for num in given.read().split(',')]

class Amplifier:
    def __init__(self, phase):
        self.phase = int(phase)
        self.index = 0
        self.program = software[:]
        self.output = None
        self.is_halted = False
        self.is_phase = False

    def run(self, input_signal):
        opcode = lambda num: num%100
        mode1 = lambda num: divmod(num%1000, 100)[0] if num >= 100 else 0
        mode2 = lambda num: divmod(num%10000, 1000)[0] if num >= 1000 else 0

        program = self.program
        i = self.index
        while i < len(program):
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
                if not self.is_phase:
                    program[program[i+1]] = self.phase
                    self.is_phase = True
                else:
                    program[program[i+1]] = input_signal
                i += 2
            elif opcode(program[i]) == 4:
                self.output = program[program[i+1]]
                i += 2
                self.index = i
                return
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
                self.is_halted = True
                return
            else:
                print('Program not working')
                break
    
# part 1
settings = list(itertools.permutations('01234', 5))
high_signal = 0
for ph in settings:
    A = Amplifier(int(ph[0]))
    B = Amplifier(int(ph[1]))
    C = Amplifier(int(ph[2]))
    D = Amplifier(int(ph[3]))
    E = Amplifier(int(ph[4]))
    A.run(0)
    B.run(A.output)
    C.run(B.output)
    D.run(C.output)
    E.run(D.output)
    if E.output > high_signal:
        high_signal = E.output

print(f'Part 1: {high_signal}') # 47064


# part 2
settings = list(itertools.permutations('56789', 5))
best_setting = None
max_signal = 0
for ph in settings:
    A = Amplifier(int(ph[0]))
    B = Amplifier(int(ph[1]))
    C = Amplifier(int(ph[2]))
    D = Amplifier(int(ph[3]))
    E = Amplifier(int(ph[4]))
    amps = [A, B, C, D, E]
    A.run(0)
    halted = False
    i = 1
    while not halted:
        amps[i].run(amps[i-1].output)
        halted = amps[i].is_halted
        if max_signal < amps[i].output:
            max_signal = amps[i].output
            best_setting = ''.join(ph)
        if any([amp.is_halted for amp in amps]) and i == 4:
            halted = True
        i += 1
        if i == 5:
            i = 0

print(f"Part 2: {max_signal} (with phase setting {best_setting})") # 4248984 with phase setting 65987