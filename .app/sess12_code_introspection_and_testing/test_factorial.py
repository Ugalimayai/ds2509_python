# Python script to demonstrate unit testing of the factorial () function

# import required modules

import unittest
from factorial import factorial

class TestFactorial(unittest.TestCase):
    def test_factorial_zero(self):
        self.assertEqual(factorial(0), 1)
    def test_factorial_positive(self):
        self.assertEqual(factorial(5), 120)
    def test_factorial_negative(self):
        with self.assertRaises(ValueError) as ve:
            factorial(-7)
        self.assertEqual(str(ve.exception), 'Factorial of negative numbers is not defined!')

# Run the tests
if __name__ == '__main__':
    unittest.main()

