with open('day01.txt') as given:
    masses = [int(line) for line in given.read().split('\n')]

# part 1
total = 0
for mass in masses:
    total += (mass//3) - 2

print(total) # 3330521


# part 2
total = 0
for mass in masses:
    intcode_mass = 0
    while True:
        fuel = (mass//3) - 2
        if fuel <= 0:
            break
        intcode_mass += fuel
        mass = fuel
    total += intcode_mass

print(total) # 4992931