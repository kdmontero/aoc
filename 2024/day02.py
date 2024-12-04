if __name__ == '__main__':
    print('Advent of Code 2024 - Day 02')

    with open('day02.txt') as f:
        reports = []
        for line in f.read().splitlines():
            raw_report = line.strip().split()
            report = [int(level) for level in raw_report]
            reports.append(report)


    # part 1

    def is_safe(report: list[int]) -> bool:
        diff = set()
        for i, num in enumerate(report[:-1]):
            diff.add(report[i+1] - num)
        return diff.issubset({1, 2, 3}) or diff.issubset({-1, -2, -3})

    total_safe = 0
    unsafe_reports = []
    for report in reports:
        if is_safe(report):
            total_safe += 1
        else:
            unsafe_reports.append(report)

    print(f'Part 1: {total_safe}') # 524


    # part 2

    def modified_is_safe(report):
        if not is_safe(report):
            for i in range(len(report)):
                tolerated_report = report[:]
                del tolerated_report[i]

                if is_safe(tolerated_report):
                    return True

            else:
                return False

        return True

    additional_safe = 0
    for report in unsafe_reports:
        if modified_is_safe(report):
            additional_safe += 1

    print(f'Part 2: {total_safe + additional_safe}') # 569

