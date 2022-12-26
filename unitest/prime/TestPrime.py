import unittest

from prime_number import is_prime

class TestPrime(unittest.TestCase):
    def test_two(self):
        self.assertTrue(is_prime(2))

    def test_five(self):
        self.assertTrue(is_prime(5))

    def test_nine(self):
        self.assertFalse(is_prime(9))

    def test_eleven(self):
        self.assertTrue(is_prime(11))

    #or as below

    def test_prime_not_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(5))
        self.assertFalse(is_prime(9))
        self.assertTrue(is_prime(11))

    def test_typeerror_1(self):
        with self.assertRaises(TypeError):
            is_prime(1.5)

    def test_typeerror_2(self):
        with self.assertRaises(TypeError):
            is_prime("one")

    def test_valueerror(self):
        with self.assertRaises(ValueError):
            is_prime(-4)

if __name__=='__main__':
    unittest.main()