if __name__ == '__main__':
    print('Advent of Code 2022 - Day 06')

    with open('day06.txt') as f:
        signal = f.read()


    def find_marker(signal: str, distinct_num: int) -> int:
        for marker in range(distinct_num, len(signal)):
            if len(set(signal[marker-distinct_num:marker])) == distinct_num:
                return marker

    print(f'Part 1: {find_marker(signal, 4)}') # 1760 - part 1

    print(f'Part 2: {find_marker(signal, 14)}') # 2974 - part 2
