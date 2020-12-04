from copy import deepcopy

with open('day02.txt') as given:
	intcode = [int(num) for num in given.read().split(',')]

def run(intcode, a, b):
	i = 0
	intcode[1] = a
	intcode[2] = b
	while i < len(intcode)+1:
		if intcode[i] == 1:
			intcode[intcode[i+3]] = intcode[intcode[i+1]] + intcode[intcode[i+2]]
		elif intcode[i] == 2:
			intcode[intcode[i+3]] = intcode[intcode[i+1]] * intcode[intcode[i+2]]
		elif intcode[i] == 99:
			break
		else:
			break
		i += 4
	return intcode[0]

# part 1
intcode1 = intcode[:]
print(run(intcode1, 12, 2)) # 7594646


# part 2
for noun in range(100):
	for verb in range(100):
		intcode2 = intcode[:]
		if run(intcode2, noun, verb) == 19690720:
			print(100 * noun + verb) # 3376
			break
	else:
		continue
	break