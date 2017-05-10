import unittest
from tdd import solution
class TestSolution(unittest.TestCase):
    def test_addition(self):
        self.assertTrue(solution(1,5, "+"), 6)
    def test_subtraction(self):
        self.assertTrue(solution(23,5, "-"), 18)
    def test_multiplication(self):
        self.assertTrue(solution(3,2, "*"), 6)
    def test_division(self):
        self.assertTrue(solution(30,2, "/"), 15)
    def modulus(self):
        self.assertTrue(solution(7,2, "%"), 1)  
    def power(self):
        self.assertTrue(solution(2,2, "**"), 4) 
    def floor_division(self):
        self.assertTrue(solution(7,2, "//"), 3)  
    def greater(self):
        self.assertTrue(solution(7,2, ">"), 7)
    def not_equal(self):
        self.assertTrue(solution(7,2, "!="), True)
    def same(self):
        self.assertTrue(solution(7,2, "=="), False)  
                     
                      
                

if __name__== "__main__":
    unittest.main()