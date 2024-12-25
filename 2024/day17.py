from collections.abc import Mapping
from copy import deepcopy


if __name__ == '__main__':
    print("Advent of Code 2024 - Day 17: Chronospatial Computer")

    with open('day17.txt') as f:
        raw_registers, raw_program = f.read().strip().split('\n\n')
        reg = {}
        for line in raw_registers.splitlines():
            register, value = line.replace('Register ', '').split(': ')
            reg[register] = int(value)

        _, program = raw_program.split()
        program = program.split(',')

    def get_combo(operand: str, reg: Mapping[str, int]) -> int:
        if '0' <= operand <= '3':
            return int(operand)
        elif operand == '4':
            return reg['A']
        elif operand == '5':
            return reg['B']
        elif operand == '6':
            return reg['C']
        

    # part 1

    def execute(program: list[str], registers: Mapping[str, int]) -> str:
        pointer = 0
        output = []
        reg = deepcopy(registers)
        while pointer < len(program):
            opcode = program[pointer]
            if pointer + 1 >= len(program): # and opcode != '3':
                break
            operand = program[pointer + 1]

            if opcode == '0': # adv
                reg['A'] = reg['A'] // (2 ** get_combo(operand, reg))
                pointer += 2
            elif opcode == '1': # bxl
                reg['B'] = reg['B'] ^ int(operand)
                pointer += 2
            elif opcode == '2': # bst
                reg['B'] = get_combo(operand, reg) % 8
                pointer += 2
            elif opcode == '3': # jnz
                if reg['A'] != 0:
                    pointer = int(operand)
                else:
                    pointer += 2
            elif opcode == '4': # bxc
                reg['B'] = reg['B'] ^ reg['C']
                pointer += 2
            elif opcode == '5': # out
                output.append(get_combo(operand, reg) % 8)
                pointer += 2
            elif opcode == '6': # bdv
                reg['B'] = reg['A'] // (2 ** get_combo(operand, reg))
                pointer += 2
            elif opcode == '7': # cdv
                reg['C'] = reg['A'] // (2 ** get_combo(operand, reg))
                pointer += 2

        return ','.join([str(num) for num in output])

    print(f'Part 1: {execute(program, reg)}') # 4,1,5,3,1,5,3,5,7


    # part 2

    print(f'Part 2: {0}') #

