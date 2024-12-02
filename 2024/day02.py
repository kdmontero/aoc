if __name__ == '__main__':
    print('Advent of Code 2024 - Day 02')

    with open('day02.txt') as f:
        reports = []
        for line in f.read().splitlines():
            raw_report = line.strip().split()
            report = [int(level) for level in raw_report]
            reports.append(report)


    # part 1

    def is_safe(report):
        if report == sorted(report):
            for i, num in enumerate(report[:-1]):
                if report[i+1] - num not in {1, 2, 3}:
                    break
            else:
                return True

            return False

        if report == sorted(report, reverse=True):
            for i, num in enumerate(report[:-1]):
                if num - report[i+1] not in {1, 2, 3}:
                    break
            else:
                return True

            return False

        return False


    total_safe1 = 0
    for report in reports:
        if is_safe(report):
            total_safe1 += 1

    print(f'Part 1: {total_safe1}') # 524


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

    total_safe2 = 0
    for report in reports:
        if modified_is_safe(report):
            total_safe2 += 1

    print(f'Part 2: {total_safe2}') # 569

