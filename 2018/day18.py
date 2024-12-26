from copy import deepcopy


if __name__ == '__main__':
    print("Advent of Code 2018 - Day 18: Settlers of The North Pole")

    with open('day18.txt') as f:
        orig_ground = set()
        orig_trees = set()
        orig_lumber = set()
        for y, line in enumerate(f.read().strip().splitlines()):
            for x, char in enumerate(line):
                if char == '.':
                    orig_ground.add((y, x))
                elif char == '|':
                    orig_trees.add((y, x))
                elif char == '#':
                    orig_lumber.add((y, x))

        height, width = y, x

    def get_8n(coords: tuple[int, int]) -> list[tuple[int, int]]:
        y, x = coords
        neighbors = []
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if dy == 0 and dx == 0:
                    continue

                if 0 <= y + dy <= height and 0 <= x + dx <= width:
                    neighbors.append((y + dy, x + dx))

        return neighbors

    def get_next_state(
        ground: set[tuple[int, int]],
        trees: set[tuple[int, int]],
        lumber: set[tuple[int, int]]
    ) -> int:

        new_ground = set()
        new_trees = set()
        new_lumber = set()

        for y in range(height + 1):
            for x in range(width + 1):
                acre = (y, x)
                if acre in ground:
                    trees_count = 0
                    for n_coords in get_8n(acre):
                        if n_coords in trees:
                            trees_count += 1
                    if trees_count >= 3:
                        new_trees.add(acre)
                    else:
                        new_ground.add(acre)
                
                elif acre in trees:

                    lumber_count = 0
                    for n_coords in get_8n(acre):
                        if n_coords in lumber:
                            lumber_count += 1
                    if lumber_count >= 3:
                        new_lumber.add(acre)
                    else:
                        new_trees.add(acre)
                
                elif acre in lumber:
                    lumber_count = 0
                    trees_count = 0
                    for n_coords in get_8n(acre):
                        if n_coords in lumber:
                            lumber_count += 1
                        elif n_coords in trees:
                            trees_count += 1
                    if lumber_count >= 1 and trees_count >= 1:
                        new_lumber.add(acre)
                    else:
                        new_ground.add(acre)

        return (new_ground, new_trees, new_lumber)


    # part 1

    ground = deepcopy(orig_ground)
    trees = deepcopy(orig_trees)
    lumber = deepcopy(orig_lumber)

    for _ in range(10):
        ground, trees, lumber = get_next_state(ground, trees, lumber)

    print(f'Part 1: {len(trees) * len(lumber)}') # 506160


    # part 2

    ground = deepcopy(orig_ground)
    trees = deepcopy(orig_trees)
    lumber = deepcopy(orig_lumber)

    seen = {}
    acre_history = {}
    iteration = 0
    state = (frozenset(ground), frozenset(trees), frozenset(lumber))

    while state not in seen:
        seen[state] = iteration
        acre_history[iteration] = (len(trees), len(lumber))
        ground, trees, lumber = get_next_state(ground, trees, lumber)
        iteration += 1
        state = (frozenset(ground), frozenset(trees), frozenset(lumber))

    cycle_start = seen[state]
    cycle_len = iteration - cycle_start
    target_state = ((1_000_000_000 - cycle_start) % cycle_len) + cycle_start
    trees_count, lumber_count = acre_history[target_state]

    print(f'Part 2: {trees_count * lumber_count}') # 189168

