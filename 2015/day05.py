with open('day05.txt') as f:
    strings = f.read().splitlines()

bad_substring = ['ab', 'cd', 'pq', 'xy']

nice = 0
for string in strings:
    for substr in bad_substring:
        if substr in string:
            break
    else:
        vowels = 0
        has_double = False
        if string[0] in {'a', 'e', 'i', 'o', 'u'}:
            vowels += 1
        for i in range(1, len(string)):
            if string[i] in {'a', 'e', 'i', 'o', 'u'}:
                vowels += 1
            if string[i] == string[i-1]:
                has_double = True
        if vowels >= 3 and has_double:
            nice += 1
    
print(f'Part 1: {nice}') # 255


# part 2
nice = 0
for string in strings:
    rule_1 = False
    rule_2 = string[0] == string[2]
    pair = [string[:2], string[1:3]]
    for i in range(3, len(string)):
        if string[i] == string[i-2]:
            rule_2 = True
        if string[i-1:i+1] in pair[:i-2]:
            rule_1 = True
        pair.append(string[i-1:i+1])
    if rule_1 and rule_2:
        nice += 1
print(f'Part 2: {nice}') # 55