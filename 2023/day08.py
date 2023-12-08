import re
import math
from typing import Optional


if __name__ == '__main__':
    print('Advent of Code 2023 - Day 08')

    with open('day08.txt') as f:
        pattern = re.compile(r'[A-Z0-9]{3}')
        raw_ins, network = f.read().split('\n\n')
        ins = raw_ins.replace('L', '0').replace('R', '1')
        path = [int(i) for i in ins]
        map_ = {}
        for line in network.splitlines():
            node, left, right = pattern.findall(line)
            map_[node] = [left, right]
    
    def find_steps(node: str, end: Optional[str] = None) -> int:
        index = 0
        steps = 0
        if end is not None:
            target = re.compile(end)
        else:
            target = re.compile(r'[A-Z0-9]{2}Z')

        while node not in target.findall(node):
            direction = path[index]
            node = map_[node][direction]
            steps += 1
            index += 1
            if index >= len(path):
                index = 0
        return steps

    # part 1

    steps1 = find_steps('AAA', 'ZZZ')
    print(f'Part 1: {steps1}') # 20777


    # part 2 (get the LCM of each step when they first end)

    g_nodes = [node for node in map_ if node.endswith('A')]
    g_steps = []
    for node in g_nodes:
        g_steps.append(find_steps(node))
    steps2 = math.lcm(*g_steps)

    print(f'Part 2: {steps2}') # 13289612809129