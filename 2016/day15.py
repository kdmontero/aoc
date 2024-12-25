print("Advent of Code 2016 - Day 15: Timing is Everything")
with open('day15.txt') as f:
    discs1 = []
    for line in f.read().splitlines():
        words = line.rstrip('.').split(' ')
        disc = int(words[1][1:])
        pos = int(words[3])
        init = int(words[-1])
        discs1.append([disc, pos, init])

def get_timing(discs):
    i = 0
    while True:
        step = i
        for disc, pos, init in discs:
            step += 1
            if (init + step) % pos == 0:
                continue
            else:
                break
        else:
            break
        i += 1
    return i

# part 1
print(f'Part 1: {get_timing(discs1)}') # 122318 


# part 2
discs2 = discs1 + [[len(discs1) + 1, 11, 0]]
print(f'Part 2: {get_timing(discs2)}') # 3208583
