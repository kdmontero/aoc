from collections import deque
from copy import deepcopy

with open('day22.txt') as f:
    player1, player2 = f.read().split('\n\n')
    given_player1 = deque(int(num) for num in player1.splitlines()[1:])
    given_player2 = deque(int(num) for num in player2.splitlines()[1:])

def play(player1, player2):
    while len(player1) > 0 and len(player2) > 0:
        play1 = player1.popleft()
        play2 = player2.popleft()
        if play1 > play2:
            player1.append(play1)
            player1.append(play2)
            winner = player1
        else:
            player2.append(play2)
            player2.append(play1)
            winner = player2
    return winner

player1 = deepcopy(given_player1)
player2 = deepcopy(given_player2)
winner = play(player1, player2)
score1 = 0
winner.reverse()
for i, card in enumerate(winner):
    score1 += card * (i+1)

print(f'Part 1: {score1}') # 33772