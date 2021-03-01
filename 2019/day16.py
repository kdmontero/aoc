import itertools

print('Advent of Code 2019 - Day 16')
with open('day16.txt') as f:
    given = f.read()
    nums = [int(num) for num in given]
    offset = int(given[:7])

PATTERN = [0, 1, 0, -1]

# part 1
def FFT(nums):
    l = len(nums)
    output_ = []
    for i, num in enumerate(nums):
        num_pattern = []
        cycle = itertools.cycle(PATTERN)
        for multiplier in cycle:
            num_pattern += [multiplier] * (i + 1)
            if len(num_pattern) > l+1:
                break
        num_pattern = num_pattern[1:l+2]
        digit = 0
        for num, multiplier in zip(nums, num_pattern):
            digit += num * multiplier
        output_.append(abs(digit) % 10)
    return output_

nums1 = nums[:]
for _ in range(100):
    ans1 = FFT(nums1)
    nums1 = ans1

ans1 = [str(num) for num in ans1[:8]]
print(f'Part 1: {"".join(ans1)}') # 52611030


# part 2
def FFT2(nums): # optimized solution (not for general case)
    output_ = [nums[-1]]
    for num in nums[-2::-1]:
        output_.append((num + output_[-1]) % 10)
    return list(reversed(output_))

nums2 = nums[:] * 10_000
num_length = len(nums2)
nums2 = nums2[num_length//2:]
for _ in range(100):
    ans2 = FFT2(nums2)
    nums2 = ans2

offset -= num_length//2
ans2 = [str(num) for num in ans2[offset:offset+8]]
print(f'Part 2: {"".join(ans2)}') # 52541026
