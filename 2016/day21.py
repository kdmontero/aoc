import collections

print("Advent of Code 2016 - Day 21: Scrambled Letters and Hash")
with open('day21.txt') as f:
    instructions = []
    for line in f.read().splitlines():
        if line.startswith('swap'):
            _, parameter, X, _, _, Y = line.split()
            if parameter == 'position':
                X, Y = int(X), int(Y)
            instructions.append(['swap', parameter, X, Y])

        elif line.startswith('rotate'):
            line = line.split()
            if len(line) == 4:
                instructions.append([line[0], line[1], int(line[2])])

            else:
                instructions.append([line[0], line[3], line[-1]])

        elif line.startswith('reverse'):
            _, _, X, _, Y = line.split()
            instructions.append(['reverse', int(X), int(Y)])

        elif line.startswith('move'):
            _, _, X, _, _, Y = line.split()
            instructions.append(['move', int(X), int(Y)])


# part 1
password1 = 'abcdefgh'

def swap(password, parameter, X, Y):
    if parameter == 'letter':
        X, Y = password.index(X), password.index(Y)

    password[X], password[Y] = password[Y], password[X]
    return password

def rotate(password, direction, X):
    password = collections.deque(password)
    if direction == 'left':
        X = -X

    elif direction == 'position':
        X = password.index(X)
        if X >= 4:
            X += 2
        else:
            X += 1

    password.rotate(X)
    return list(password)

def reverse(password, X, Y):
    return password[:X] + password[X:Y+1][::-1] + password[Y+1:]

def move(password, X, Y):
    letter = password.pop(X)
    password.insert(Y, letter)
    return password


password1 = list(password1)

for ins in instructions:
    if ins[0] == 'swap':
        password1 = swap(password1, ins[1], ins[2], ins[3])

    elif ins[0] == 'rotate':
        password1 = rotate(password1, ins[1], ins[2])

    elif ins[0] == 'reverse':
        password1 = reverse(password1, ins[1], ins[2])

    elif ins[0] == 'move':
        password1 = move(password1, ins[1], ins[2])

print(f'Part 1: {"".join(password1)}') # aefgbcdh


# part 2
password2 = 'fbgdceah'

def rotate_reverse(password, direction, X):
    password = collections.deque(password)
    if direction == 'right':
        X = -X

    elif direction == 'position':
        X = password.index(X)
        
        # brute force calculate the rotation for password with length 8
        rev_pos_rotate = { 
            1: 1,
            3: 2,
            5: 3,
            7: 4,
            2: 6,
            4: 7,
            6: 8,
            0: 9,
        }
        X = -rev_pos_rotate[X]

    password.rotate(X)
    return list(password)


password2 = list(password2)

for ins in instructions[::-1]:
    if ins[0] == 'swap':
        password2 = swap(password2, ins[1], ins[2], ins[3])

    elif ins[0] == 'rotate':
        password2 = rotate_reverse(password2, ins[1], ins[2])

    elif ins[0] == 'reverse':
        password2 = reverse(password2, ins[1], ins[2])

    elif ins[0] == 'move':
        password2 = move(password2, ins[2], ins[1])

print(f'Part 2: {"".join(password2)}') # egcdahbf
