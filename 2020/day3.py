with open('day3.txt') as given:
    unit_map = given.read().split('\n')

def walk(map_, right, down):
    init_height = len(map_)
    init_width = len(map_[0])
    
    reverse_map = list(zip(*map_))
    full_map = reverse_map[:]
    right, down = down, right
    init_height, init_width = init_width, init_height
    height = init_height

    trees = 0
    y = 0
    x = 0
    while x < init_width:
        if y >= height:
            full_map += reverse_map
            height += init_height
        if full_map[y][x] == '#':
            trees += 1
        y += down
        x += right

    return trees

# part 1
print(walk(unit_map[:], 3, 1)) # 244


# part 2
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
product_trees = 1
for slope in slopes:
    product_trees *= walk(unit_map[:], *slope)

print(product_trees) # 9406609920