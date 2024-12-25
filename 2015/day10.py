INPUT = '1321131112'

print("Advent of Code 2015 - Day 10: Elves Look, Elves Say")
def get_conway_length(start, turns):
    for _ in range(turns):
        next_num = ''
        count = 0
        i = 0
        current_num = start[0]
        while i < len(start):
            if start[i] == current_num:
                count += 1
            else:
                next_num += str(count) + current_num
                count = 0
                current_num = start[i]
                continue
            i += 1
        next_num += str(count) + current_num
        start = next_num
    return start, len(start)

# part 1
ans1, length1 = get_conway_length(INPUT, 40)
print(f'Part 1: {length1}') # 492982


# part 2
print(f'Part 2: {get_conway_length(ans1, 10)[1]}') # 6989950
