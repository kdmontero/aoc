with open('day06.txt') as given:
	data_map = {}
	for line in given.read().split('\n'):
		data_map[line[4:]] = line[:3]

# part 1
orbital = {}
exorbit = []
for planet, orbit in data_map.items():
	orbital[planet] = [orbit]
	exorbit.append(orbit)
	if orbit in orbital.keys():
		orbital[planet] += orbital[orbit]
	if planet in exorbit:
		for x, y in orbital.items():
			if planet in y:
				orbital[x] += orbital[planet]
				
total = 0
for orbits in orbital.values():
	total += len(orbits)
	
print(f'Part 1: {total}') # 151345


# part 2
common = []
for x in orbital["YOU"]:
	for y in orbital["SAN"]:
		if x == y:
			common.append(x)
			break

def transfer(a,b):
	steps = 0
	while a != b:
		a = data_map[a]
		steps += 1
	return steps

min_you = min_san = len(data_map)
for orbit in common:
	steps_you = transfer("YOU", orbit)
	steps_san = transfer("SAN", orbit)
	if steps_you < min_you:
		min_you = steps_you
	if steps_san < min_san:
		min_san = steps_san
	
print(f'Part 2: {min_you + min_san - 2}') # 391