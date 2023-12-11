import sys
from collections import defaultdict

from utils import get_input


TEST_1 = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""


def main() -> int:
    # part_1(TEST_1[1:])
    part_1(get_input("3.txt"))

    # part_2(TEST_1[1:])
    part_2(get_input("3.txt"))

    return 0


def part_1(raw_input: str) -> None:
    lines = raw_input.splitlines()
    value = 0
    num_rows = len(lines)
    num_cols = len(lines[0])
    numbers = defaultdict(list)

    for j, line in enumerate(lines):
        i = 0
        start = None
        while True:
            if line[i] in "0123456789":
                if start is None:
                    start = i
            else:
                if start is not None:
                    numbers[j].append((start, i))
                    start = None
            i += 1
            if i == len(line):
                if start is not None:
                    numbers[j].append((start, i))
                    start = None
                break

    for j, index_list in numbers.items():
        for start, end in index_list:
            adjacent = False
            num = ""
            for i in range(start, end):
                num += lines[j][i]
            for row in (j-1, j, j+1):
                for col in range(start-1, end+1):
                    if col < 0 or col >= num_cols or row < 0 or row >= num_rows:
                        continue
                    c = lines[row][col]
                    if c not in ".0123456789":
                        adjacent = True
            if adjacent:
                value += int(num)

    print(value)


def part_2(raw_input: str) -> None:
    lines = raw_input.splitlines()
    value = 0
    num_rows = len(lines)
    num_cols = len(lines[0])
    numbers = defaultdict(list)
    gears = defaultdict(list)

    for j, line in enumerate(lines):
        i = 0
        start = None
        while True:
            if line[i] in "0123456789":
                if start is None:
                    start = i
            else:
                if start is not None:
                    numbers[j].append((start, i))
                    start = None
            i += 1
            if i == len(line):
                if start is not None:
                    numbers[j].append((start, i))
                    start = None
                break

    for j, index_list in numbers.items():
        for start, end in index_list:
            adjacent_gears = set()
            num = ""
            for i in range(start, end):
                num += lines[j][i]
            for row in (j - 1, j, j + 1):
                for col in range(start - 1, end + 1):
                    if col < 0 or col >= num_cols or row < 0 or row >= num_rows:
                        continue
                    c = lines[row][col]
                    if c == "*":
                        adjacent_gears.add((col, row))
            for x, y in adjacent_gears:
                gears[(x, y)].append(int(num))

    for position, neighbors in gears.items():
        if len(neighbors) == 2:
            value += neighbors[0] * neighbors[1]

    print(value)


if __name__ == "__main__":
    sys.exit(main())
