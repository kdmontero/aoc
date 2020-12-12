def parse(text):
    lmin = text.split('-')[0]
    lmax = text.split('-')[1].split()[0]
    letter = text.split('-')[1].split()[1].rstrip(':')
    pw = text.split('-')[1].split()[2]
    return (lmin, lmax, letter, pw)

with open('day02.txt') as given:
    passwords = [parse(line) for line in given.read().split('\n')]

valid1 = 0
valid2 = 0
for password in passwords:
    lmin, lmax, letter, pw = password
    if int(lmin) <= pw.count(letter) <= int(lmax):
        valid1 += 1
    if bool(pw[int(lmin)-1] == letter) != bool(pw[int(lmax)-1] == letter): # XOR: bool(x) != bool(y)
        valid2 += 1

print(f'Part 1: {valid1}') # 445
print(f'Part 2: {valid2}') # 491