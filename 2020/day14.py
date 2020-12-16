with open('day14.txt') as f:
    program = []
    temp_group = []
    for line in f.read().split('\n'):
        if line[:4] == 'mask':
            if temp_group:
                temp_group.append(values)
                program.append(temp_group)
                temp_group = []
            temp_group.append(line[7:])
            values = []
        else:
            address, value = line.replace('mem[', '').replace(
                ']', '').replace(' ', '').split('=')
            values.append((int(address), int(value)))
    temp_group.append(values)
    program.append(temp_group)

# part 1
def get_masked(mask, value):
    bin_value = list(format(value, '036b'))
    for i, digit in enumerate(mask):
        if digit != 'X':
            bin_value[i] = digit
    return int(''.join(bin_value), 2)

mem = {}
for group in program:
    mask = group[0]
    for address, value in group[1]:
        mem[address] = get_masked(mask, value)

print(f'Part 1: {sum(mem.values())}') # 12408060320841