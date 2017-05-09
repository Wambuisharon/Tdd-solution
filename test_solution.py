import unittest
from tdd import solution
class TestSolution(unittest.TestCase):
	def test_addition(self):
		self.assertTrue(solution(1,5, "+"), 6)
    def test_subtraction(self):
		self.assertTrue(solution(23,5, "-"), 18)
    def test_multiplication(self):
		self.assertTrue(solution(3,0, "*"), 0)
	def test_division(self):
		self.assertTrue(solution(30,2, "/"), 15)
	def modulus(self):
	    self.assertTrue(solution(7,2, "%"), 1)	

if __name__== "__main__":
	unittest.main()