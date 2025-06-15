import unittest
import pytest 
from simple_calculator import SimpleCalculator

class TestAdd(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(2,3), -1)
        self.assertEqual(self.calc.subtract(3,2), 1)
        self.assertEqual(self.calc.subtract(-2,-3), -5)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(2,3), 6)
        self.assertEqual(self.calc.multiply(-2,-3), 6)
        self.assertEqual(self.calc.multiply(-2,3), -6)
        self.assertEqual(self.calc.multiply(-2,0), 0)
        self.assertEqual(self.calc.multiply(-2,1), -2)

    def test_division(self):
        self.assertEqual(self.calc.divide(4,24), 6)
        self.assertIsNone(self.calc.divide(-2, 0))

