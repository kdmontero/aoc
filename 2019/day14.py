from collections import deque, Counter
from copy import deepcopy

with open('day14.txt') as f:
    recipe = {}
    qty = {}
    given_fuel = {}
    for formula in f.read().splitlines():
        elements, result = formula.split(' => ')
        num, main = result.split()
        if main != 'FUEL':
            qty[main] = int(num)
            ingredients = []
            for ingr in elements.split(', '):
                num, elem = ingr.split(' ')
                ingredients.append((int(num), elem))
            recipe[main] = ingredients
        else:
            given_fuel_dq = deque()
            for ingr in elements.split(', '):
                num, elem = ingr.split()
                given_fuel[elem] = int(num)
                given_fuel_dq.append(elem)


# part 1
def ore_quantity(fuel_qty):
    excess = Counter()
    fuel_dq = deepcopy(given_fuel_dq)
    fuel = {}
    for key, value in given_fuel.items():
        fuel[key] = value * fuel_qty

    while len(fuel_dq) > 1:
        fuel_elem = fuel_dq.popleft()
        if fuel_elem == "ORE":
            fuel_dq.append(fuel_elem)
            continue
        if excess[fuel_elem] >= fuel[fuel_elem]:
            excess[fuel_elem] -= fuel[fuel_elem]
        else:
            new_qty = fuel[fuel_elem] - excess[fuel_elem]
            if new_qty % qty[fuel_elem] == 0:
                no_of_reactions = new_qty // qty[fuel_elem]
            else:
                no_of_reactions = new_qty // qty[fuel_elem] + 1
            excess[fuel_elem] = (no_of_reactions * qty[fuel_elem]) - new_qty
            for num_req, item in recipe[fuel_elem]:
                if excess[item] >= num_req * no_of_reactions:
                    excess[item] -= num_req * no_of_reactions
                else:
                    if item in fuel:
                        fuel[item] += num_req * no_of_reactions - excess[item]
                    else:
                        fuel[item] = num_req * no_of_reactions - excess[item]
                        fuel_dq.append(item)
                    excess[item] = 0
        fuel.pop(fuel_elem)

    return fuel["ORE"]

print(f'Part 1: {ore_quantity(1)}') # 278404


# part 2
TARGET = 1_000_000_000_000
low = 1
hi = TARGET
mid = (low + hi) // 2

while True:
    ores = ore_quantity(mid)
    if ores < TARGET:
        low = mid
    elif ores > TARGET:
        hi = mid
    mid = (low + hi) // 2
    if ores == ore_quantity(mid):
        break

print(f'Part 2: {mid} fuels (from {ores} ores)') # 4436981 fuels (from 999999877077 ores)