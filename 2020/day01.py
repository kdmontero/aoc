with open('day01.txt') as given:
    expenses = [int(expense) for expense in given.read().split('\n')]

# PART 1
for i, num1 in enumerate(expenses):
    for num2 in expenses[i+1:]:
        if num1 + num2  == 2020:    
            print(num1*num2) # 468051
            break
    else:
        continue
    break


# PART 2
for i, num1 in enumerate(expenses):
    for j, num2 in enumerate(expenses[i+1:]):
        for num3 in expenses[j+1:]:
            if num1 + num2 + num3 == 2020:    
                print(num1*num2*num3) # 272611658
                break
        else:
            continue
        break
    else:
        continue
    break