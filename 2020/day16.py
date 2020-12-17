from copy import deepcopy

with open('day16.txt') as f:
    rules = {}
    nearby_tickets = []
    given1, given2, given3 = f.read().split('\n\n')
    for rule in given1.splitlines():
        key, value = rule.split(': ')
        rules[key] = value.split(' or ')
    for key, value in rules.items():
        temp_rule = []
        for range_ in value:
            lower, upper = range_.split('-')
            temp_rule.append(range(int(lower), int(upper) + 1))
        rules[key] = temp_rule
    
    my_ticket = [int(num) for num in given2.splitlines()[1].split(',')]

    for ticket in given3.splitlines()[1:]:
        nearby_tickets.append([int(num) for num in ticket.split(',')])


# part 1
def check_validity(num):
    for rule in rules.values():
        for range_ in rule:
            if num in range_:
                return True
    return False

error_rate = 0
invalid_tickets = []
for i, ticket in enumerate(nearby_tickets):
    for value in ticket:
        if not check_validity(value):
            error_rate += value
            if i not in invalid_tickets:
                invalid_tickets.append(i)

print(f'Part 1: {error_rate}') # 28882