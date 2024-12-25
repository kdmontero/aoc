print("Advent of Code 2015 - Day 08: Matchsticks")
with open('day08.txt') as f:
    strings = []
    y = 0
    for string in f.read().splitlines():
        strings.append(string)

# part 1
disregard = 0
for string in strings:
    i = 1
    disregard += 2
    while i < len(string) - 1:
        if string[i] == '\\':
            if string[i+1] == 'x':
                i += 3
                disregard += 3
                continue
            else:
                disregard += 1
                i += 2
                continue
        i += 1

print(f'Part 1: {disregard}') # 1371


# part 2
additional = 0
for string in strings:
    additional += 2
    additional += string.count('\\') + string.count('"')

print(f'Part 2: {additional}') # 2117
