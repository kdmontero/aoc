print("Advent of Code 2016 - Day 09: Explosives in Cyberspace")
with open('day09.txt') as file:
    f = file.read().strip()

# part 1
d_length1 = 0
i = 0
inside_marker = False
while i < len(f):
    if not inside_marker:
        if f[i] == '(':
            inside_marker = True
            marker = ''
        else:
            d_length1 += 1
    else:
        if f[i] == ')':
            substring, repeat = [int(x) for x in marker.split('x')]
            inside_marker = False
            d_length1 += substring * repeat
            i += substring + 1
            continue
        else:
            marker += f[i]
    i += 1 

print(f'Part 1: {d_length1}') # 112830


# part 2
def d_length(string, multiply):
    if '(' not in string:
        return len(string) * multiply
    else:
        i = 0
        inside_marker = False
        length = 0
        while i < len(string):
            if not inside_marker:
                if string[i] == '(':
                    inside_marker = True
                    marker = ''
                else:
                    length += 1
            
            else:
                if string[i] == ')':
                    substring, repeat = [int(x) for x in marker.split('x')]
                    inside_marker = False
                    length += d_length(string[i+1:i+1+substring], repeat)
                    i += substring + 1
                    continue
                else:
                    marker += string[i]
            i += 1 

        return length * multiply 

print(f'Part 2: {d_length(f, 1)}') # 10931789799
