import collections

print("Advent of Code 2015 - Day 11: Corporate Policy")
INPUT = 'hepxcrrq'

def check1(pw):
    for i in range(len(pw[:-2])):
        if ord(pw[i]) == ord(pw[i+1])-1 == ord(pw[i+2])-2:
            break
    else:
        return False
    return True

def check2(pw):
    if pw.count('i') + pw.count('o') + pw.count('l'):
        return False
    return True

def check3(pw):
    i = 1
    pairs = collections.Counter()
    while i < len(pw):
        if pw[i] == pw[i-1]:
            pairs[pw[i]] += 1
            i += 2
            continue
        i += 1
    if len(pairs) >= 2:
            return True
    return False

def next_pw(pw):
    if 'i' in pw:
        return pw.replace('i', 'j')
    if 'o' in pw:
        return pw.replace('o', 'p')
    if 'l' in pw:
        return pw.replace('l', 'm')
    if pw[-1] != 'z':
        return pw[:-1] + chr(ord(pw[-1])+1)
    elif pw.strip('z') == '':
        return 'a' * len(pw)
    else:
        count_z = len(pw) - len(pw.rstrip('z'))
        mid = len(pw) - count_z - 1
        return pw[:mid] + chr(ord(pw[mid])+1) + 'a'*count_z

def next_valid(pw):
    while True:
        new_pw = next_pw(pw)
        if check1(new_pw) and check2(new_pw) and check3(new_pw):
            return new_pw
        pw = new_pw

# part 1
password1 = next_valid(INPUT)
print(f'Part 1: {password1}') # hepxxyzz


# part 2
print(f'Part 2: {next_valid(password1)}') # heqaabcc
