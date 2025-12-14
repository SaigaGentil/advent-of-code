import unittest
from pathlib import Path

from solve import count_zero_points


class TestSolve(unittest.TestCase):
    def test_example(self):
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
        self.assertEqual(count_zero_points(example), 3)

    def test_input_file(self):
        path = Path(__file__).with_name('input.txt')
        self.assertTrue(path.exists(), "input.txt must exist for this test")
        lines = path.read_text(encoding='utf-8').splitlines()
        self.assertEqual(count_zero_points(lines), 1034)


if __name__ == '__main__':
    unittest.main()
