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


def test_input_file_sanity():
    path = Path(__file__).with_name('input.txt')
    assert path.exists()
    lines = path.read_text(encoding='utf-8').splitlines()
    result = count_zero_points(lines)
    assert isinstance(result, int)
    assert 0 <= result <= len(lines)


def test_blank_lines_ignored():
    lines = ['L1', '', 'R1', '\n', 'L0']
    # same as ['L1', 'R1', 'L0']
    assert count_zero_points(lines) == count_zero_points(
        [l for l in lines if l.strip()])
