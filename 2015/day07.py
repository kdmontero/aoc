print("Advent of Code 2015 - Day 07: Some Assembly Required")
with open('day07.txt') as f:
    instructions = {}
    for ins in f.read().splitlines():
        formula, key = ins.split(' -> ')
        formula = formula.split(' ')
        if len(formula) == 1:
            instructions[key] = ('DIRECT', formula)
        elif len(formula) == 2:
            instructions[key] = (formula[0], formula[1:])
        elif len(formula) == 3:
            instructions[key] = (formula[1], formula[0:3:2])

def get_signal(wire):
    if wire in cache:
        return cache[wire]
    operator, parts = instructions[wire]
    if operator == 'DIRECT':
        if parts[0].isdigit():
            signal = int(parts[0])
        else:
            signal = get_signal(parts[0])
    elif operator == 'NOT':
        if parts[0].isdigit():
            signal = BIT_SIZE - int(parts[0])
        else:
            signal = BIT_SIZE - get_signal(parts[0])
    elif operator == 'RSHIFT':
        num, shift = parts
        if num.isdigit():
            signal = int(num) >> int(shift)
        else:
            signal = get_signal(num) >> int(shift)
    elif operator == 'LSHIFT':
        num, shift = parts
        if num.isdigit():
            signal = int(num) << int(shift)
        else:
            signal = get_signal(num) << int(shift)
    elif operator == 'OR':
        num1, num2 = parts
        if num1.isdigit():
            num1 = int(num1)
        else:
            num1 = get_signal(num1)
        if num2.isdigit():
            num2 = int(num2)
        else:
            num2 = get_signal(num2)
        signal = num1 | num2
    elif operator == 'AND':
        num1, num2 = parts
        if num1.isdigit():
            num1 = int(num1)
        else:
            num1 = get_signal(num1)
        if num2.isdigit():
            num2 = int(num2)
        else:
            num2 = get_signal(num2)
        signal = num1 & num2
    cache[wire] = signal
    return signal

# part 1
cache = {}
BIT_SIZE = 65535
signal_a = get_signal('a')
print(f'Part 1: {signal_a}') # 46065


# part 2
cache.clear()
cache['b'] = signal_a
print(f'Part 2: {get_signal("a")}') # 14134
