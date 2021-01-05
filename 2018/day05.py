with open('day05.txt') as f:
    given_polymers = f.read().strip()

# part 1
def polymerize(polymers):
    polymers = list(polymers)
    i = save = 0
    while i < len(polymers) - 1:
        if abs(ord(polymers[i]) - ord(polymers[i+1])) == 32:
            del polymers[i:i+2]
            i = max(0, save - 1)
            save = i
            continue
        i += 1
        save = i
    return len(polymers)

print(f'Part 1: {polymerize(given_polymers)}') # 10638


# part 2
min_polymers = 10000
for i in range(26):
    polymers_i = given_polymers.replace(chr(97+i), '').replace(chr(65+i),'')
    min_polymers = min(min_polymers, polymerize(polymers_i))

print(f'Part 2: {min_polymers}') # 4944