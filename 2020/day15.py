given = '8,11,0,19,1,2'
start = [int(i) for i in given.split(',')]

def memory_game(start, target):
    spoken = {}
    turn = 0
    current = None
    while turn < target:
        previous = current
        if turn < len(start):
            current = start[turn]
        else:
            if previous not in spoken:
                current = 0
            else:
                current = turn - spoken[previous]
        spoken[previous] = turn
        turn += 1
    return current

print(f'Part 1: {memory_game(start, 2020)}') # 447
print(f'Part 2: {memory_game(start, 30000000)}') # 11721679