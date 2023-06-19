#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest

max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """
    tests methods for max_integer
    """

    def test_orderedList(self):
        """
        max integer at the end of list
        """
        self.assertEqual(max_integer([1, 2, 3, 5]), 5)

    def test_unorderedList(self):
        """
        max integer in average case
        """
        self.assertEqual(max_integer([3, 2, 5, 1, 4]), 5)

    def test_reverseOrderList(self):
        """
        max integer at start of list
        """
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)

    def test_posAndNegList(self):
        """
        list of positives and negatives
        """
        self.assertEqual(max_integer([-3, 2, 5, -99]), 5)

    def test_negativeList(self):
        """
        list of negatives
        """
        self.assertEqual(max_integer([-909, -22, -3]), -3)

    def test_typeError(self):
        """
        tests error case
        """
        with self.assertRaises(TypeError):
            max_integer(["e", 3, 5])

    def test_NoList(self):
        """
        tests with no list
        """
        self.assertEqual(max_integer([]), None)

    def test_LonelyNumber(self):
        """
        tests with a lone number
        """
        self.assertEqual(max_integer([17]), 17)


if __name__ == "__main__":
    unittest.main()
