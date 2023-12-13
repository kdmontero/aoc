import re
from functools import lru_cache


if __name__ == '__main__':
    print('Advent of Code 2023 - Day 12')

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


    # total2 = 0
    # for report, damage in zip(reports, damages):
    #     print(report, damage)
    #     total2 += count_valid('?'.join([report] * 5), damage * 5)

            
    # print(f'Part 2: {total2}') #