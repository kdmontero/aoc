print("Advent of Code 2019 - Day 03: Crossed Wires")
with open('day03.txt') as given:
    wires = given.read().split('\n')

wire1 = wires[0].split(',')
wire2 = wires[1].split(',')

def move(direction, position):
	if direction == "R":
		return (position[0]+1, position[1])
	if direction == "L":
		return (position[0]-1, position[1])
	if direction == "U":
		return (position[0], position[1]+1)
	if direction == "D":
		return (position[0], position[1]-1)

path1 = {(0, 0): 0}
crossed = {}

length1 = 0
current = (0,0)
for line in wire1:
	direction = line[0]
	step = int(line[1:])
	for i in range(1, step+1):
		current = move(direction, current)
		length1 += 1
		if current not in path1:
			path1[current] = length1

length2 = 0
current = (0,0)
for line in wire2:
	direction = line[0]
	step = int(line[1:])
	for i in range(1, step+1):
		current = move(direction, current)
		length2 += 1
		if current in path1:
			crossed[current] = path1[current] + length2

# part 1
print(f'Part 1: {min(abs(x) + abs(y) for x, y in crossed)}') # 308

# part 2
print(f'Part 2: {min(crossed.values())}') # 12934
