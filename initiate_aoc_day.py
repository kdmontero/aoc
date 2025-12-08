import os
import re
import sys
import time

from requests import HTTPError
from requests import request


def initiate_script(year: int, day: int, session_cookie: str) -> None:

    # get the title of the puzzle
    url = f'https://adventofcode.com/{year}/day/{int(day)}'
    headers = {
        'Cookie': session_cookie,
        'User-Agent': 'kevindmontero@gmail.com'
    }

    for _ in range(5):
        try:
            response = request('GET', url, headers=headers)
            response.raise_for_status()
        except HTTPError as e:
            print(f'{response.text}')
            time.sleep(1)
        else:
            break
    else:
        exit('timed out after 5 failed attempts')

    pattern = re.compile(r'Day [\d]+: (.+) ---')
    title = pattern.findall(response.text)[0]

    if day == '25':
        part2_text = f'Complete all 49 stars in Advent of Code {year}'
    else:
        part2_text = '{0}'

    # generate the template code
    code = (
        "if __name__ == '__main__':\n"
        f'    print("Advent of Code {year} - Day {day}: {title}")\n\n'
        f"    with open('day{day}.txt') as f:\n"
        "        pass\n\n\n"
        "    # part 1\n\n"
        "    print(f'Part 1: {0}') #\n\n\n"
        "    # part 2\n\n"
        f"    print(f'Part 2: {part2_text}') #\n\n"
    )

    with open(f'day{day}.py', 'w') as f:
        f.write(code)

    return

def download_input(session_cookie):

    url = f'https://adventofcode.com/{year}/day/{int(day)}/input'
    headers = {
        'Cookie': session_cookie,
        'User-Agent': 'kevindmontero@gmail.com'
    }


    for _ in range(5):
        try:
            response = request('GET', url, headers=headers)
            response.raise_for_status()
        except HTTPError as e:
            print(f'Not ready yet: {e}')
            time.sleep(1)
        else:
            break
    else:
        exit('timed out after 5 failed attempts')


    with open(f'day{day}.txt', 'w') as f:
        f.write(response.text.strip())

    return


if __name__ == '__main__':

    env_dir = os.path.dirname(os.path.abspath(__file__))
    env_path = os.path.join(env_dir, '.env')

    with open(env_path) as f:
        session_cookie = f.read().strip()


    # ERROR HANDLERS

    if len(sys.argv) < 2:
        exit('Error: Input day XX')

    year = os.getcwd()[-4:]
    day = sys.argv[1]

    if len(day) != 2:
        exit('Error: Input day XX')

    if os.name == 'posix':
        if not os.getcwd().endswith(f'Github/aoc/{year}'):
            exit(f'Error: Invalid AOC directory')
    elif os.name == 'nt':
        if not os.getcwd().endswith(f'aoc\\{year}'):
            exit(f'Error: Invalid AOC directory')

    if (int(year) < 2015) or (int(year) > 2100):
        exit('Error: Invalid year')

    if 2015 <= int(year) <= 2024:
        if (int(day) < 1) or (int(day) > 25):
            exit('Error: Invalid day')
    else:
        if (int(day) < 1) or (int(day) > 12):
            exit('Error: Invalid day. Starting 2025, AOC only has 12 days')




    # INITIATE PYTHON SCRIPT

    if f'day{day}.py' in os.listdir():
        print(f'Day {day} script is already initiated')
    else:
        initiate_script(year, day, session_cookie)
        print(f'Day {day} script initiated successfully')



    # DOWNLOAD INPUT

    if f'day{day}.txt' in os.listdir():
        print(f'Day {day} input is already downloaded')
    else:
        download_input(session_cookie)
        print(f'Day {day} input downloaded successfully')

