print("Advent of Code 2016 - Day 16: Dragon Checksum")
INPUT = '01111001100111011'
LENGTH1 = 272
LENGTH2 = 35651584

def dragon_curve(data, length):
    while len(data) < length:
        b = data.replace('0', '2').replace('1', '0').replace('2', '1')
        data = data + '0' + b[::-1]

    return data[:length]


def get_checksum(given_data):
    checksum = ''
    for i in range(0, len(given_data), 2):
        if given_data[i] == given_data[i+1]:
            checksum += '1'
        else:
            checksum += '0'
    return checksum


# part 1
data1 = dragon_curve(INPUT, LENGTH1)
checksum1 = get_checksum(data1)
while len(checksum1) % 2 != 1:
    checksum1 = get_checksum(checksum1)

print(f'Part 1: {checksum1}') # 11111000111110000


# part 2
data2 = dragon_curve(INPUT, LENGTH2)
checksum2 = get_checksum(data2)
while len(checksum2) % 2 != 1:
    checksum2 = get_checksum(checksum2)

print(f'Part 2: {checksum2}') # 10111100110110100
