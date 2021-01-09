import collections

with open('day04.txt') as f:
    records = []
    for line in f.read().splitlines():
        line = line.lstrip('[').replace(':', '-').replace(
            ' ', '-', 1)
        time, details = line.split('] ')
        time = [int(num) for num in time.split('-')]
        records.append(time + [details])


# part 1
records.sort(key=lambda x: (x[0], x[1], x[2], x[3], x[4]))
sleep_counter = collections.Counter()
for record in records:
    *_, minute, action = record
    if action.startswith('Guard'):
        id_ = int(action.split(' ')[1].lstrip('#'))
    record.insert(5, id_)
    if action == 'falls asleep':
        sleep_time = minute
    elif action == 'wakes up':
        sleep_counter[id_] += minute - sleep_time
# records = [year, month, day, hour, minute, guard_ID, action]

sleeper1 = max(sleep_counter, key=sleep_counter.get)

sleeper_sched = collections.Counter()
for *_, minute, _, action in [r for r in records if r[-2] == sleeper1 and 
    not r[-1].startswith('Guard')]:
        if action == 'falls asleep':
            sleep_time = minute
        elif action == 'wakes up':
            sleeper_sched += collections.Counter(range(sleep_time, minute))

sleepy_time1 = max(sleeper_sched, key=sleeper_sched.get)

print(f'Part 1: {sleepy_time1*sleeper1}') # 21956


# part 2
guards_sched = {}
for *_, minute, guard, action in [r for r in records if not 
    r[-1].startswith('Guard')]:
        if guard not in guards_sched:
            guards_sched[guard] = collections.Counter()
        if action == 'falls asleep':
            sleep_time = minute
        elif action == 'wakes up':
            guards_sched[guard] += collections.Counter(range(sleep_time, minute))

sleeper2 = max(guards_sched, key=lambda guard: max(guards_sched[guard].values()))
sleepy_time2 = max(guards_sched[sleeper2], key=guards_sched[sleeper2].get)

print(f'Part 2: {sleeper2*sleepy_time2}') # 134511