if __name__ == "__main__":
    print("Advent of Code 2021 - Day 01: Sonar Sweep")

    with open('day01.txt') as f:
        depths = [int(x) for x in f.read().splitlines()]

    # part 1
    increase1 = 0
    for a, b in zip(depths, depths[1:]):
        if b > a:
            increase1 += 1

    print(f'Part 1: {increase1}') # 1766


    # part 2
    increase2 = 0
    for a, b, c, d in zip(depths, depths[1:], depths[2:], depths[3:]):
        if b + c + d > a + b + c:
            increase2 += 1

    print(f'Part 2: {increase2}') # 1797
