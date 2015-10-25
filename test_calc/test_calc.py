import calc
import unittest

class TestCalc(unittest.TestCase):
	def setUp(self):
		self.a = 10
		self.b = 5
		
	def test_calc_add(self):
		result = calc.add(self.a, self.b)
		self.assertEqual(result, self.a + self.b)
	
	def test_calc_divide(self):
		result = calc.divide(self.a, self.b)
		self.assertEqual(result, self.a / self.b)
		
	def test_calc_mult(self):
		result = calc.mult(self.a, self.b)
		self.assertEqual(result, self.a * self.b)
		
if __name__ == '__main__':
	unittest.main()
