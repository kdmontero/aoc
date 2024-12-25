print("Advent of Code 2020 - Day 01: Report Repair")
with open('day01.txt') as given:
    expenses = [int(expense) for expense in given.read().split('\n')]

# part 1
for i, num1 in enumerate(expenses):
    for num2 in expenses[i+1:]:
        if num1 + num2  == 2020:    
            ans1 = num1 * num2
            break
    else:
        continue
    break

print(f'Part 1: {ans1}') # 468051


# part 2
for i, num1 in enumerate(expenses):
    for j, num2 in enumerate(expenses[i+1:]):
        for num3 in expenses[j+1:]:
            if num1 + num2 + num3 == 2020:    
                ans2 = num1 * num2 * num3
                break
        else:
            continue
        break
    else:
        continue
    break

print(f'Part 2: {ans2}') # 272611658
