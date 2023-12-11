import sys

from utils import get_input


TEST_1 = """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""


def main() -> int:
    # part_1(TEST_1[1:])
    part_1(get_input("2.txt"))

    # part_2(TEST_1[1:])
    part_2(get_input("2.txt"))

    return 0


def part_1(raw_input: str) -> None:
    lines = raw_input.splitlines()
    value = 0
    for i, line in enumerate(lines, start=1):
        cubes = {'red': 0, 'green': 0, 'blue': 0}
        sets = line.split(': ')[1].split('; ')
        for s in sets:
            for draw in s.split(', '):
                number = int(draw.split(' ')[0])
                color = draw.split(' ')[1]
                cubes[color] = max(cubes[color], number)
        if cubes['red'] <= 12 and cubes['green'] <= 13 and cubes['blue'] <= 14:
            value += i
    print(value)


def part_2(raw_input: str) -> None:
    lines = raw_input.splitlines()
    value = 0
    for i, line in enumerate(lines, start=1):
        cubes = {'red': 0, 'green': 0, 'blue': 0}
        sets = line.split(': ')[1].split('; ')
        for s in sets:
            for draw in s.split(', '):
                number = int(draw.split(' ')[0])
                color = draw.split(' ')[1]
                cubes[color] = max(cubes[color], number)
        power = cubes['red'] * cubes['green'] * cubes['blue']
        value += power
    print(value)


if __name__ == "__main__":
    sys.exit(main())
