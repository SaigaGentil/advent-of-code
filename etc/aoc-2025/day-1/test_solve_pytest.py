"""Tests for day 1 solver (count_zero_points)."""

from pathlib import Path
import pytest
from solve import count_zero_points


@pytest.mark.parametrize(
    "lines,expected",
    [
        (
            [
                "L68",
                "L30",
                "R48",
                "L5",
                "R60",
                "L55",
                "L1",
                "L99",
                "R14",
                "L82",
            ],
            3,
        ),
        (["L1", "", "R1", "\n", "L0"], count_zero_points(
            [l for l in ["L1", "", "R1", "\n", "L0"] if l.strip()])),
    ],
)
def test_examples(lines, expected):
    assert count_zero_points(lines) == expected


def test_input_file_sanity():
    path = Path(__file__).with_name("input.txt")
    assert path.exists()
    lines = path.read_text(encoding="utf-8").splitlines()
    result = count_zero_points(lines)
    assert isinstance(result, int)
    assert 0 <= result <= len(lines)


def test_invalid_direction_raises():
    with pytest.raises(ValueError):
        count_zero_points(["X1"])
