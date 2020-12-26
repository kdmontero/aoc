with open('day01.txt') as f:
    digits = [int(n) for n in f.readline()]

# part 1
captcha1 = 0
for i in range(len(digits)):
    if i == len(digits)-1:
        j = 0
    else:
        j = i + 1
    if digits[i] == digits[j]:
        captcha1 += digits[i]

print(f'Part 1: {captcha1}') # 1034


# part 2
captcha2 = 0
half = len(digits)//2
for i in range(half):
    if digits[i] == digits[i + half]:
        captcha2 += 2 * digits[i]

print(f'Part 2: {captcha2}') # 1356