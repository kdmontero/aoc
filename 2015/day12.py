import json

print("Advent of Code 2015 - Day 12: JSAbacusFramework.io")
with open('day12.txt') as f:
    doc = json.loads(f.read())

# part 1
def get_sum1(obj):
    if isinstance(obj, int):
        return obj
    
    elif isinstance(obj, list):
        return sum(get_sum1(num) for num in obj)
    
    elif isinstance(obj, str):
        return 0
    
    elif isinstance(obj, dict):
        return sum(get_sum1(num) for num in obj.keys()) + sum(get_sum1(num) for num in obj.values())

print(f'Part 1: {get_sum1(doc)}') # 111754


# part 2
def get_sum2(obj):
    if isinstance(obj, int):
        return obj
    
    elif isinstance(obj, list):
        return sum(get_sum2(num) for num in obj)
    
    elif isinstance(obj, str):
        return 0
    
    elif isinstance(obj, dict):
        if 'red' in obj.values():
            return 0
        else:
            return sum(get_sum2(num) for num in obj.keys()) + sum(get_sum2(num) for num in obj.values())

print(f'Part 2: {get_sum2(doc)}') # 65402
