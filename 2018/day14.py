if __name__ == '__main__':
    print("Advent of Code 2018 - Day 14: Chocolate Charts")

    with open('day14.txt') as f:
        given = int(f.read().strip())


    # part 1

    target_len = given + 10
    recipes = '37'
    elf1, elf2 = 0, 1
    while len(recipes) < target_len:
        elf1_recipe = int(recipes[elf1])
        elf2_recipe = int(recipes[elf2])
        new_recipe = str(elf1_recipe + elf2_recipe)
        recipes += new_recipe
        elf1 = (elf1 + 1 + elf1_recipe) % len(recipes)
        elf2 = (elf2 + 1 + elf2_recipe) % len(recipes)
        if len(recipes) == target_len:
            score = ''.join(recipes[-10:])

    print(f'Part 1: {score}') # 1031816654


    # part 2

    print(f'Part 2: {0}') #

