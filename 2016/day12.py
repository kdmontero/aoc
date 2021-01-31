with open('day12.txt') as f:
    ins = [line.split(' ') for line in f.read().splitlines()]

def isinteger(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def reg_a(reg):
    i = 0
    while 0 <= i < len(ins):
        if ins[i][0] == 'inc':
            reg[ins[i][1]] += 1

        elif ins[i][0] == 'dec':
            reg[ins[i][1]] -= 1

        elif ins[i][0] == 'cpy':
            if isinteger(ins[i][1]):
                val = int(ins[i][1])
            else:
                val = reg[ins[i][1]]
            reg[ins[i][2]] = val

        elif ins[i][0] == 'jnz':
            if isinteger(ins[i][1]):
                val = int(ins[i][1])
            else:
                val = reg[ins[i][1]]
            if val != 0:
                if isinteger(ins[i][2]):
                    jump = int(ins[i][2])
                else:
                    jump = reg[ins[i][2]]
                i += jump
                continue

        i += 1

    return reg['a']

print(f"Part 1: {reg_a({'a': 0, 'b': 0, 'c': 0, 'd': 0})}") # 318020 - part 1
print(f"Part 2: {reg_a({'a': 0, 'b': 0, 'c': 1, 'd': 0})}") # 9227674 - part 2
