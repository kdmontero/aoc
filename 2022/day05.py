import re
import copy

if __name__ == '__main__':
    print("Advent of Code 2022 - Day 05: Supply Stacks")

    with open('day05.txt') as f:
        initial_stack, raw_instructions = f.read().split('\n\n')

    # parse the stack

    initial_stack = initial_stack.splitlines()[::-1]
    num_of_stack = int(initial_stack[0].split()[-1])

    orig_stack = {i: [] for i in range(1,num_of_stack+1)}

    for line in initial_stack[1:]:
        for stack_no, crate_index in enumerate(range(1, len(line), 4), 1):
            crate = line[crate_index]
            if crate != ' ':
                orig_stack[stack_no].append(crate)

    # parse the instructions

    raw_instructions = raw_instructions.splitlines()
    pattern = '\d+'
    instructions = []
    for line in raw_instructions:
        ins = []
        for num in re.findall(pattern, line):
            ins.append(int(num))
        instructions.append(ins)


    stack1 = copy.deepcopy(orig_stack)
    stack2 = copy.deepcopy(orig_stack)

    for instruction in instructions:
        qty, start, end = instruction

        for _ in range(qty):
            stack1[end].append(stack1[start].pop())

        stack2[end] += stack2[start][-qty:]
        del stack2[start][-qty:]


    top_crates1 = ''
    top_crates2 = ''
    for i in range(1, num_of_stack+1):
        top_crates1 += stack1[i][-1]
        top_crates2 += stack2[i][-1]

    print(f'Part 1: {top_crates1}') # TDCHVHJTG - part 1

    print(f'Part 2: {top_crates2}') # NGCMPJLHV - part 2
