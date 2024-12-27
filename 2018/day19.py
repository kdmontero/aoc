from collections.abc import Mapping


if __name__ == '__main__':
    print("Advent of Code 2018 - Day 19: Go With The Flow")

    with open('day19.txt') as f:
        instructions = []
        raw_binding, *raw_ins = f.read().strip().splitlines()

        _, ip = raw_binding.split()
        ip = int(ip)

        for line in raw_ins:
            command, A, B, C = line.split()
            instructions.append([command, int(A), int(B), int(C)])


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


    # part 1

    registers = {i: 0 for i in range(6)}
    pointer = 0
    while pointer < len(instructions):
        opcode, A, B, C = instructions[pointer]
        registers[ip] = pointer
        registers = execute(opcode, A, B, C, registers)
        pointer = registers[ip] + 1

    print(f'Part 1: {registers[0]}') # 1140


    # part 2

    print(f'Part 2: {0}') # 

