import collections
import itertools
import math

INPUT = 36000000

# part 1
def sum_factors1(num):
    total = num + 1
    for x in range(2, int(num**0.5) + 1):
        if num % x == 0:
            if x == num**0.5:
                total += x
            else:
                total += num//x + x
    return total

house1 = 1
while sum_factors1(house1)*10 < INPUT:
    house1 += 1

print(f'Part 1: {house1}') # 831600


# part 2
def get_prime_factors(num):
    prime_factors = []
    i = 2
    while i <= num:
        if num % i == 0:
            prime_factors.append(i)
            num = num // i
        else:
            i += 1
    return prime_factors

def sum_factors2(num):
    total = 0
    prime_factors = get_prime_factors(num)
    prime_factor_comb = set()

    for i in range(1, len(prime_factors) + 1):
        prime_factor_comb ^= set(itertools.combinations(prime_factors, i))
    
    for comb in prime_factor_comb:
        f = math.prod(comb)
        if f >= num//50:
            total += f
    
    return total

house2 = house1 # start with the part 1 ans for faster iteration
gifts = sum_factors2(house2)*11
while gifts < INPUT:
    house2 += 10 # every increase in max gifts occurs in multiples of 10
    gifts = sum_factors2(house2)*11

print(f'Part 2: {house2}') # 884520