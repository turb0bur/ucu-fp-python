import unittest

from Essentials.PrimeCheck.task import is_prime


class TestCase(unittest.TestCase):
    def test_ensures_numbers_are_prime(self):
        for num in [3, 7, 11, 773, 507961]:
            self.assertTrue(is_prime(num), msg=f"Expected ${num} to be prime")

    def test_ensures_nums_are_not_prime(self):
        for num in [15, 507962]:
            self.assertFalse(is_prime(num), msg=f"Expected ${num} not to be prime")

    def test_ensures_any_pow_of_2_is_no_prime(self):
        for num in range(2, 64, 2):
            value = pow(2, num)
            self.assertFalse(is_prime(value), msg=f"Expected ${value} not to be prime")

    def test_ensures_negative_numbers_are_not_prime(self):
        for num in [-1, -2, -3, -10]:
            self.assertFalse(is_prime(num), msg=f"Expected {num} not to be prime")

    def test_edge_cases(self):
        self.assertFalse(is_prime(0), msg="Expected 0 not to be prime")
        self.assertFalse(is_prime(1), msg="Expected 1 not to be prime")
        self.assertTrue(is_prime(2), msg="Expected 2 to be prime")
        self.assertTrue(is_prime(3), msg="Expected 3 to be prime")

    def test_ensures_divisible_by_i_or_i_plus_2_are_not_prime(self):
        for num in [25, 49, 77, 121]:  # 25 = 5*5, 49 = 7*7, 77 = 7*11, 121 = 11*11
            self.assertFalse(is_prime(num), msg=f"Expected {num} not to be prime")