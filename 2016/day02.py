with open('day02.txt') as f:
    instructions = f.read().splitlines()

# part 1
keypad1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

keypad1_dict = {}
for y in range(len(keypad1)):
    for x in range(len(keypad1[0])):
        keypad1_dict[(y, x)] = keypad1[y][x]

def get_key(y, x, keypad_dict, dir):
    if direction == 'U':
        if (y-1, x) in keypad_dict:
            y -= 1
    elif direction == 'L':
        if (y, x-1) in keypad_dict:
            x -= 1
    elif direction == 'D':
        if (y+1, x) in keypad_dict:
            y += 1
    elif direction == 'R':
        if (y, x+1) in keypad_dict:
            x += 1
    return (y, x)

code1 = ''
y, x = 1, 1
for ins in instructions:
    for direction in ins:
        y, x = get_key(y, x, keypad1_dict, direction)
    code1 += str(keypad1_dict[(y, x)])

print(f'Part 1: {code1}') # 95549


# # part 2
keypad2 = [
    [0, 0, 1, 0, 0],
    [0, 2, 3, 4, 0],
    [5, 6, 7, 8, 9],
    [0, 'A', 'B', 'C', 0],
    [0, 0, 'D', 0, 0]
]

keypad2_dict = {}
for y in range(len(keypad2)):
    for x in range(len(keypad2[0])):
        if keypad2[y][x]:
            keypad2_dict[(y, x)] = keypad2[y][x]

code2 = ''
y, x = 2, 0
for ins in instructions:
    for direction in ins:
        y, x = get_key(y, x, keypad2_dict, direction)
    code2 += str(keypad2_dict[(y, x)])

print(f'Part 2: {code2}') # D87AD