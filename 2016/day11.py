from itertools import combinations
import copy

with open('day11.txt') as f:
    bldg = [None] * 4 
    total_obj1 = 0
    for line in f.read().splitlines():
        if 'first' in line:
            level = 0
        elif 'second' in line:
            level = 1
        elif 'third' in line:
            level = 2
        elif 'fourth' in line:
            level = 3
        
        if 'nothing relevant' in line:
            bldg[level] = ()
            continue
        
        *_, objects = line.split(' ', 5)
        objects = (obj for obj in 
                objects.replace(',', '').replace(' and', '').split(' a '))
        
        final_obj = []
        for obj in objects:
            if 'generator' in obj:
                final_obj.append(obj.split(' ')[0] + '_G')
            elif 'microchip' in obj:
                final_obj.append(obj.split('-')[0] + '_M')
        
        bldg[level] = tuple(sorted(final_obj))
        total_obj1 += len(final_obj)

    bldg = tuple(bldg)

# part 1
def check_floor(objects):
    microchips = set()
    generators = set()
    for obj in objects:
        if obj.endswith('M'):
            microchips.add(obj.rstrip('_M'))
        elif obj.endswith('G'):
            generators.add(obj.rstrip('_G'))
    if not generators:
        return True

    if microchips - generators:
        return False
    else:
        return True

def empty_floors_below(level, bldg):
    for floor in range(level):
        if len(bldg[floor]) > 0:
            return False
    return True

def all_complete_pair(objects):
    if len(objects) % 2 == 1 or len(objects) < 4:
        return False
    for i in range(0, len(objects), 2):
        if objects[i][:-1] != objects[i+1][:-1]:
            return False
    return True

def find_optimal_steps(bldg, total_obj):
    queue = [[bldg, 0]]
    seen = {(bldg, 0)}
    steps = 0
    while True:
        temp = []
        while queue:
            bldg, level = queue.pop()

            if len(bldg[3]) == total_obj:
                break
                
            for move in [+1, -1]:
                if level + move < 0 or level + move > 3:
                    continue

                if all_complete_pair(bldg[level]): # optimization for pairs
                    optimal_indexes = [(0,), (0, 1), (0, 2), (1, 3)]
                    items_to_bring = set()
                    for indexes in optimal_indexes:
                        items = ()
                        for i in indexes:
                            items += (bldg[level][i],)
                        items_to_bring.add(items)
                else:
                    items_to_bring = set(combinations(bldg[level], 2)) | set(
                        combinations(bldg[level], 1))

                for items in items_to_bring:
                    temp_bldg = list(copy.deepcopy(bldg))
                    temp_bldg[level] = set(temp_bldg[level]) - set(items)
                    temp_bldg[level] = tuple(sorted(temp_bldg[level]))
                    temp_bldg[level + move] = set(
                        temp_bldg[level + move]) | set(items)
                    temp_bldg[level + move] = tuple(
                        sorted(temp_bldg[level + move]))
                    temp_bldg = tuple(temp_bldg)

                    if all((
                        check_floor(temp_bldg[level]),
                        check_floor(temp_bldg[level + move]),
                        (temp_bldg, level + move) not in seen,
                        not(empty_floors_below(level, temp_bldg) and move == -1)
                    )):
                        temp.append([temp_bldg, level + move])
                        seen.add((temp_bldg, level + move))

        else:
            queue = temp
            steps += 1
            continue
        
        return steps

print(f'Part 1: {find_optimal_steps(bldg, total_obj1)}') # 31


# part 2
new_items = ['elerium_G', 'elerium_M', 'dilithium_G', 'dilithium_M']
new_first_flr = tuple(sorted(list(bldg[0]) + new_items))
bldg = list(bldg)
bldg[0] = new_first_flr
bldg = tuple(bldg)
total_obj2 = total_obj1 + 4

print(f'Part 2: {find_optimal_steps(bldg, total_obj2)}') # 55
