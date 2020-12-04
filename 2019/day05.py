with open('day05.txt') as given:
	program = [int(num) for num in given.read().split(',')]

def opcode(num):
	return int(str(num)[-2:])
	
def mode1(num):
	if len(str(num))>=3:
		return int(str(num)[-3])
	else:
		return 0

def mode2(num):
	if len(str(num))>=4:
		return int(str(num)[-4])
	else:
		return 0
		
def mode3(num):
	if len(str(num))>=5:
		return int(str(num)[-5])
	else:
		return 0

def run(program, input_num):
	i=0
	while i < len(program)+1:
		if opcode(program[i]) == 1:
			if mode1(program[i]) == 1:
				parameter1 = program[i+1]
			elif mode1(program[i]) == 0:
				parameter1 = program[program[i+1]]
			if mode2(program[i]) == 1:
				parameter2 = program[i+2]
			elif mode2(program[i]) == 0:
				parameter2 = program[program[i+2]]
			program[program[i+3]] = parameter1 + parameter2
			i += 4
		elif opcode(program[i]) == 2:
			if mode1(program[i]) == 1:
				parameter1 = program[i+1]
			elif mode1(program[i]) == 0:
				parameter1 = program[program[i+1]]
			if mode2(program[i]) == 1:
				parameter2 = program[i+2]
			elif mode2(program[i]) == 0:
				parameter2 = program[program[i+2]]
			program[program[i+3]] = parameter1 * parameter2
			i += 4
		elif opcode(program[i]) == 3:
			program[program[i+1]] = input_num
			i += 2
		elif opcode(program[i]) == 4:
			output = program[program[i+1]]
			# print(output) # shows all the output
			i += 2
		elif opcode(program[i]) == 5:
			if mode1(program[i]) == 1:
				parameter1 = program[i+1]
			elif mode1(program[i]) == 0:
				parameter1 = program[program[i+1]]
			if mode2(program[i]) == 1:
				parameter2 = program[i+2]
			elif mode2(program[i]) == 0:
				parameter2 = program[program[i+2]]
			if parameter1 != 0:
				i = parameter2
			else:
				i += 3
		elif opcode(program[i]) == 6:
			if mode1(program[i]) == 1:
				parameter1 = program[i+1]
			elif mode1(program[i]) == 0:
				parameter1 = program[program[i+1]]
			if mode2(program[i]) == 1:
				parameter2 = program[i+2]
			elif mode2(program[i]) == 0:
				parameter2 = program[program[i+2]]
			if parameter1 == 0:
				i = parameter2
			else:
				i += 3
		elif opcode(program[i]) == 7:
			if mode1(program[i]) == 1:
				parameter1 = program[i+1]
			elif mode1(program[i]) == 0:
				parameter1 = program[program[i+1]]
			if mode2(program[i]) == 1:
				parameter2 = program[i+2]
			elif mode2(program[i]) == 0:
				parameter2 = program[program[i+2]]
			if parameter1 < parameter2:
				program[program[i+3]] = 1
			else:
				program[program[i+3]] = 0
			i += 4
		elif opcode(program[i]) == 8:
			if mode1(program[i]) == 1:
				parameter1 = program[i+1]
			elif mode1(program[i]) == 0:
				parameter1 = program[program[i+1]]
			if mode2(program[i]) == 1:
				parameter2 = program[i+2]
			elif mode2(program[i]) == 0:
				parameter2 = program[program[i+2]]
			if parameter1 == parameter2:
				program[program[i+3]] = 1
			else:
				program[program[i+3]] = 0
			i += 4
		elif opcode(program[i]) == 99:
			return output
		else:
			break

# part 1
program1 = program[:]
print(run(program1, 1)) # 7692125

# part 2
program2 = program[:]
print(run(program2, 5)) # 14340395