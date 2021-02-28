print('Advent of Code 2016 - Day 03')
with open('day03.txt') as f:
    given = f.read().splitlines()
    triangles1 = [[int(side) for side in tri.strip().split()]
        for tri in given]
    triangles2 = []
    for i in range(0, len(given), 3):
        tri_group = list(zip(
            [int(side) for side in given[i].strip().split()], 
            [int(side) for side in given[i+1].strip().split()], 
            [int(side) for side in given[i+2].strip().split()], 
        ))
        triangles2 += tri_group

# part 1
possible1 = 0
for triangle in triangles1:
    a, b, c = triangle
    if a + b <= c or b + c <= a or c + a <= b:
        continue
    possible1 += 1
print(f'Part 1: {possible1}') # 1032


# part 2
possible2 = 0
for triangle in triangles2:
    a, b, c = triangle
    if a + b <= c or b + c <= a or c + a <= b:
        continue
    possible2 += 1
print(f'Part 2: {possible2}') # 1838
