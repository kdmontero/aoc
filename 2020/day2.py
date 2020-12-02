from collections import Counter

def parse(text):
    lmin = text.split('-')[0]
    lmax = text.split('-')[1].split()[0]
    letter = text.split('-')[1].split()[1].rstrip(':')
    pw = text.split('-')[1].split()[2]
    return (lmin, lmax, letter, pw)

passwords = []
with open('day2.txt') as given:
    for line in given.readlines():
        passwords.append(parse(line.rstrip('\n')))

# part 1
valid = 0
for password in passwords:
    lmin, lmax, letter, pw = password
    c = Counter(pw)
    if int(lmin) <= c[letter] <= int(lmax):
        valid += 1

print(valid)


# part 2
valid = 0
for password in passwords:
    lmin, lmax, letter, pw = password
    c = Counter(pw)
    if (pw[int(lmin)-1] == letter and pw[int(lmax)-1] != letter) or (pw[int(lmin)-1] != letter and pw[int(lmax)-1] == letter):
        valid += 1

print(valid)