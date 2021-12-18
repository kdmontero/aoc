from collections import Counter

if __name__ == '__main__':
    print('Advent of Code 2021 - Day 06')
    with open('day06.txt') as f:
        given_timer = Counter([int(x) for x in f.read().split(',')])
    
    def lanternfish_after_day(day, timer):
        for _ in range(day):
            new_timer = Counter()
            for i in range(9):
                if i == 0:
                    new_timer[6] = timer[i]
                    new_timer[8] = timer[i]
                else:
                    new_timer[i-1] += timer[i]
        return sum(new_timer.values())
    
    # part 1
    print(f'Part 1: {lanternfish_after_day(80, given_timer)}') # 376194

    # part 2
    print(f'Part 2: {lanternfish_after_day(256, given_timer)}') # 1693022481538
