from collections import defaultdict


if __name__ == '__main__':
    print("Advent of Code 2023 - Day 04: Scratchcards")

    with open('day04.txt') as f:
        cards = []
        for line in f.read().splitlines():
            title, given = line.split(': ')
            card_id = int(title.split()[1])

            winning_nums, my_nums = given.split(' | ')
            cards.append([card_id, [
                set([int(num) for num in winning_nums.split()]),
                set([int(num) for num in my_nums.split()])
            ]])


    # part 1

    points = 0
    for _, (winning_card, my_card) in cards:
        no_of_win = len(winning_card & my_card)
        if no_of_win == 0:
            continue
        elif no_of_win == 1:
            points += 1
        else:
            points += 2**(no_of_win - 1)

    print(f'Part 1: {points}') # 23847


    # part 2

    scratchcards = 0
    copy_counter = defaultdict(int)
    for card_id, (winning_card, my_card) in cards:
        no_of_win = len(winning_card & my_card)
        for i in range(1, no_of_win + 1):
            copy_counter[card_id + i] += copy_counter[card_id] + 1
        scratchcards += 1 + copy_counter[card_id]
    
    print(f'Part 2: {scratchcards}') # 8570000
