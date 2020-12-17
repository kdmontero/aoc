import itertools

with open('day14.txt') as f:
    program = []
    temp_group = []
    for line in f.read().split('\n'):
        if line.startswith('mask'):
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
def masked_value(mask, value):
    bin_value = list(format(value, '036b'))
    for i, digit in enumerate(mask):
        if digit != 'X':
            bin_value[i] = digit
    return int(''.join(bin_value), 2)

mem = {}
for group in program:
    mask = group[0]
    for address, value in group[1]:
        mem[address] = masked_value(mask, value)

print(f'Part 1: {sum(mem.values())}') # 12408060320841


# part 2
def masked_address(mask, address):
    bin_value = list(format(address, '036b'))
    for i, digit in enumerate(mask):
        if digit != '0':
            bin_value[i] = digit
    return ''.join(bin_value)

def get_addresses(masked_addr):
    floating = masked_addr.count('X')
    combinations = [list(i) for i in itertools.product(['0','1'], repeat=floating)]
    addresses = []
    for comb in combinations:
        temp_addr = masked_addr
        for digit in comb:
            temp_addr = temp_addr.replace('X', digit, 1)
        addresses.append(int(temp_addr, 2))
    return addresses

mem = {}
for group in program:
    mask = group[0]
    for address, value in group[1]:
        addresses = get_addresses(masked_address(mask, address))
        for addr in addresses:
            mem[addr] = value

print(f'Part 2: {sum(mem.values())}') # 4466434626828