from collections import deque
from copy import deepcopy

print('Advent of Code 2020 - Day 22')
with open('day22.txt') as f:
    player1, player2 = f.read().split('\n\n')
    given_player1 = deque(int(num) for num in player1.splitlines()[1:])
    given_player2 = deque(int(num) for num in player2.splitlines()[1:])

def play(player1, player2):
    while len(player1) > 0 and len(player2) > 0:
        play1 = player1.popleft()
        play2 = player2.popleft()
        if play1 > play2:
            player1.extend((play1, play2))
            winner = player1
        else:
            player2.extend((play2, play1))
            winner = player2
    return winner

player1 = deepcopy(given_player1)
player2 = deepcopy(given_player2)
winner = play(player1, player2)
score1 = 0
winner.reverse()
for i, card in enumerate(winner):
    score1 += card * (i + 1)

print(f'Part 1: {score1}') # 33772


# part 2
def recursive_combat(player1, player2):
    states = set()
    while True:
        state = (tuple(player1), tuple(player2))
        if state in states:
            return 'Player 1'
        states.add(state)

        play1, play2 = player1.popleft(), player2.popleft()

        if play1 <= len(player1) and play2 <= len(player2):
            sub_player1 = deque(deepcopy(list(player1)[:play1]))
            sub_player2 = deque(deepcopy(list(player2)[:play2]))

            if not (sub_player1 and sub_player2):
                pass
            else:
                sub_winner = recursive_combat(sub_player1, sub_player2)
                if sub_winner == 'Player 1':
                    player1.extend((play1, play2))
                elif sub_winner == 'Player 2':
                    player2.extend((play2, play1))
                
                if len(player1) == 0:
                    return 'Player 2'
                elif len(player2) == 0:
                    return 'Player 1'
                continue

        if play1 > play2:
            player1.extend((play1, play2))
        else:
            player2.extend((play2, play1))

        if len(player1) == 0:
            return 'Player 2'
        elif len(player2) == 0:
            return 'Player 1'

player1 = deepcopy(given_player1)
player2 = deepcopy(given_player2)
winner = recursive_combat(player1, player2)
if winner == 'Player 1':
    winner_cards = player1
elif winner == 'Player 2':
    winner_cards = player2

score2 = 0
winner_cards.reverse()
for i, card in enumerate(winner_cards):
    score2 += card * (i + 1)

print(f'Part 2: {score2}') # 35070
