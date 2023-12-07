from __future__ import annotations
from collections import Counter
from copy import deepcopy


if __name__ == '__main__':
    print('Advent of Code 2023 - Day 07')

    with open('day07.txt') as f:
        hands = []
        for line in f.read().splitlines():
            hand, bid = line.split()
            hands.append([hand, int(bid)])
    

    # part 1

    class Hand:
        index = {str(i): i for i in range(2,10)}
        index['T'] = 10
        index['J'] = 11
        index['Q'] = 12
        index['K'] = 13
        index['A'] = 14

        def __init__(self, cards: str, bid: int) -> None:
            self.cards = cards
            self.bid = bid
        
        @property
        def counter(self):
            self._counter = Counter(self.cards)
            return self._counter
        
        @property
        def strength(self):
            if 5 in self.counter.values(): # five of a kind
                self._strength = 7
            elif 4 in self.counter.values(): # four of a kind
                self._strength = 6
            elif {3, 2} == set(self.counter.values()): # full house
                self._strength = 5
            elif {3, 1} == set(self.counter.values()): # three of a kind
                self._strength = 4
            elif {2, 1} == set(self.counter.values()) and len(self.counter) == 3: # two pairs
                self._strength = 3
            elif {2, 1} == set(self.counter.values()) and len(self.counter) == 4: # one pair
                self._strength = 2
            elif len(self.counter) == 5: # high card
                self._strength = 1
            else:
                raise NotImplementedError("Hand strength can't be computed")
            return self._strength
        
        def __lt__(self, other: Hand) -> bool:
            if self.strength < other.strength:
                return True
            elif self.strength == other.strength:
                for self_card, other_card in zip(self.cards, other.cards):
                    if self.index[self_card] < self.index[other_card]:
                        return True
                    elif self.index[self_card] > self.index[other_card]:
                        return False
            return False
        
        def __eq__(self, other: Hand) -> bool:
            if self.cards == other.cards:
                return True
            return False
        
    def compute_winnigs(hands: list[Hand]) -> int:
        hands.sort()
        winnings= 0
        for i, hand in enumerate(hands, 1):
            winnings += i * hand.bid
        return winnings

    hands1 = [Hand(hand, bid) for hand, bid in hands]
    print(f'Part 1: {compute_winnigs(hands1)}') # 251106089


    # part 2
    
    class HandJoker(Hand):
        index = deepcopy(Hand.index)
        index['J'] = 1

        @property
        def counter(self):
            orig_counter = Counter(self.cards)
            if 'J' not in self.cards:
                self._counter = orig_counter
                return self._counter

            self._counter = {key: value for key, value in orig_counter.items() if key != 'J'}
            if len(self._counter) == 0:
                self._counter = {'A': 5}
                return self._counter

            leading_card = max(self._counter, key=lambda x: self._counter[x])
            self._counter[leading_card] += orig_counter['J']
            return self._counter

    hands2 = [HandJoker(hand, bid) for hand, bid in hands]
    print(f'Part 2: {compute_winnigs(hands2)}') # 249620106