import re
from collections import deque, defaultdict


class MarbleRing:
    def __init__(self):
        self.ring = deque([0])

    def insert(self, marble):
        if marble % 23 == 0:
            self.ring.rotate(7)
            score = self.ring.popleft()
            return score + marble

        else:
            self.ring.rotate(-2)
            self.ring.appendleft(marble)
            return 0


if __name__ == '__main__':
    print("Advent of Code 2018 - Day 09: Marble Mania")

    with open('day09.txt') as f:
        pattern = re.compile(r'\d+')
        matches = pattern.findall(f.read())
        players = int(matches[0])
        marbles = int(matches[1])

    def find_winning_score(players: int, marbles: int) -> int:
        scores = defaultdict(int)
        highest_score = 0
        marble_ring = MarbleRing()

        for marble in range(marbles):
            player = marble % players
            scores[player] += marble_ring.insert(marble + 1)
            highest_score = max(highest_score, scores[player])

        return highest_score

    print(f'Part 1: {find_winning_score(players, marbles)}') # 423717

    print(f'Part 2: {find_winning_score(players, marbles * 100)}') # 3553108197
