from copy import deepcopy
from collections import OrderedDict

print('Advent of Code 2020 - Day 21')
with open('day21.txt') as f:
    foods = []
    ingredients = set()
    allergens = set()
    for line in f.read().splitlines():
        i, a = line.rstrip(')').split(' (contains ')
        ingredients.update(i.split(' '))
        allergens.update(a.split(', '))
        foods.append([i.split(' '),a.split(', ')])


# part 1
with_a = set()
match_a = {}
for a in allergens:
    ingredients_with_a = deepcopy(ingredients)
    for i_list, a_list in foods:
        if a in a_list:
            ingredients_with_a = ingredients_with_a.intersection(i_list)
    with_a = with_a.union(ingredients_with_a)
    match_a[a] = ingredients_with_a

no_a = ingredients.difference(with_a)

count = 0
for food in foods:
    for i in food[0]:
        if i in no_a:
            count += 1

print(f'Part 1: {count}') # 2061


# part 2
cdil_list = [] # canonical dangerous ingredient list
matched = set()
while len(cdil_list) != len(match_a):
    for a in list(allergens):
        match_a[a] = match_a[a].difference(matched)
        if len(match_a[a]) == 1:
            matched = matched.union(match_a[a])
            cdil_list.append([a, list(match_a[a])[0]])

cdil = ''
for allergen, ingredient in sorted(cdil_list):
    cdil += ingredient + ','

print(f'Part 2: {cdil.strip(",")}') # cdqvp,dglm,zhqjs,rbpg,xvtrfz,tgmzqjz,mfqgx,rffqhl
