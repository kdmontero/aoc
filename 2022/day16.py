import re
from itertools import permutations

if __name__ == '__main__':
    print('Advent of Code 2022 - Day 16')

    with open('day16.txt') as f:
        tunnels = {}
        flow = {}

        for line in f.read().splitlines():
            flow_rate = int(re.findall('-?\d+', line)[0])
            valve, *tunnel = re.findall(r'\b[A-Z]{2}\b', line)
            tunnels[valve] = tunnel
            if (flow_rate != 0) or (valve == 'AA'):
                flow[valve] = flow_rate

    def get_min_dist(start: str, end: str) -> int:

        visited = set()
        queue = [start]
        step = 0
        while end not in visited:
            temp_queue = []
            step += 1
            for current in queue:
                for node in tunnels[current]:
                    if node in visited or node in queue:
                        continue
                    if node == end:
                        return step
                    temp_queue.append(node)
                else:
                    visited.add(current)
            queue = temp_queue

    paths = {}
    path_list = []
    for start in flow:
        paths[start] = {}
        path_list.append(start)
        for end in flow:
            if start == end:
                continue
            distance = get_min_dist(start, end)
            paths[start][end] = distance

    
    print(path_list)
    # part 1

    queue = [(0, {'AA'}, 'AA', 30)] # pressure, visited, node, time remaining
    max_pressure1 = 0

    while queue:
        temp_queue = []
        for current in queue:
            cur_pressure, visited, cur_node, cur_time = current
            for n_node in paths[cur_node]:
                if n_node in visited:
                    continue
                n_time = cur_time - (paths[cur_node][n_node] + 1)
                if n_time < 0:
                    continue

                n_pressure = cur_pressure + (flow[n_node] * n_time)
                max_pressure1 = max(max_pressure1, n_pressure)
                n_visited = visited | {cur_node}
                temp_queue.append((n_pressure, n_visited, n_node, n_time))
        queue = temp_queue

    print(f'Part 1: {max_pressure1}') # 2124


    # part 2

    queue = [(0, {'AA'}, 'AA', 26, 'AA', 26,)] 
    # pressure, visited, node, time, e_node, e_time

    max_pressure2 = 0

    while queue:
        temp_queue = []
        for current in queue:
            pressure, visited, cur_node, cur_time, e_node, e_time = current

            not_visited = paths.keys() - visited

            for n_node, n_e_node in permutations(not_visited, 2):
                n_time = max(0, cur_time - (paths[cur_node][n_node] + 1))
                n_e_time = max(0, e_time - (paths[e_node][n_e_node] + 1))

                if n_time == n_e_time == 0:
                    continue

                ideal_time = max(n_time, n_e_time)
                ideal_pressure = pressure
                for not_visited_node in not_visited:
                    ideal_pressure += ideal_time * flow[not_visited_node]
                if ideal_pressure < max_pressure2:
                    continue

                n_pressure = pressure \
                + (flow[n_node] * n_time) \
                + (flow[n_e_node] * n_e_time)

                max_pressure2 = max(max_pressure2, n_pressure)
                n_visited = visited | {cur_node, e_node, n_node, n_e_node}
                temp_queue.append((
                    n_pressure, n_visited, n_node, 
                    n_time, n_e_node, n_e_time
                ))

        queue = temp_queue

    print(f'Part 2: {max_pressure2}') # 2775
