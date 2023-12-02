import re

if __name__ == '__main__':
    print('Advent of Code 2023 - Day 02')

    with open('day02.txt') as f:
        game = {}
        reg_game = re.compile(r'^Game (\d+):')
        reg_red = re.compile(r'(\d+) red')
        reg_green = re.compile(r'(\d+) green')
        reg_blue = re.compile(r'(\d+) blue')
        for line in f.read().splitlines():
            _, sets = line.split(': ')
            game_id = int(reg_game.match(line)[1])
            game_sets = [] # list of lists containing [r, g, b]

            for set_ in sets.split('; '):
                game_set = []
                red = reg_red.findall(set_)
                green = reg_green.findall(set_)
                blue = reg_blue.findall(set_)

                game_set.append(int(*red))
                game_set.append(int(*green))
                game_set.append(int(*blue))

                game_sets.append(game_set)

            game[game_id] = game_sets


    # part 1
    # 12 red cubes, 13 green cubes, and 14 blue cubes

    total1 = 0
    for game_id, game_sets in game.items():
        for red, green, blue in game_sets:
            if red > 12 or green > 13 or blue > 14:
                break
        else:
            total1 += game_id

    print(f'Part 1: {total1}') # 2101


    # part 2

    total2 = 0
    for game_id, game_sets in game.items():
        min_red = 0
        min_green = 0
        min_blue = 0
        for red, green, blue in game_sets:
            min_red = max(min_red, red)
            min_green = max(min_green, green)
            min_blue = max(min_blue, blue)

        total2 += min_red * min_green * min_blue

    print(f'Part 2: {total2}') # 58269
