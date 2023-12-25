import sys
import os
import subprocess


# ERROR HANDLERS

if len(sys.argv) < 2:
    print('Error: Input day XX')
    exit()

year = os.getcwd()[-4:]
day = sys.argv[1]

if len(day) != 2:
    print('Error: Input day XX')
    exit()

if os.name == 'posix':
    if not os.getcwd().endswith(f'Github/aoc/{year}'):
        print(f'Error: Invalid AOC directory')
        exit()
elif os.name == 'nt':
    if not os.getcwd().endswith(f'aoc\\{year}'):
        print(f'Error: Invalid AOC directory')
        exit()

if (int(year) < 2015) or (int(year) > 2100):
    print('Error: Invalid year')
    exit()

if (int(day) < 1) or (int(day) > 25):
    print('Error: Invalid day')
    exit()

if f'day{day}.py' in os.listdir():
    print(f'Error: Day {day} script is already initiated')
    exit()

if f'day{day}.txt' in os.listdir():
    print(f'Error: Day {day} input is already downloaded')
    exit()


# INITIATE PYTHON SCRIPT

code = (
    "if __name__ == '__main__':\n"
    f"    print('Advent of Code {year} - Day {day}')\n\n"
    f"    with open('day{day}.txt') as f:\n"
    "        pass\n\n\n"
    "    print(f'Part 1: {0}') #\n\n\n"
    "    print(f'Part 2: {0}') #"
)

subprocess.call(f"touch day{day}.py", shell=True)
subprocess.call(f"touch day{day}.txt", shell=True)
with open(f'day{day}.py', 'w') as f:
    f.write(code)


print(f'Day {day} initiated successfully')
