import itertools as it
import heapq as hq
import copy as cp

print("Advent of Code 2016 - Day 11: Radioisotope Thermoelectric Generators")
with open('day11.txt') as f:
    init_bldg = [None] * 4 
    elements = []
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
            init_bldg[level] = ()
            continue
        
        *_, objects = line.split(' ', 5)
        objects = (obj.replace(' ', '-') for obj in 
                objects.replace(',', '').replace(' and', '').split(' a '))
        
        final_obj = []
        for obj in objects:
            element = obj.split('-')[0]
            if element not in elements:
                elements.append(element)
            value = elements.index(element) + 1
            if 'generator' in obj:
                final_obj.append(value)
            elif 'microchip' in obj:
                final_obj.append(-value)
        
        init_bldg[level] = tuple(sorted(final_obj))

    init_bldg = tuple(init_bldg)
    # objects in the floor of init_bldg is represented by integers. Microchips
    # are negative and Generators are positive. The pair has equal absolute
    # values. The floor levels are arranged in ascending order


class Building:
    no_of_objects = 0
    starting_score = 0

    def __init__(self, bldg, elevator, steps):
        self.bldg = bldg # tuple of tuples (floors)
        self.elevator = elevator # index of the elevator index
        self.steps = steps
        self.score = Building.get_score(bldg)
        self.g_cost = Building.starting_score - self.score
        # g_cost is distance (heuristic) of the bldg to the starting bldg
        self.h_cost = (Building.no_of_objects * 4) - self.score
        # h_cost is distance (heuristic) of the bldg to the target bldg
        self.f_cost = self.g_cost + self.h_cost

    def get_score(bldg):
        '''Returns the building score (heuristic value)'''
        bldg_score = 0
        for level, floor in enumerate(bldg):
            bldg_score += (level + 1) * len(floor)
        return bldg_score

    def set_starting_score(init_bldg):
        Building.starting_score = Building.get_score(init_bldg)

    def set_no_of_objects(init_bldg):
        Building.no_of_objects = sum(len(floor) for floor in init_bldg)

    def __lt__(self, other):
        if self.f_cost < other.f_cost:
            return True
        elif self.f_cost > other.f_cost:
            return False
        else:
            if self.steps < other.steps:
                return True
            else:
                return False


def check_floor(objects):
    '''Returns True if the floor setup is valid, otherwise False'''

    microchips = set()
    generators = set()
    for obj in objects:
        if obj < 0:
            microchips.add(abs(obj))
        elif obj > 0:
            generators.add(abs(obj))

    if not generators:
        return True

    if microchips - generators:
        return False
    else:
        return True


def a_star(init_bldg):
    '''A-star algorithm to get the shortest path'''

    queue = [Building(init_bldg, 0, 0)]
    seen = set()

    while True:
        cur_bldg = hq.heappop(queue)
        bldg = cur_bldg.bldg
        level = cur_bldg.elevator
        steps = cur_bldg.steps

        if cur_bldg.score == Building.no_of_objects * 4:
            break
        
        if (bldg, level) not in seen:
            seen.add((bldg, level))
        else:
            continue

        # get all the possible combinations of objects to bring
        objects_to_bring = set(it.combinations(bldg[level], 2)) | set(
            it.combinations(bldg[level], 1))

        for move in [+1, -1]: # movement of the elevator 
            if level + move < 0 or level + move > 3:
                continue

            for objects in objects_to_bring:
                # remove the objects in the current floor
                temp_bldg = list(cp.deepcopy(bldg))
                temp_bldg[level] = set(temp_bldg[level]) - set(objects)
                temp_bldg[level] = tuple(sorted(temp_bldg[level]))

                # add the objects in the next floor
                temp_bldg[level + move] = set(
                    temp_bldg[level + move]) | set(objects)
                temp_bldg[level + move] = tuple(
                    sorted(temp_bldg[level + move]))
                temp_bldg = tuple(temp_bldg)

                # Add the Building instance to the queue if both the current
                # and next floor are valid
                if check_floor(temp_bldg[level]) and check_floor(
                    temp_bldg[level + move]):
                        valid_bldg = Building(temp_bldg, level+move, steps+1)
                        hq.heappush(queue, valid_bldg)

    return steps

# part 1
Building.set_starting_score(init_bldg)
Building.set_no_of_objects(init_bldg)
print(f'Part 1: {a_star(init_bldg)}') # 31

            
# part 2
# VERY SLOW AND UNOPTIMIZED SOLUTION, 30 MINS RUNTIME
new_items = [ 
    len(elements) + 1,
    len(elements) + 2,
    -(len(elements) + 1),
    -(len(elements) + 2)
] # add the 4 objects by adding 2 positive and negative values to the init_bldg

new_first_flr = tuple(sorted(list(init_bldg[0]) + new_items))
init_bldg = list(init_bldg)
init_bldg[0] = new_first_flr
init_bldg2 = tuple(init_bldg)

Building.set_starting_score(init_bldg2)
Building.set_no_of_objects(init_bldg2)
print(f'Part 2: {a_star(init_bldg2)}') # 55
