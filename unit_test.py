
import unittest
def addition(x, y):
    return x + y


def subtraction(x, y):
    return x - y


def multiplication(x, y):
    return x * y


def division(x, y):
    return x / y
class TestCalc(unittest.TestCase):
 def test_addition(self):
    self.assertEqual(addition(5, 5), 10)
    self.assertEqual(addition(-3, 3), 0)
    self.assertEqual(addition(-5,-5),-10)
 def test_subtraction(self):
    self.assertEqual(subtraction(15, 5), 10)
    self.assertEqual(subtraction(-1, 2),-3)
    self.assertEqual(subtraction(-1,-1), 0)
 def test_multiplication(self):
    self.assertEqual(multiplication(20, 5), 10)
    self.assertEqual(multiplication(-2, 1),-2)
    self.assertEqual(multiplication(-1,-3), 3)
 def test_division(self):
    self.assertEqual(division(0, 1), 1)
    self.assertEqual(division(-1, 1),-1)
    self.assertEqual(division(-2,-2), 1)
    self.assertEqual(division(6, 3), 2)
 def test_modulus(self):
      self.assertEqual(division(0, 1), 1)
      self.assertEqual(division(-1, 1), -1)
      self.assertEqual(division(-2, -2), 1)
      self.assertEqual(division(6, 3), 2)

if __name__ == '__main__':
   unittest.main()

