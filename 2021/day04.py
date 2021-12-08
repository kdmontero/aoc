class BingoCard:
    def __init__(self, card):
        self.card = {(x, y): card[x][y] for x in range(5) for y in range(5)}
        self.mark = [[0]*5 for _ in range(5)]
        self.value_set = set(self.card.values())
        self.pre_score = sum([sum(row) for row in card])
        self.score = 0
        self.complete = False

    def update(self, draw):
        if draw in self.value_set:
            for x in range(5):
                for y in range(5):
                    if self.card[(x, y)] == draw:
                        self.mark[x][y] = 1
                        self.pre_score -= draw
                        self.score = draw * self.pre_score

                        if self.check():
                            self.complete = True
                                
    def check(self):
        for row in self.mark:
            if sum(row) == 5:
                return True
        for col in zip(*self.mark):
            if sum(col) == 5:
                return True
        return False


if __name__ == '__main__':
    print('Advent of Code 2021 - Day 04')

    with open('day04.txt') as f:
        draw_list, *cards_raw = f.read().split('\n\n')
        draw_list = [int(i) for i in draw_list.split(',')]

        cards = []
        for card_raw in cards_raw:
            card_raw = card_raw.split('\n')

            card = []
            for row in card_raw:
                card.append([int(i) for i in row.split()])
            
            cards.append(BingoCard(card))

    winning_score = losing_score = 0
    total_cards = len(cards)
    cards_won = set()
    for draw in draw_list:
        for i, card in enumerate(cards):
            card.update(draw)

            if card.complete:
                cards_won.add(i)
                
                if winning_score == 0:
                    winning_score = card.score

                if len(cards_won) == total_cards and losing_score == 0:
                    losing_score = card.score


    print(f'Part 1: {winning_score}') # 11536 - part 1

    print(f'Part 2: {losing_score}') # 1284 - part 2
