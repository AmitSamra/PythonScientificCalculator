import unittest
import PyCalc0327

class TestCalc(unittest.TestCase):

	def test_PyCalc0327(self):
		self.assertEqual(Calculator.add(2,3),5)

	def test_PyCalc0327_(self):
		self.assertEqual(Calculator.subtract(5,3),2)

	def test_PyCalc0327_multiply(self):
		self.assertEqual(Calculator.multiply(2,5),10)

	def test_PyCalc0327_divide(self):
		self.assertEqual(Calculator.divide(10,2),5)

	def test_PyCalc0327(self):
		self.assertEqual(Calculator.square(2,4),16)




if __name__ == '__main__':
	unittest.main()

