if __name__ == '__main__':
    print("Advent of Code 2022 - Day 08: Treetop Tree House")

    with open('day08.txt') as f:
        MAP_HEIGHT = 0
        MAP_WIDTH = 0
        tree_map = {}

        for y, line in enumerate(f.read().splitlines()):
            MAP_HEIGHT = max(MAP_HEIGHT, y)
            for x, height in enumerate(line):
                tree_map[(y, x)] = int(height)
                MAP_WIDTH = max(MAP_WIDTH, x)


    # part 1

    visible_trees = set()

    # view from left
    for y in range(MAP_HEIGHT + 1):
        seen_tree = -1
        for x in range(MAP_WIDTH + 1):
            current_tree = tree_map[(y, x)]
            if current_tree > seen_tree:
                seen_tree = current_tree
                visible_trees.add((y, x))
                if seen_tree == 9:
                    break

    # view from right
    for y in range(MAP_HEIGHT + 1):
        seen_tree = -1
        for x in range(MAP_WIDTH, -1, -1):
            current_tree = tree_map[(y, x)]
            if current_tree > seen_tree:
                seen_tree = current_tree
                visible_trees.add((y, x))
                if seen_tree == 9:
                    break

    # view from top
    for x in range(MAP_WIDTH + 1):
        seen_tree = -1
        for y in range(MAP_HEIGHT + 1):
            current_tree = tree_map[(y, x)]
            if current_tree > seen_tree:
                seen_tree = current_tree
                visible_trees.add((y, x))
                if seen_tree == 9:
                    break

    # view from bottom
    for x in range(MAP_WIDTH + 1):
        seen_tree = -1
        for y in range(MAP_HEIGHT, -1, -1):
            current_tree = tree_map[(y, x)]
            if current_tree > seen_tree:
                seen_tree = current_tree
                visible_trees.add((y, x))
                if seen_tree == 9:
                    break


    print(f'Part 1: {len(visible_trees)}') # 1546


    # part 2

    def find_scenic_score(y, x):
        tree_height = tree_map[(y, x)]

        # look up
        up = 0
        for dy in range(y - 1, -1, -1):
            up += 1
            if tree_map[(dy, x)] >= tree_height:
                break

        # look down
        down = 0
        for dy in range(y + 1, MAP_HEIGHT + 1):
            down += 1
            if tree_map[(dy, x)] >= tree_height:
                break

        # look left
        left = 0
        for dx in range(x - 1, -1, -1):
            left += 1
            if tree_map[(y, dx)] >= tree_height:
                break

        # look right
        right = 0
        for dx in range(x + 1, MAP_WIDTH + 1):
            right += 1
            if tree_map[(y, dx)] >= tree_height:
                break

        return right * left * down * up

    highest_score = 0

    for y in range(MAP_HEIGHT + 1):
        for x in range(MAP_WIDTH + 1):
            highest_score = max(highest_score, find_scenic_score(y, x))

    print(f'Part 2: {highest_score}') # 519064
