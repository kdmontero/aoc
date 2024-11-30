import os
import sys
import time

from requests import HTTPError
from requests import request


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



# INITIATE PYTHON SCRIPT

def initiate_script():
    code = (
        "if __name__ == '__main__':\n"
        f"    print('Advent of Code {year} - Day {day}')\n\n"
        f"    with open('day{day}.txt') as f:\n"
        "        pass\n\n\n"
        "    print(f'Part 1: {0}') #\n\n\n"
        "    print(f'Part 2: {0}') #"
    )

    with open(f'day{day}.py', 'w') as f:
        f.write(code)


if f'day{day}.py' in os.listdir():
    print(f'Day {day} script is already initiated')
else:
    initiate_script()
    print(f'Day {day} script initiated successfully')



# DOWNLOAD INPUT

def download_input():
    env_dir = os.path.dirname(os.path.abspath(__file__))
    env_path = os.path.join(env_dir, '.env')

    with open(env_path) as f:
        session_cookie = f.read().strip()

    url = f'https://adventofcode.com/{year}/day/{int(day)}/input'
    headers = {
        'Cookie': session_cookie,
        'User-Agent': 'kevindmontero@gmail.com'
    }


    for _ in range(5):
        response = request('GET', url, headers=headers)

        try:
            response.raise_for_status()
        except HTTPError:
            raise HTTPError(response.text)
            time.sleep(1)
        else:
            break
    else:
        raise SystemExit('timed out after 5 failed attempts')


    with open(f'day{day}.txt', 'w') as f:
        f.write(response.text.strip())


if f'day{day}.txt' in os.listdir():
    print(f'Day {day} input is already downloaded')
else:
    download_input()
    print(f'Day {day} input downloaded successfully')

