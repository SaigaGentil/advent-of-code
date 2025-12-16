"""Advent of Code 2025 Day 1 - Secret Entrance

Usage:
    python solve.py [input_file]

If no input_file is provided, it uses `input.txt` in the same directory.
"""

from pathlib import Path
import sys


def count_zero_points(lines, start=50, modulo=100):
    pos = start
    zeros = 0
    for raw in lines:
        line = raw.strip()
        if not line:
            continue
        dir_ = line[0]
        dist = int(line[1:])
        if dir_ == 'L':
            pos = (pos - dist) % modulo
        elif dir_ == 'R':
            pos = (pos + dist) % modulo
        else:
            raise ValueError(f"Unknown direction: {dir_}")
        if pos == 0:
            zeros += 1
    return (f"The password is {zeros}")


def main(argv=None):
    argv = argv or sys.argv[1:]
    if argv:
        path = Path(argv[0])
    else:
        path = Path(__file__).with_name('input.txt')
    if not path.exists():
        print(f"Input file not found: {path}")
        return 2
    with path.open('r', encoding='utf-8') as f:
        lines = f.readlines()
    result = count_zero_points(lines)
    print(result)
    return 0


# Not needed for now, moved to a separate test file
# def _test_example():
#     example = [
#         'L68',
#         'L30',
#         'R48',
#         'L5',
#         'R60',
#         'L55',
#         'L1',
#         'L99',
#         'R14',
#         'L82',
#     ]
#     assert count_zero_points(example) == 3


if __name__ == '__main__':
    # _test_example()
    raise SystemExit(main())
