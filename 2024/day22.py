from collections import defaultdict


if __name__ == '__main__':
    print("Advent of Code 2024 - Day 22: Monkey Market")

    with open('day22.txt') as f:
        secret_nums = [int(num) for num in f.read().strip().splitlines()]


    # part 1

    def get_next_secret(secret: int) -> int:
        state1 = ((secret * 64) ^ secret) % 16777216
        state2 = ((state1 //32) ^ state1) % 16777216
        state3 = ((state2 * 2048) ^ state2) % 16777216
        return state3

    diff_seq = []
    total_secret_num = 0
    for secret in secret_nums:
        seq = []
        for _ in range(2000):
            price = secret % 10
            next_secret = get_next_secret(secret)
            next_price = next_secret % 10
            seq.append([next_price - price, next_price]) # [diff, price]
            secret = next_secret

        total_secret_num += secret
        diff_seq.append(seq)

    print(f'Part 1: {total_secret_num}') # 20506453102


    # part 2

    max_diff_seq = defaultdict(int)
    for diff in diff_seq:
        seen_seq = set()
        for i in range(3, 2000):
            price = diff[i][1]
            seq = (diff[i-3][0], diff[i-2][0], diff[i-1][0], diff[i][0])
            if seq in seen_seq:
                continue

            seen_seq.add(seq)
            max_diff_seq[seq] += price

    max_bananas = max(max_diff_seq.values())
    print(f'Part 2: {max_bananas}') # 2423

