import unittest

from pe import integer

class TestPalindromic(unittest.TestCase):

    def test_palindromic(self):
        self.assertTrue(integer.palindromic(110011))
        self.assertTrue(integer.palindromic(98230403289))
        self.assertTrue(integer.palindromic(1))
        self.assertFalse(integer.palindromic(10))
