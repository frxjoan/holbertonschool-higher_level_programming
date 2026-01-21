#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_sortedlist(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unsortedlist(self):
        self.assertEqual(max_integer([4, 1, 3, 2]), 4)

    def test_emptylist(self):
        self.assertEqual(max_integer([]), None)

    def test_one_element(self):
        self.assertEqual(max_integer([6]), 6)

    def test_negative_number(self):
        self.assertEqual(max_integer([-6, -12, -5, -2]), -2)

    def test_same_number(self):
        self.assertEqual(max_integer([5, 5, 5]), 5)
