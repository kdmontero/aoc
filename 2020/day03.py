print("Advent of Code 2020 - Day 03: Toboggan Trajectory")
with open('day03.txt') as given:
    unit_map = given.read().split('\n')

def walk(map_, right, down):
    height = len(map_)
    width = len(map_[0])
    
    reverse_map = list(zip(*map_))
    full_map = reverse_map[:]
    right, down = down, right
    height, width = width, height
    cur_height = height

    trees = 0
    y = 0
    x = 0
    while x < width:
        if y >= cur_height:
            full_map += reverse_map
            cur_height += height
        if full_map[y][x] == '#':
            trees += 1
        y += down
        x += right

    return trees

# part 1
print(f'Part 1: {walk(unit_map[:], 3, 1)}') # 244


# part 2
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
product_trees = 1
for slope in slopes:
    product_trees *= walk(unit_map[:], *slope)

print(f'Part 2: {product_trees}') # 9406609920
