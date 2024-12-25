from collections import Counter

print("Advent of Code 2018 - Day 02: Inventory Management System")
with open('day02.txt') as f:
    ids = f.read().splitlines()

# part 1
ids_2 = ids_3 = 0
for id_ in ids:
    c = Counter(id_)
    if 2 in c.values():
        ids_2 += 1
    if 3 in c.values():
        ids_3 += 1

print(f'Part 1: {ids_2 * ids_3}') # 8296


# part 2
for j, id1 in enumerate(ids):
    for id2 in ids[j+1:]:
        found = False
        common = ''
        for i, letters in enumerate(zip(id1, id2)):
            if letters[0] == letters[1]:
                common += letters[0]
            elif letters[0] != letters[1] and not found:
                found = True
            elif letters[0] != letters[1] and found:
                break
        else:
            break
    else:
        continue
    break

print(f'Part 2: {common}') # pazvmqbftrbeosiecxlghkwud
