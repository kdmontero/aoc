class Ingredient:
    def __init__(self, name, capacity, durability, flavor, texture, calories):
        self.name = name
        self.capacity = capacity
        self.durability = durability
        self.flavor = flavor
        self.texture = texture
        self.calories = calories

with open('day15.txt') as f:
    ingredients = []
    for line in f.read().splitlines():
        line = line.replace(':', '').replace(',', '').split()
        name, _, cap, _, dur, _, flv, _, txt, _, cal = line
        ingredients.append(
            Ingredient(name, int(cap), int(dur), int(flv), int(txt), int(cal))
        )

max_score = max_score_with_cal = 0
for a in range(101):
    for b in range(101-a):
        for c in range(101-a-b):
            d = 100-a-b-c
            total_cap = total_dur = total_flv = total_txt = total_cal = 0
            for amount, ingr in zip([a,b,c,d],ingredients):
                total_cap += amount*ingr.capacity
                total_dur += amount*ingr.durability
                total_flv += amount*ingr.flavor
                total_txt += amount*ingr.texture
                total_cal += amount*ingr.calories
            total_cap = max(0, total_cap)
            total_dur = max(0, total_dur)
            total_flv = max(0, total_flv)
            total_txt = max(0, total_txt)
            total_cal = max(0, total_cal)
            max_score = max(max_score, total_cap*total_dur*total_flv*total_txt)
            if total_cal == 500:
                max_score_with_cal = max(
                    max_score_with_cal, total_cap*total_dur*total_flv*total_txt
                )

print(f'Part 1: {max_score}') # 21367368 - part 1
print(f'Part 2: {max_score_with_cal}') # 1766400 - part 2