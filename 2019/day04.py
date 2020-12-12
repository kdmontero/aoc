from collections import Counter

given = '372304-847060'

min_, max_ = tuple(given.split('-'))

def adj_check(password):
	for i in range(len(password)-1):
		if password[i] == password[i+1]:
			return True
	else:
		return False

def inc_check(password):
	for i in range(len(password)-1):
		if password[i] > password[i+1]:
			return False
	else:
		return True

def adj_check2(password):
	counter = Counter(password)
	if 2 in counter.values():
		return True
	return False

count1 = 0
count2 = 0
for pw in range(int(min_), int(max_)+1):
	if adj_check(str(pw)) and inc_check(str(pw)):
		count1 += 1
	if adj_check2(str(pw)) and inc_check(str(pw)):
		count2 += 1

print(f'Part 1: {count1}') # 475
print(f'Part 2: {count2}') # 297