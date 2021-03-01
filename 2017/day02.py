print('Advent of Code 2017 - Day 02')
with open('day02.txt') as f:
    spreadsheet = [[int(num) for num in line.split()] 
    for line in f.read().splitlines()]

checksum = 0
sum_ = 0
for line in spreadsheet:
    checksum += max(line) - min(line)
    for i, num1 in enumerate(line):
        for num2 in line[i+1:]:
            if not (num1 % num2 and num2 % num1):
                sum_ += max(num1, num2) // min(num1, num2)
                break
        else:
            continue
        break

print(f'Part 1: {checksum}') # 45972
print(f'Part 2: {sum_}') # 326
