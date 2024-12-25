from collections import defaultdict


if __name__ == '__main__':
    print("Advent of Code 2018 - Day 12: Subterranean Sustainability")

    with open('day12.txt') as f:
        raw_pots, raw_notes = f.read().strip().split('\n\n')
        pots = raw_pots.replace('initial state: ', '')
        state = (pots, 0, len(pots) - 1)
        notes = defaultdict(lambda: '.')
        for note in raw_notes.splitlines():
            pattern, outcome = note.split(' => ')
            notes[pattern] = outcome


    # part 1

    def next_gen(state: tuple[str, int, int]) -> tuple[str, int, int]:
        pots, first, last = state
        pots = '....' + pots + '....'
        next_pots = ''
        next_first = None
        for i in range(2, len(pots) - 2):
            next_pot = notes[pots[i-2:i+3]]
            next_pots += next_pot
            if next_first == None and next_pot == '#':
                next_first = (first - 4) + i
        next_pots = next_pots.strip('.')
        next_last = next_first + len(next_pots) - 1
        return (next_pots, next_first, next_last)
            
    for i in range(20):
        state = next_gen(state)

    plant_label_sum = 0
    pots, first, last = state
    for i, pot in enumerate(pots):
        if pot == '#':
            plant_label_sum += first + i

    print(f'Part 1: {plant_label_sum}') # 1733


    # part 2

    print(f'Part 2: {0}') #

