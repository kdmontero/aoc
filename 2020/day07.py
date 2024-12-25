print("Advent of Code 2020 - Day 07: Handy Haversacks")
with open('day07.txt') as f:
    lines = f.read().split('\n')
    rules = {}
    for line in lines:
        outer, inner = line.split(' bags contain ')
        inner = inner.replace(' bags','').replace(' bag','').rstrip('.').split(', ')
        inner_parsed = []
        for element in inner:
            try:
                num = int(element[0])
                inner_parsed.append((num, element[2:]))
            except ValueError:
                inner_parsed.append((0, element))
        rules[outer] = inner_parsed

# part 1
valid = {'shiny gold'}
invalid = {'no other'}

def is_valid(bag):
    if bag in valid:
        return True
    elif set(inner[1] for inner in rules[bag]).issubset(invalid):
        invalid.add(bag)
        return False
    else:
        for inner in rules[bag]:
            if is_valid(inner[1]):
                valid.add(bag)
                return True

contains_shiny_gold = 0
for bag in rules:
    if is_valid(bag):
        contains_shiny_gold += 1

print(f'Part 1: {contains_shiny_gold - 1}') # 272


# part 2
def total_bags(num, color):
    if rules[color] == [(0, 'no other')]:
        return num
    total = 0
    for qty, bag in rules[color]:
        total += total_bags(qty, bag)
    return (num*total)+num

print(f'Part 2: {total_bags(1, "shiny gold") - 1}') # 172246
