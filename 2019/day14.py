from collections import deque, Counter

with open('day14.txt') as f:
    recipe = {}
    qty = {}
    fuel = {}
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
            fuel_dq = deque()
            for ingr in elements.split(', '):
                num, elem = ingr.split()
                fuel[elem] = int(num)
                fuel_dq.append(elem)

excess = Counter()

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

print(f'Part 1: {fuel["ORE"]}') # 278404