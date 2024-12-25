if __name__ == '__main__':
    print("Advent of Code 2017 - Day 15: Dueling Generators")
    
    FACTOR_A = 16807
    FACTOR_B = 48271
    DIVISOR = 2147483647
    
    with open('day15.txt') as f:
        A_init, B_init = (
            int(line.split()[-1]) for line in f.read().splitlines()
        )

    def is_matched(a, b):
        # uses bitwise operations: bitmasked left shift and right shift
        bin_a = ((a << 15) & 2147483647) >> 15
        bin_b = ((b << 15) & 2147483647) >> 15
        return bin_a == bin_b

    def judge_count(seq_a, seq_b, rounds):
        judge_count = 0
        for i in range(rounds):
            A_init = next(seq_a)
            B_init = next(seq_b)

            if is_matched(A_init, B_init):
                judge_count += 1

        return judge_count

    def generator(init, factor, divisor, multiple):
        while True:
            init = (init*factor) % divisor
            if init % multiple == 0:
                yield init

    
    # part 1

    seq_A1 = generator(A_init, FACTOR_A, DIVISOR, 1)
    seq_B1 = generator(B_init, FACTOR_B, DIVISOR, 1)

    print(f'Part 1: {judge_count(seq_A1, seq_B1, 40_000_000)}') # 597


    # part 2

    seq_A2 = generator(A_init, FACTOR_A, DIVISOR, 4)
    seq_B2 = generator(B_init, FACTOR_B, DIVISOR, 8)

    print(f'Part 2: {judge_count(seq_A2, seq_B2, 5_000_000)}') # 303
