print("Advent of Code 2020 - Day 25: Combo Breaker")
with open('day25.txt') as f:
    card_key, door_key = [int(num) for num in f.read().splitlines()]

# part 1
def transform(sub_num, loop):
    key = 1
    for _ in range(loop):
        key = (sub_num*key) % 20201227
    return key

def find_loop(sub_num, public_key):
    key = 1
    loop = 0
    while key != public_key:
        key = (7*key) % 20201227
        loop += 1
    return loop

card_loop = find_loop(7, card_key)
door_loop = find_loop(7, door_key)
loop = min(card_loop, door_loop) # check only the shortest loop

if loop == card_loop:
    encryption_key = transform(door_key, card_loop)
elif loop == door_loop:
    encryption_key = transform(card_key, door_loop)

print(f'Part 1: {encryption_key}') # 7936032


# part 2
print('Part 2: Complete all 49 stars in Advent of Code 2020')
