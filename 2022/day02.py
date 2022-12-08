if __name__ == '__main__':
    print('Advent of Code 2022 - Day 02')

    with open('day02.txt') as f:
        guide = [line.split() for line in f.read().splitlines()]

    convert_opponent_move = {
        'A': 'Rock',
        'B': 'Paper',
        'C': 'Scissors'
    }


    # part 1

    def play1(opponent_move: str, player_move: str) -> int:

        if opponent_move == player_move:
            round_score = 3 # draw
        elif any((
            ((opponent_move == 'Rock') and (player_move == 'Paper')),
            ((opponent_move == 'Paper') and (player_move == 'Scissors')),
            ((opponent_move == 'Scissors') and (player_move == 'Rock'))
        )):
            round_score  = 6 # won
        else:
            round_score  = 0 # lost


        if player_move == 'Rock':
            move_score = 1
        elif player_move == 'Paper':
            move_score = 2
        elif player_move == 'Scissors':
            move_score = 3

        return round_score + move_score

    convert_player_move = {
        'X': 'Rock',
        'Y': 'Paper',
        'Z': 'Scissors'
    }

    total_score1 = 0
    for round_ in guide:
        O, P = round_

        opponent_move = convert_opponent_move[O]
        player_move = convert_player_move[P]

        total_score1 += play1(opponent_move, player_move)


    print(f'Part 1: {total_score1}') # 10404


    # part 2
    
    def play2(opponent_move: str, result: str) -> int:

        if any((
            ((opponent_move == 'Rock') and (result == 'Draw')),
            ((opponent_move == 'Paper') and (result == 'Lost')),
            ((opponent_move == 'Scissors') and (result == 'Won'))
        )):
            move_score = 1 # rock
        elif any((
            ((opponent_move == 'Rock') and (result == 'Won')),
            ((opponent_move == 'Paper') and (result == 'Draw')),
            ((opponent_move == 'Scissors') and (result == 'Lost'))
        )):
            move_score = 2 # paper
        elif any((
            ((opponent_move == 'Rock') and (result == 'Lost')),
            ((opponent_move == 'Paper') and (result == 'Won')),
            ((opponent_move == 'Scissors') and (result == 'Draw'))
        )):
            move_score = 3 # scissors


        if result == 'Lost':
            round_score = 0
        elif result == 'Draw':
            round_score = 3
        elif result == 'Won':
            round_score = 6

        return round_score + move_score

    convert_result = {
        'X': 'Lost',
        'Y': 'Draw',
        'Z': 'Won'
    }

    total_score2 = 0
    for round_ in guide:
        O, R = round_

        opponent_move = convert_opponent_move[O]
        result = convert_result[R]

        total_score2 += play2(opponent_move, result)

    print(f'Part 2: {total_score2}') # 10334
