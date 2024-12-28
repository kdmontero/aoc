if __name__ == '__main__':
    print("Advent of Code 2022 - Day 25: Full of Hot Air")

    with open('day25.txt') as f:
        fuel_nums = [line for line in f.read().strip().splitlines()]


    def snafu_to_decimal(snafu: str) -> int:
        decimal = 0
        for i, s_digit in enumerate(snafu[::-1]):
            if s_digit == '=':
                d_digit = -2
            elif s_digit == '-':
                d_digit = -1
            else:
                d_digit = int(s_digit)

            decimal += (5 ** i) * d_digit
        return decimal

    def decimal_to_snafu(given: int) -> str:

        # find the length of SNAFU digits
        i = 0
        num = 2 * (5 ** i)
        while num < given:
            i += 1
            num += 2 * (5 ** i)

        # i+1 = length of SNAFU digits

        # find the leftmost digit, this is either 1 or 2
        if snafu_to_decimal('1' + '2' * i) >= given:
            snafu = '1' + 'X' * i
        else:
            snafu = '2' + 'X' * i

        # populate the rest of the digits 1-by-1 by finding the correct bound
        while 'X' in snafu:
            for next_digit in ['=', '-', '0', '1', '2']:
                low_bound = snafu.replace('X', next_digit, 1).replace('X', '=')
                up_bound = snafu.replace('X', next_digit, 1).replace('X', '2')
                low_bound_decimal = snafu_to_decimal(low_bound)
                up_bound_decimal = snafu_to_decimal(up_bound)

                if low_bound_decimal <= given <= up_bound_decimal:
                    snafu = snafu.replace('X', next_digit, 1)

        return snafu

    total = sum([snafu_to_decimal(snafu) for snafu in fuel_nums])
    print(f'Part 1: {decimal_to_snafu(total)}') # 2=0--0---11--01=-100

    print(f'Part 2: Complete all 49 stars in Advent of Code 2022')

