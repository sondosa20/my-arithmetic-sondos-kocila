import unittest
from src.my_arithmetic_sondos_kocila.pgcd import gcd

# FILE: my-arithmetic-sondos-kocila/tests/test_pgcd_tests.py

class TestGCD(unittest.TestCase):
    def test_gcd_positive_numbers(self):
        self.assertEqual(gcd(48, 18), 6)
        self.assertEqual(gcd(56, 98), 14)

    def test_gcd_with_zero(self):
        self.assertEqual(gcd(0, 5), 5)
        self.assertEqual(gcd(5, 0), 5)
        self.assertEqual(gcd(0, 0), 0)

    def test_gcd_negative_numbers(self):
        self.assertEqual(gcd(-48, 18), 6)
        self.assertEqual(gcd(48, -18), 6)
        self.assertEqual(gcd(-48, -18), 6)

    def test_gcd_same_numbers(self):
        self.assertEqual(gcd(7, 7), 7)
        self.assertEqual(gcd(-7, -7), 7)
