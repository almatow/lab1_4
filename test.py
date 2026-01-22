import unittest
from lib import common_count


class TestCommonCount(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(common_count([1, 2, 3], [2, 3, 4], [0, 2, 9]), 1)  # общий: 2

    def test_multiple_common(self):
        self.assertEqual(common_count([1, 2, 3], [2, 3, 4], [2, 3]), 2)  # общие: 2 и 3

    def test_no_common(self):
        self.assertEqual(common_count([1], [2], [3]), 0)

    def test_empty_input(self):
        self.assertEqual(common_count(), 0)

    def test_duplicates_do_not_matter(self):
        self.assertEqual(common_count([2, 2, 2], [2], [2, 3, 2]), 1)


if __name__ == "__main__":
    unittest.main()
