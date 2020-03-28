import unittest
import PyCalc0327

class TestCalc(unittest.TestCase):

	calc = Calculator()

	def test_PyCalc0327(self):
		self.assertEqual(calc.add(2,3),5)

	def test_PyCalc0327_(self):
		self.assertEqual(calc.subtract(5,3),2)

	def test_PyCalc0327_multiply(self):
		self.assertEqual(calc.multiply(2,5),10)

	def test_PyCalc0327_divide(self):
		self.assertEqual(calc.divide(10,2),5)

	def test_PyCalc0327(self):
		self.assertEqual(calc.square(2,4),16)



if __name__ == '__main__':
	unittest.main()

