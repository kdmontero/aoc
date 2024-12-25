from collections import Counter

print("Advent of Code 2016 - Day 04: Security Through Obscurity")
with open('day04.txt') as f:
    rooms = []
    for room in f.read().splitlines():
        room = room.rstrip(']').replace('[', '-').split('-')
        checksum = room.pop(-1)
        id_ = int(room.pop(-1))
        name = '-'.join(room)
        rooms.append([name, id_, checksum])

# part 1
def get_checksum(name):
    c = Counter(name.replace('-', ''))
    arrange = sorted(c.items(), key=lambda x: (-x[1], x[0]))
    checksum = [letter[0] for letter in arrange[0:5]]
    return ''.join(checksum)

ids = 0
real = []
for room in rooms:
    name, id_, checksum = room
    if checksum == get_checksum(name):
        ids += id_
        real.append(room)

print(f'Part 1: {ids}') # 137896


# part 2
def decrypt(name, cipher):
    ans = ''
    cipher = cipher % 26
    for char in name:
        if char == '-':
            ans += char
        else:
            real_ord = ord(char) + cipher
            if real_ord > ord('z'):
                real_ord = ord('a') + real_ord - ord('z') - 1
            ans += chr(real_ord)
    return ans

sector_id = None
for room in real:
    real_name = decrypt(room[0], room[1])
    if 'north' in real_name:
        sector_id = room[1]
        break

print(f'Part 2: {sector_id} ({real_name})') # 501 (northpole-object-storage)
