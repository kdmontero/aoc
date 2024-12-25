print("Advent of Code 2017 - Day 11: Hex Ed")

with open('day11.txt') as f:
    path = f.read().split(',')

def no_of_steps(x, y):
    y_prime = abs(y * 2)
    x_prime = abs(x)

    if x_prime >= y_prime:
        return int(x_prime)
    else:
        return int(x_prime + ((y_prime - x_prime) / 2))

x = y = 0
furthest_step = 0

for step in path:
    if step == 'n':
        y += 1
    elif step == 'ne':
        y += 0.5
        x += 1
    elif step == 'se':
        y -= 0.5
        x += 1
    elif step == 's':
        y -= 1
    elif step == 'sw':
        y -= 0.5
        x -= 1
    elif step == 'nw':
        y += 0.5
        x -= 1
    
    furthest_step = max(furthest_step, no_of_steps(x, y))

print(f'Part 1: {no_of_steps(x, y)}') # 747
print(f'Part 2: {furthest_step}') # 1544
