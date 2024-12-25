from collections.abc import Mapping
from copy import deepcopy


if __name__ == '__main__':
    print("Advent of Code 2018 - Day 16: Chronal Classification")

    with open('day16.txt') as f:
        raw_manual, raw_program = f.read().strip().split('\n\n\n')
        manuals = []
        for entry in raw_manual.split('\n\n'):
            raw_before, raw_instruction, raw_after = entry.splitlines()
            _, bef = raw_before.split(': ')
            before = {
                key: int(num) for key, num in 
                enumerate(bef.replace('[', '').replace(']', '').split(', '))
            }
            _, aft = raw_after.split(': ')
            after = {
                key: int(num) for key, num in 
                enumerate(aft.replace('[', '').replace(']', '').split(', '))
            }
            instruction = [int(num) for num in raw_instruction.split()]
            manuals.append([before, instruction, after])

        program = []
        for line in raw_program.strip().splitlines():
            entry = [int(num) for num in line.split()]
            program.append(entry)


    # part 1

    def execute(
        opcode: str,
        A: int,
        B: int,
        C: int,
        register: Mapping[int, int]
    ) -> Mapping[int, int]:

        if opcode == 'addr':
            register[C] = register[A] + register[B]
        elif opcode == 'addi':
            register[C] = register[A] + B
        elif opcode == 'mulr':
            register[C] = register[A] * register[B]
        elif opcode == 'muli':
            register[C] = register[A] * B
        elif opcode == 'banr':
            register[C] = register[A] & register[B]
        elif opcode == 'bani':
            register[C] = register[A] & B
        elif opcode == 'borr':
            register[C] = register[A] | register[B]
        elif opcode == 'bori':
            register[C] = register[A] | B
        elif opcode == 'setr':
            register[C] = register[A]
        elif opcode == 'seti':
            register[C] = A
        elif opcode == 'gtir':
            register[C] = int(A > register[B])
        elif opcode == 'gtri':
            register[C] = int(register[A] > B)
        elif opcode == 'gtrr':
            register[C] = int(register[A] > register[B])
        elif opcode == 'eqir':
            register[C] = int(A == register[B])
        elif opcode == 'eqri':
            register[C] = int(register[A] == B)
        elif opcode == 'eqrr':
            register[C] = int(register[A] == register[B])

        return register
            
    ins_names = ['addr', 'addi', 'mulr', 'muli', 'banr', 'bani', 'borr', 'bori',
        'setr', 'seti', 'gtir', 'gtri', 'gtrr', 'eqir', 'eqri', 'eqrr']

    ins_mapping = {}
    total = 0
    for manual in manuals:
        before, [opcode, A, B, C], after = manual
        count = 0
        possible_ins = set()
        for ins_name in ins_names:
            if execute(ins_name, A, B, C, deepcopy(before)) == after:
                possible_ins.add(ins_name)
                count += 1

        if opcode not in ins_mapping:
            ins_mapping[opcode] = possible_ins
        else:
            ins_mapping[opcode] &= possible_ins

        if count >= 3:
            total += 1

    print(f'Part 1: {total}') # 651


    # part 2

    real_ins = {}

    while len(real_ins) < 16:
        for opcode, instructions in ins_mapping.items():
            if len(instructions) == 1:
                true_instruction = instructions.pop()
                real_ins[opcode] = true_instruction
                break

        for instructions in ins_mapping.values():
            instructions -= {true_instruction}

    register = {num: 0 for num in range(4)}
    for entry in program:
        opcode, A, B, C = entry
        instruction = real_ins[opcode]
        execute(instruction, A, B, C, register)

    print(f'Part 2: {register[0]}') # 706

