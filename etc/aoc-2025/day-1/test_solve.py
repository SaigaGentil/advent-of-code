from pathlib import Path

from solve import count_zero_points


def test_example():
    example = [
        'L68',
        'L30',
        'R48',
        'L5',
        'R60',
        'L55',
        'L1',
        'L99',
        'R14',
        'L82',
    ]
    assert count_zero_points(example) == 3


def test_input_file():
    path = Path(__file__).with_name('input.txt')
    assert path.exists(), "input.txt must exist for this test"
    lines = path.read_text(encoding='utf-8').splitlines()
    assert count_zero_points(lines) == 1034
