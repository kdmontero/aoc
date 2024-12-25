import heapq as hq
import time

print("Advent of Code 2016 - Day 22: Grid Computing")
class FileSystem:
    def __init__(self, x, y, used, avail):
        self.x = x
        self.y = y
        self.used = used
        self.avail = avail

    @staticmethod
    def arrange_descending_avail(filesystems):
        return sorted(filesystems, key=lambda x: x.avail, reverse=True)

    @staticmethod
    def arrange_ascending_used(filesystems):
        return sorted(filesystems, key=lambda x: x.used)

with open('day22.txt') as f:
    df = []
    grid = {}
    max_x = max_y = 0
    for line in [filesystem for filesystem in f.read().splitlines() 
        if filesystem.startswith('/dev/grid/node')]:
            _, x, y, _, used, avail, _ = line.replace('-', ' ').split()
            x, y = int(x.lstrip('x')), int(y.lstrip('y'))
            used, avail = int(used.rstrip('T')), int(avail.rstrip('T'))
            df.append(FileSystem(x, y, used, avail))
            grid[(y, x)] = [used, avail]
            max_x = max(max_x, x)
            max_y = max(max_y, y)


# part 1
descending_avail = FileSystem.arrange_descending_avail(df)
ascending_used = FileSystem.arrange_ascending_used(df) 
viable_pairs = 0

for source in ascending_used:
    if source.used == 0:
        continue

    for destination in descending_avail:
        if source == destination:
            continue
        
        if source.used <= destination.avail:
            viable_pairs += 1
        else:
            break

print(f'Part 1: {viable_pairs}') # 872


# part 2
def adjacent(y, x, grid):
    n = []
    for dt in [-1, 1]:
        if (y, x+dt) in grid:
            n.append((y, x+dt))

        if (y+dt, x) in grid:
            n.append((y+dt, x))
    return n

def check_adjacent(y, x, grid):
    valid_destinations = 0
    used = grid[(y, x)][0]
    for node in get_n(y, x, grid):
        if used <= node[1]:
            valid_destinations += 1
    
    return valid_destinations

def get_state(y, x, grid):
    EMPTY = '_'
    LARGE = '#'
    GOAL = 'G'
    ACCESS = '!'

    if grid[(y, x)][0] == 0:
        return EMPTY
    
    if x == max_x and y == 0:
        return GOAL

    if x == y == 0:
        return ACCESS

    for node in adjacent(y, x, grid):
        if grid[(y,x)][0] > grid[node][1] + grid[node][0]:
            return LARGE

    return '.'

array = [['.']*(max_x+1) for _ in range(max_y+1)]

for i in range(max_y+1):
    for j in range(max_x+1):
        if grid.get((i, j)):
            array[i][j] = get_state(i, j, grid)

'''
def print_array(array):
    for line in array:
        print(''.join(line))
'''

def a_star(array, start, end):
    # elements on queue: (f_cost: g_cost + h_cost, h_cost: distance from end,
    # node, steps, g_cost: distance from start)
    start_to_end = abs(start[0] - end[0]) + abs(start[1] - end[1])
    queue = [(start_to_end, start_to_end, start, 0, 0)]
    queue_pos = set()
    
    seen = set()

    while True:
        cur_node = hq.heappop(queue)
        f_cost, h_cost, position, steps, g_cost = cur_node
        y, x = position

        if position == end:
            break

        if cur_node not in seen:
            seen.add((y, x))
        else:
            continue

        for n in adjacent(y, x, grid):
            dy, dx = n
            if array[dy][dx] != '#' and (dy, dx) not in seen and (dy, dx) not in queue_pos:
                g_cost = abs(start[0] - n[0]) + abs(start[1] - n[1])
                h_cost = abs(end[0] - n[0]) + abs(end[1] - n[1])
                f_cost = g_cost + h_cost
                hq.heappush(queue, (f_cost, g_cost, n, steps+1, h_cost))
                queue_pos.add((dy, dx))
                
    return steps

steps = a_star(array, (22, 24), (0, 31)) + (5*30)
print(f'Part 2: {steps}') # 211
