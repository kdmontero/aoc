import collections

with open('day06.txt') as f:
    messages = f.read().splitlines()

char_counter = [collections.Counter() for _ in range(len(messages[0]))]

for msg in messages:
    for i, char in enumerate(msg):
        char_counter[i][char] += 1

error_corrected1 = ''
error_corrected2 = ''
for counter in char_counter:
    error_corrected1 += max(counter.keys(), key=counter.get)
    error_corrected2 += min(counter.keys(), key=counter.get)

print(f'Part 1: {error_corrected1}') # umejzgdw - part 1
print(f'Part 2: {error_corrected2}') # aovueakv - part 2