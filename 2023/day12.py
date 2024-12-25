import re
from functools import lru_cache


if __name__ == '__main__':
    print("Advent of Code 2023 - Day 12: Hot Springs")

    with open('day12.txt') as f:
        reports = []
        damages = []
        for line in f.read().splitlines():
            report, damage = line.split()
            reports.append(report)
            damages.append(tuple(int(num) for num in damage.split(',')))
    
    # part 1
    
    def is_valid(report: str, damage: list[int]) -> bool:
        pattern = '^[.?]*'
        regex_damage = ['[#?]{' + str(num) + '}' for num in damage]
        pattern += '[.?]+'.join(regex_damage)
        pattern += '[.?]*$'
        return bool(re.findall(pattern, report))
    
    def count_valid(report: str, damage: list[int]) -> int:
        if '?' not in report:
            return 1
        
        total = 0
        for char in '.#':
            if not is_valid(report.replace('?', char, 1), damage):
                continue
            total += count_valid(report.replace('?', char, 1), damage)

        return total
    
    total1 = 0
    for report, damage in zip(reports, damages):
        total1 += count_valid(report, damage)
            
    print(f'Part 1: {total1}') # 7361


    # part 2

    @lru_cache
    def count_all(report: str, damage: tuple[int], damage_start: bool = False) -> int:
        if damage_start and report.startswith('.'):
            return 0

        if report.startswith('?'):
            return count_all(report.replace('?', '.', 1), damage, damage_start) + count_all(report.replace('?', '#', 1), damage, damage_start)

        if not report and not damage:
            return 1
        
        if not report and damage:
            return 0

        if report.startswith('.'):
            return count_all(report.lstrip('.'), damage)
        
        # default logic: report.startswith('#')
        if len(damage) == 0:
            return 0

        if damage[0] == 1:
            if len(report) > 1:
                if report[1] == '#':
                    return 0
                else:
                    return count_all(report[2:], damage[1:])
            else:
                return count_all(report[1:], damage[1:])

        damage = list(damage)
        damage[0] -= 1
        damage = tuple(damage)
        return count_all(report[1:], damage, True)
        

    total2 = 0
    for report, damage in zip(reports, damages):
        total2 += count_all('?'.join([report] * 5), damage * 5)

            
    print(f'Part 2: {total2}') # 83317216247365