import sys
import os
import subprocess

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


if len(sys.argv) < 3:
    print('Error: Input year (20XX) and day (XX)')
    exit()

year = sys.argv[1]
day = sys.argv[2]

if (int(year) < 2015) or (int(year) > 2100):
    print('Error: Invalid year')
    exit()

if (int(day) < 1) or (int(day) > 25):
    print('Error: Invalid day')
    exit()


AOC_WEBSITE = f'https://adventofcode.com/{year}/day/{int(day)}/input'
CHROMEDRIVER_LOC = '/home/kevin/Downloads/chromedriver'

if not os.getcwd().endswith(f'Github/aoc/{year}'):
    print(f'Error: wrong AOC directory, you are not in {year}')
    exit()

if f'dayday{day}.py' in os.listdir():
    print(f'Error: Day {day} is already initiated')
    exit()


# GET INPUT
options = Options()
options.add_experimental_option("excludeSwitches", ['enable-automation'])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument("user-data-dir=/home/kevin/.config/google-chrome/")
#options.add_argument("profile-directory=Profile1")
options.headless = True


service = Service(executable_path=CHROMEDRIVER_LOC)
driver = webdriver.Chrome(service=service, options=options)
driver.implicitly_wait(10)
driver.get(AOC_WEBSITE)

given_input = driver.find_element('tag name', 'pre')
print(given_input.text)

'''
#subprocess.call(f'echo "{given_input.text}" >> dayday{day}.txt', shell=True)
'''

# INITIATE PYTHON SCRIPT
code = (
    f"if __name__ == '__main__':\n"
    f"    print('Advent of Code {year} - Day {day}')\n\n"
    f"    with open('day{day}.txt') as f:\n"
    f"        pass\n\n\n"
    "print(f'Part 1: {}') #\n\n\n"
    "print(f'Part 2: {}') #"
)

#subprocess.call(f'echo "{code}" >> dayday{day}.py', shell=True)


print(f'Day {day} initiated successfully')
driver.quit()
