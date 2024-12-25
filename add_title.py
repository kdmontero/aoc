import os
import re
import sys
import time

from requests import HTTPError
from requests import request


def get_title(year: int, day: int, session_cookie: str) -> str:

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
    return pattern.findall(response.text)[0]


if __name__ == '__main__':

    env_dir = os.path.dirname(os.path.abspath(__file__))
    env_path = os.path.join(env_dir, '.env')

    with open(env_path) as f:
        session_cookie = f.read().strip()

    for year in range(2015, 2025):
        for day in range(1, 26):
            day_title = get_title(year, day, session_cookie)

            day = str(day).rjust(2, '0')
            file_path = os.path.join(env_dir, f'{year}/day{day}.py')

            check_title = f'print("Advent of Code {year} - Day {day}: '
            old_title = f"print('Advent of Code {year} - Day {day}')"
            new_title = f'print("Advent of Code {year} - Day {day}: {day_title}")'

            if (os.path.isfile(file_path)):
                with open(file_path, 'r') as f:
                    file_text = f.read()
                if check_title in file_text:
                    print(f'{year} Day {day}: No need to add title')
                    continue
                with open(file_path, 'w') as f:
                    f.write(file_text.replace(old_title, new_title))
                    print(new_title)

