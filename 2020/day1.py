expenses = []
with open('day1.txt') as given:
    for line in given.readlines():
        expenses.append(int(line.rstrip('\n')))


# PART 1
for i, num1 in enumerate(expenses):
    for j, num2 in enumerate(expenses[i+1:]):
        if num1 + num2  == 2020:    
            print(num1*num2)
            break
    else:
        continue
    break


# PART 2
for i, num1 in enumerate(expenses):
    for j, num2 in enumerate(expenses[i+1:]):
        for k, num3 in enumerate(expenses[j+1:]):
            if num1 + num2 + num3 == 2020:    
                print(num1*num2*num3)
                break
        else:
            continue
        break
    else:
        continue
    break