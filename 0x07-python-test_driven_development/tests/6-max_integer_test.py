#!/usr/bin/python3
"""unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """define unittests"""

    def test_empty_list(self):
        """tests for an empty list"""
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        """tests for a list with a single element"""
        self.assertEqual(max_integer([5]), 5)

    def test_multiple_elements(self):
        """tests for a list with multiple elements"""
        self.assertEqual(max_integer([1, 4, 2, 8]), 8)

    def test_negative_numbers(self):
        """tests for a list with negative numbers"""
        self.assertEqual(max_integer([-2, 1, -5]), 1)

    def test_max_at_beginning(self):
        """tests a list with a beginning max value"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_all_same_elements(self):
        """tests for a list with all elements the same"""
        self.assertEqual(max_integer([3, 3, 3]), 3)

    def test_none_value(self):
        """tests for passing None instead of a list"""
        self.assertRaises(TypeError, max_integer, None)


if __name__ == '__main__':
    unittest.main()
