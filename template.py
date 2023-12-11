import sys

from utils import get_input


TEST_1 = """

"""


TEST_2 = """

"""


def main() -> int:
    part_1(TEST_1[1:])
    # part_1(get_input(".txt"))

    # part_2(TEST_2[1:])
    # part_2(get_input(".txt"))

    return 0


def part_1(raw_input: str) -> None:
    lines = raw_input.splitlines()


def part_2(raw_input: str) -> None:
    lines = raw_input.splitlines()


if __name__ == "__main__":
    sys.exit(main())
