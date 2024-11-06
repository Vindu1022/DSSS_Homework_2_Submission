#Add unit tests
import unittest
from math_quiz import Randomfunction_M, Randomfunction_N, Randomfunction_O
class TestMathQuizFunctions(unittest.TestCase):
    
    def test_Randomfunction_M(self):
        min_value, max_value = 1, 10
        for _ in range(100):
            result = Randomfunction_M(min_value, max_value)
            self.assertTrue(min_value <= result <= max_value, 
                            f"Result {result} is not within the range {min_value}-{max_value}")
    
    def test_Randomfunction_N(self): 
        valid_operators = ['+', '-', '*']
        for _ in range(100):  
            operator = Randomfunction_N()
            self.assertIn(operator, valid_operators, 
                          f"Operator {operator} is not in the expected operators {valid_operators}")
    
    def test_Randomfunction_O(self)
        test_cases = [
            (5, 3, '+', 8),
            (10, 4, '-', 6),
            (7, 6, '*', 42)
        ]
        
        for operand1, operand2, operator, expected_answer in test_cases:
            question, answer = Randomfunction_O(operand1, operand2, operator)
            self.assertEqual(answer, expected_answer, 
                             f"For question '{question}', expected answer {expected_answer} but got {answer}")

if _name_ == "_main_":
    unittest.main()
