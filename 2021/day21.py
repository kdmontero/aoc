if __name__ == '__main__':
    print("Advent of Code 2021 - Day 21: Dirac Dice")

    with open('day21.txt') as f:
        line1, line2 = f.read().strip().splitlines()
        P1_START = int(line1.split()[-1])
        P2_START = int(line2.split()[-1])


    # part 1
    def play(pos: int, dice_sum: int, score: int) -> tuple[int, int]:
        '''Given the current position, sum of the dice rolls, and the current
        score, this will output the next current position and the score after
        this round.
        '''

        landing_pos = ((dice_sum % 10) + pos) % 10
        if landing_pos == 0:
            landing_pos = 10
        new_score = score + landing_pos
        return (landing_pos, new_score)

    rolls = 0
    dice = 0
    score = {1: 0, 2: 0}
    pos = {1: P1_START, 2: P2_START}
    player = 1
    while score[1] < 1000 and score[2] < 1000:
        dice_sum = 0
        for _ in range(3):
            dice = (dice % 100) + 1
            dice_sum += dice
        rolls += 3

        pos[player], score[player] = play(pos[player], dice_sum, score[player])
        player = (player % 2) + 1

    if score[1] < score[2]:
        answer = rolls * score[1]
    elif score[1] > score[2]:
        answer = rolls * score[2]

    print(f'Part 1: {answer}') # 920580


    # part 2

    print(f'Part 2: {0}') #

