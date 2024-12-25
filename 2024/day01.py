from collections import Counter


if __name__ == '__main__':
    print("Advent of Code 2024 - Day 01: Historian Hysteria")

    with open('day01.txt') as f:
        group1 = []
        group2 = []
        for line in f.read().splitlines():
            a, b = line.strip().split()
            group1.append(int(a))
            group2.append(int(b))


    # part 1

    group1.sort()
    group2.sort()

    total_distance = 0
    for num1, num2 in zip(group1, group2):
        total_distance += abs(num1 - num2)

    print(f'Part 1: {total_distance}') # 2196996


    # part 2

    counter = Counter(group2)

    similarity_score = 0
    for num in group1:
        similarity_score += num * counter[num]

    print(f'Part 2: {similarity_score}') # 23655822

