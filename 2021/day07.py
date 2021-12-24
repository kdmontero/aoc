import statistics

if __name__ == '__main__':
    print('Advent of Code 2021 - Day 07')
    with open('day07.txt') as f:
        crabs = [int(i) for i in f.read().split(',')]
    
    # part 1
    
    target = round(statistics.median(crabs[:]))
    min_fuel1 = 0
    for crab in crabs:
        min_fuel1 += abs(crab - target)
        
    print(f'Part 1: {min_fuel1}') # 344735
    
    
    # part 2
    
    min_fuel2 = 999_999_999_999_999
    for target in range(min(crabs), max(crabs)+1):
        fuel = 0
        for crab in crabs:
            difference = abs(target - crab)
            fuel += (difference * (difference + 1))//2
        min_fuel2 = min(min_fuel2, fuel)
    
    print(f'Part 2: {min_fuel2}') # 96798233
