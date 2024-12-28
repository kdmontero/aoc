from functools import lru_cache


if __name__ == '__main__':
    print("Advent of Code 2022 - Day 21: Monkey Math")

    with open('day21.txt') as f:
        jobs = {}
        for line in f.read().strip().splitlines():
            monkey, raw_job = line.split(': ')
            job = raw_job.split()
            if len(job) == 1:
                jobs[monkey] = int(job[0])
            elif len(job) == 3:
                jobs[monkey] = job


    # part 1

    done = {}
    for monkey, job in jobs.items():
        if type(job) == int:
            done[monkey] = job

    def get_monkey_num(monkey: str) -> int:
        if monkey in done:
            return done[monkey]

        monkey1, op, monkey2 = jobs[monkey]
        if op == '+':
            value = get_monkey_num(monkey1) + get_monkey_num(monkey2)
        elif op == '-':
            value = get_monkey_num(monkey1) - get_monkey_num(monkey2)
        elif op == '*':
            value = get_monkey_num(monkey1) * get_monkey_num(monkey2)
        elif op == '/':
            value = get_monkey_num(monkey1) // get_monkey_num(monkey2)

        done[monkey] = value
        return value

    print(f'Part 1: {get_monkey_num("root")}') # 331120084396440


    # part 2

    affected = []

    @lru_cache
    def is_affected(monkey: str) -> bool:
        '''checks if monkey is part of the path from root to humn'''
        if monkey in ('humn'):
            affected.append(monkey)
            return True
        if type(jobs[monkey]) == int:
            return False

        monkey1, _, monkey2 = jobs[monkey]
        answer = is_affected(monkey1) or is_affected(monkey2)
        if answer:
            affected.append(monkey)
        return answer

    is_affected('root')

    def set_value(monkey: str, target: int) -> int:
        if monkey == 'humn':
            return target

        monkey1, op, monkey2 = jobs[monkey]
        if monkey1 in affected:
            unknown, known = monkey1, monkey2
        elif monkey2 in affected:
            unknown, known = monkey2, monkey1

        if op == '+':
            corrected_val = target - done[known]
        elif op == '*':
            corrected_val = target // done[known]
        elif op == '-':
            if monkey1 == unknown:
                corrected_val = target + done[known]
            elif monkey2 == unknown:
                corrected_val = done[known] - target
        elif op == '/':
            if monkey1 == unknown:
                corrected_val = target * done[known]
            elif monkey2 == unknown:
                corrected_val = done[known] // target

        return set_value(unknown, corrected_val)
         
    monkey1, _, monkey2 = jobs['root']
    if monkey1 in affected:
        humn_value = set_value(monkey1, done[monkey2])
    else:
        humn_value = set_value(monkey2, done[monkey1])

    print(f'Part 2: {humn_value}') # 3378273370680

