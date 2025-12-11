if __name__ == '__main__':
    print("Advent of Code 2025 - Day 01: Secret Entrance")

    with open('day01.txt') as f:
        rotations = f.read().strip().splitlines()


    def rotate(pw2_count: int, cur: int, rotation: str) -> tuple[int, str]:
        direction = rotation[0]
        roundtrip, steps = divmod(int(rotation[1:]), 100)
        destination = None

        if direction == 'R':
            if steps + cur <= 99:
                destination = cur + steps
            else:
                destination = cur + steps - 100
                pw2_count += 1
        elif direction == 'L':
            if cur - steps >= 0:
                destination = cur - steps
                if (destination == 0 and steps != 0):
                    pw2_count += 1
            else:
                destination = cur - steps + 100
                if cur != 0:
                    pw2_count += 1

        pw2_count += roundtrip

        return pw2_count, destination

    cur = 50
    pw1_count = 0
    pw2_count = 0

    for rotation in rotations:
        pw2_count, cur = rotate(pw2_count, cur, rotation)
        if cur == 0:
            pw1_count += 1

    print(f'Part 1: {pw1_count}') # 1097

    print(f'Part 2: {pw2_count}') # 7101

