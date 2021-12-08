from collections import Counter

if __name__ == '__main__':
    print('Advent of Code 2021 - Day 03')

    with open('day03.txt') as f:
        report = f.read().splitlines()

    # part 1

    counters = []
    for digits in zip(*report):
        counters.append(Counter(digits))

    gamma = ''.join(max(counter, key=counter.get) for counter in counters)
    epsilon = ''.join('1' if i == '0' else '0' for i in gamma)

    print(f'Part 1: {int(gamma, 2) * int(epsilon, 2)}') # 3633500

    
    # part 2

    oxygen = report[:]
    CO2 = report[:]
    for i in range(len(report[0])):
        counter_oxy = Counter(num[i] for num in oxygen)
        if counter_oxy['0'] == counter_oxy['1']:
            oxy_digit = '1'
        else:
            oxy_digit = max(counter_oxy, key=counter_oxy.get)
        oxygen = [num for num in oxygen if num[i] == oxy_digit]

        counter_co2 = Counter(num[i] for num in CO2)
        if counter_co2['0'] == counter_co2['1']:
            co2_digit = '0'
        else:
            co2_digit = min(counter_co2, key=counter_co2.get)
        CO2 = [num for num in CO2 if num[i] == co2_digit]

    OGR = int(*oxygen, 2) # Oxygen Generator Rating
    CSR = int(*CO2, 2) # CO2 Scrubber Rating

    print(f'Part 2: {OGR * CSR}') # 4550283
