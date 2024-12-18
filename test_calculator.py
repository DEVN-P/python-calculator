import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    # Add the following test methods to the TestCalculator class:
    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(4, 2), 6)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(1, 2), -1)
        self.assertEqual(self.calc.subtract(4, 2), 2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(0, 2), 0)
        self.assertEqual(self.calc.multiply(4, -2), -8)
        self.assertEqual(self.calc.multiply(4, 2), 8)
        self.assertEqual(self.calc.multiply(-1, -2), 2)
        self.assertEqual(self.calc.multiply(4, 0), 0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(0, 3), 0)
        self.assertEqual(self.calc.divide(4, 2), 2)
        self.assertEqual(self.calc.divide(9, -3), -3)
        self.assertEqual(self.calc.divide(-4, 2), -2)
        self.assertEqual(self.calc.divide(-4, -2), 2)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(4, 2), 0)
        self.assertEqual(self.calc.modulo(1, 2), 1)

if __name__ == '__main__':
    unittest.main()