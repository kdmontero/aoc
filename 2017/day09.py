print("Advent of Code 2017 - Day 09: Stream Processing")

with open('day09.txt') as f:
    stream = f.readline()

# eliminate ignored characters
new_stream = ''
i = 0
while i < len(stream):
    if stream[i] == '!':
        i += 2
        continue
    new_stream += stream[i]
    i += 1

# eliminate and count garbage characters
final_stream = ''
inside_garbage = False
garbage = 0
i = 0
while i < len(new_stream):
    if not inside_garbage:
        if new_stream[i] == '<':
            inside_garbage = True
        else:
            final_stream += new_stream[i]
    
    else:
        if new_stream[i] == '>':
            inside_garbage = False
        else:
            garbage += 1

    i += 1

# count score
score = 0
impending_points = 0
for char in final_stream:
    if char == '{':
        impending_points += 1
        score += impending_points
    elif char == '}':
        impending_points -= 1

print(f'Part 1: {score}') # 23588 - part 1
print(f'Part 2: {garbage}') # 10045 - part 2
