from collections import deque
from copy import deepcopy

print('Advent of Code 2020 - Day 23')
given = '538914762'

# part 1
def remove_cups(main_cups):
    return [main_cups[0]] + main_cups[4:]

def get_destination(main_cups, current): # index of destination
    destination = current - 1
    max_cup = max(main_cups)
    while True:
        if destination in cups:
            break
        else:
            destination -= 1
        
        if destination <= 0:
            destination = max_cup
    return main_cups.index(destination)

def insert_cups(main_cups, cups):
    for i in range(3):
        main_cups.insert(i + 1, cups[i])
    return main_cups

def rotate(main_cups, index):
    main_cups = deque(main_cups)
    main_cups.rotate(-index)
    return list(main_cups)

cups = [int(num) for num in list(given)]
for _ in range(100):
    current_cup = cups[0]
    three_cups = deepcopy(cups[1:4])
    cups = remove_cups(cups)
    destination = get_destination(cups, current_cup)
    cups = rotate(cups, destination)
    cups = insert_cups(cups, three_cups)
    cups = rotate(cups, cups.index(current_cup)+1)

index_1 = cups.index(1)
cups = deque([str(num) for num in cups])
cups.rotate(-index_1)
cups.popleft()
ans = ''.join(cups)
print(f'Part 1: {ans}') # 54327968
