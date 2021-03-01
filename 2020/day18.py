from collections import deque
from copy import deepcopy

print('Advent of Code 2020 - Day 18')
with open('day18.txt') as f:
    given_homework = [[char for char in expression.split(' ')]
        for expression in f.read().splitlines()]


# part 1
homework = deepcopy(given_homework)
def solve(num1, operation, num2):
    if operation == '+':
        return str(int(num1.lstrip('(')) + int(num2.rstrip(')')))
    elif operation == '*':
        return str(int(num1.lstrip('(')) * int(num2.rstrip(')')))

def evaluate(expression):
    expression = deque(expression)
    while len(expression) != 1:
        num1 = expression.popleft()
        operation = expression.popleft()
        num2 = expression.popleft()
        expression.appendleft(solve(num1, operation, num2))
    return expression[0]

def find_p(expression):
    open_i = None
    close_i = None
    for i in range(0, len(expression), 2):
        if expression[i].startswith('('):
            open_i = i
        elif expression[i].endswith(')'):
            close_i = i
            return open_i, close_i
    return

total1 = 0
for expression in homework:
    while len(expression) != 1:
        try:
            open_i, close_i = find_p(expression)
        except:
            total1 += int(evaluate(expression))
            break
        
        open_p = expression[open_i].count('(')
        close_p = expression[close_i].count(')')
        num = evaluate(expression[open_i:close_i+1])
        if open_p > close_p:
            num = (open_p-close_p)*'(' + num
        elif close_p > open_p:
            num += (close_p-open_p)*')'
        del expression[open_i:close_i+1]
        expression.insert(open_i, num)
    
print(f'Part 1: {total1}') # 650217205854


# part 2
def advance_eval(expression):
    while len(expression) != 1:
        if '+' in expression:
            i = expression.index('+')
            num1, operation, num2 = expression[i-1:i+2]
            del expression[i-1:i+2]
            expression.insert(i-1, solve(num1, operation, num2))
        else:
            expression = deque(expression)
            num1 = expression.popleft()
            operation = expression.popleft()
            num2 = expression.popleft()
            expression.appendleft(solve(num1, operation, num2))
    return expression[0]

total2 = 0
homework = deepcopy(given_homework)
for expression in homework:
    while True:
        try:
            open_i, close_i = find_p(expression)
        except:
            total2 += int(advance_eval(expression))
            break
        
        open_p = expression[open_i].count('(')
        close_p = expression[close_i].count(')')
        num = advance_eval(expression[open_i:close_i+1])
        if open_p > close_p:
            num = (open_p-close_p)*'(' + num
        elif close_p > open_p:
            num += (close_p-open_p)*')'
        del expression[open_i:close_i+1]
        expression.insert(open_i, num)
    
print(f'Part 2: {total2}') # 20394514442037
