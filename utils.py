from pathlib import Path

INPUT_FOLDER = Path(__file__).parent / "input"


def get_input(file: str) -> str:
    with open(INPUT_FOLDER / file) as fp:
        return fp.read()
