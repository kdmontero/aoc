from collections import defaultdict

print('Advent of Code 2017 - Day 08')

with open('day08.txt') as f:
    raw_ins = []
    for line in f.readlines():
        raw_ins.append(line.replace('if','').split())


registers = defaultdict(int)

def condition(reg, equality, num):
    if equality == '==':
        if registers[reg] == int(num):
            return True
    elif equality == '<':
        if registers[reg] < int(num):
            return True
    elif equality == '>':
        if registers[reg] > int(num):
            return True
    elif equality == '<=':
        if registers[reg] <= int(num):
            return True
    elif equality == '>=':
        if registers[reg] >= int(num):
            return True
    elif equality == '!=':
        if registers[reg] != int(num):
            return True
    return False

max_val = 0
for r, change, val, reg, equality, num in raw_ins:
    if condition(reg, equality, num):
        if change == 'inc':
            registers[r] += int(val)
        elif change == 'dec':
            registers[r] -= int(val)
        max_val = max(registers[r], max_val)

print(f'Part 1: {max(registers.values())}') # 4448 - part 1

print(f'Part 2: {max_val}') # 6582 - part 2
