from collections import OrderedDict

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


# part 2
valid_tickets = nearby_tickets
for i in sorted(invalid_tickets, reverse=True):
    valid_tickets.pop(i)

field_index = {}
indexes = set()
field_indexes = []

def check_value(value, field_range): # field_range is list of ranges
    for range_ in field_range:
        if value in range_:
            return True
    return False

def check_field(index, field):
    for ticket in valid_tickets:
        if not check_value(ticket[index], field):
            return False
    return True

for field in rules:
    valid_indexes = []
    for i in range(len(rules)):
        if not check_field(i, rules[field]):
            continue
        else:
            valid_indexes.append(i)
    field_indexes.append([field, valid_indexes])

field_indexes = OrderedDict(sorted(field_indexes, key=lambda x: len(x[1])))

ans = 1
for field in field_indexes.keys():
    for index in field_indexes[field]:
        if index not in indexes:
            field_index[field] = index
            indexes.add(index)
    
    if field.startswith('departure'):
        ans *= my_ticket[field_index[field]]

print(f'Part 2: {ans}') # 1429779530273