#!/usr/bin/python3
"""this is test"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """this is test"""
    def test_max_at_the_end(self):
        """this is test"""
        self.assertEqual(max_integer([5,1,3,4]), 5)

    def test_one_negative_number(self):
        """this is test"""
        self.assertEqual(max_integer([2,-2, 7, 5]), 7)

    def test_only_negative(self):
        """this is test"""
        self.assertEqual(max_integer([-1,-2,-3]), -1)

    def test_Zero(self):
        """this is test"""
        self.assertEqual(max_integer([]), None)

    def test_postive_and_negative(self):
        """this is test"""
        self.assertEqual(max_integer([10,-30,5,-1,50]), 50)

    def test_max_in_the_middle(self):
        """this is test"""
        self.assertEqual(max_integer([1,2,14,2,1]), 14)

    def test_max_at_the_begining(self):
        """this is test"""
        self.assertEqual(max_integer([14,1,2,1,2]), 14)

    def test_max_all_equal(self):
        """this is test"""
        self.assertEqual(max_integer([10,10,10]), 10)

    def test_list_with_one_element(self):
        """this is test"""
        self.assertEqual(max_integer([10]), 10)

if __name__ == '__main__':
    unittest.main()
