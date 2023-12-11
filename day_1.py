import sys
import re

from utils import get_input


TEST_1 = """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""


TEST_2 = """
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""


def main() -> int:
    # part_1(TEST_1[1:])
    part_1(get_input("1.txt"))

    # part_2(TEST_2[1:])
    part_2(get_input("1.txt"))

    return 0


def part_1(raw_input: str) -> None:
    lines = raw_input.splitlines()
    total = 0
    for line in lines:
        matches = re.findall(r'\d', line)
        first = matches[0]
        last = matches[-1]
        value = int(f"{first}{last}")
        total += value
    print(total)


def part_2(raw_input: str) -> None:
    lines = raw_input.splitlines()
    total = 0
    number_map = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    for line in lines:
        matches = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)
        first = matches[0]
        first = number_map.get(first, first)
        last = matches[-1]
        last = number_map.get(last, last)
        value = int(f"{first}{last}")
        total += value
    print(total)


if __name__ == "__main__":
    sys.exit(main())
