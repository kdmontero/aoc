from collections import deque

with open('day08.txt') as f:
    data = [int(num) for num in f.read()]

width = 25
height = 6

# part 1
data1 = deque(data[:])
min_zeros = 1000
while data1:
    zeros, ones, twos = 0, 0, 0
    for _ in range(height):
        for _ in range(width):
            pixel = data1.popleft()
            if pixel == 0:
                zeros += 1
            elif pixel == 1:
                ones += 1
            elif pixel == 2:
                twos += 1
    if zeros < min_zeros:
        min_zeros = zeros
        check = ones * twos

print(f'Part 1: {check}') # 1572


# part 2
decode = {
    0: ' ', # black
    1: '#', # white
    2: ' '  # transparent
}

image = ''
for i in range(0, width*height):
    for pixel in range(i, len(data), width*height):
        if data[pixel] != 2:
            image += decode[data[pixel]]
            break

bios = [image[i:i+width] for i in range(0, len(image), width)]
print('Part 2:')
print(*bios, sep='\n') # KYHFE