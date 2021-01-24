with open('day10.txt') as f:
    ins = {}
    start = []
    for line in f.read().splitlines():
        if line.startswith('value'):
            val, bot = line.replace('value ', '').split(' goes to ')
            start.append([int(val), bot])
        else:
            line = line.replace(' gives low to ', '-').replace(
                    ' and high to ', '-')
            b_bot, low, high = line.split('-')
            ins[b_bot] = [low, high]

# part 1
bot = {}
queue = []
for instruction in start:
    val, b_bot = instruction
    if b_bot not in bot:
        bot[b_bot] = [val]
    else:
        bot[b_bot].append(val)
        queue.append(b_bot)

while queue:
    b_bot = queue.pop()

    if 61 in bot[b_bot] and 17 in bot[b_bot]:
        bot_num = int(b_bot.split(' ')[1])

    low_val = min(bot[b_bot]) 
    high_val = max(bot[b_bot]) 
    low_bot = ins[b_bot][0]
    high_bot = ins[b_bot][1]
    bot[b_bot] = []
    if low_bot not in bot:
        bot[low_bot] = [low_val]
    else:
        bot[low_bot].append(low_val)
        queue.append(low_bot)
    if high_bot not in bot:
        bot[high_bot] = [high_val]
    else:
        bot[high_bot].append(high_val)
        queue.append(high_bot)

print(f'Part 1: {bot_num}') # 27


# part 2
output_chips = bot['output 0'][0] * bot['output 1'][0] * bot['output 2'][0]

print(f'Part 2: {output_chips}') # 13727
