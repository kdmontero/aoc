from copy import deepcopy

print("Advent of Code 2020 - Day 08: Handheld Halting")
with open('day08.txt') as f:
    boot = [[ins[:3], int(ins[4:])] for ins in f.read().split('\n')]

# part 1
def run(boot):
    accumulator = i = 0
    done = set()
    while i < len(boot):
        op, arg = boot[i]
        if op == 'acc':
            accumulator += arg
            i += 1
        elif op == 'jmp':
            i += arg
        elif op == 'nop':
            i += 1
        if i in done:
            return (accumulator, False)
        done.add(i)
    return (accumulator, True)

print(f'Part 1: {run(boot)[0]}') # 1801


# part 2
for i in range(len(boot)):
    op = boot[i][0]
    if op == 'acc':
        continue
    boot_test = deepcopy(boot)
    if op == 'nop':
        boot_test[i][0] = 'jmp'
    elif op == 'jmp':
        boot_test[i][0] = 'nop'
    valid_acc, is_halted = run(boot_test)
    if is_halted:
        print(f'Part 2: {valid_acc}') # 2060
        break
