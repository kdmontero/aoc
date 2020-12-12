with open('day09.txt') as f:
    xmas = [int(i) for i in f.read().split('\n')]

def is_valid(num, array):
    for i in range(len(array)-1):
        for j in range(i+1, len(array)):
            if array[i] + array[j] == num:
                return True
    return False

# part 1
for i in range(25, len(xmas)):
    if not is_valid(xmas[i], xmas[i-25:i]):
        invalid_num = xmas[i]
        break
    
print(f'Part 1: {invalid_num}') # 248131121


# part 2
for low in range(i):
    high = low + 1
    while sum(xmas[low:high+1]) < invalid_num:
        high += 1
    
    if sum(xmas[low:high+1]) == invalid_num:
        weakness = min(xmas[low:high+1]) + max(xmas[low:high+1])
        break

print(f'Part 2: {weakness}') # 31580383