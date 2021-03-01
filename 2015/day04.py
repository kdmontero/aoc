import hashlib

print('Advent of Code 2015 - Day 04')
key = 'ckczppom'

# part 1
i = 0
while True:
    value = key + str(i)
    md5_hash = hashlib.md5(value.encode())
    if md5_hash.hexdigest().startswith('00000'):
        break
    i += 1

print(f'Part 1: {i}') # 117946


# part 2
i = 0
while True:
    value = key + str(i)
    md5_hash = hashlib.md5(value.encode())
    if md5_hash.hexdigest().startswith('000000'):
        break
    i += 1

print(f'Part 2: {i}') # 3938038
