import unittest
import math
import io
import sys
from exercise import *

class TestFunctions(unittest.TestCase):
    def setUp(self):
        # Reset global score before each test
        global score
        score = 0
    
    def test_greet_user(self):
        """Test Exercise 1: Basic Function Definition"""
        # Since greet_user prints to stdout, we'd need to capture stdout
        # Redirect stdout to capture print output
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        greet_user()
        
        # Restore stdout
        sys.stdout = sys.__stdout__
        
        self.assertEqual(captured_output.getvalue().strip(), "Hello, World!")
  

    def test_personalized_greeting(self):
        """Test Exercise 2: Function Parameters and Type Hints"""
        # Test valid input
        self.assertEqual(personalized_greeting("Alice"), "Hello, Alice!")
        self.assertEqual(personalized_greeting("Bob"), "Hello, Bob!")
        self.assertIsInstance(personalized_greeting("Test"), str)
        
        # Test invalid input
        with self.assertRaises(TypeError):
            personalized_greeting(123)
        with self.assertRaises(TypeError):
            personalized_greeting(None)
  

    def test_calculate_rectangle_area(self):
        """Test Exercise 3: Multiple Parameters and Default Values"""
        # Test rectangle calculation
        self.assertEqual(calculate_rectangle_area(5, 3), 15)
        self.assertEqual(calculate_rectangle_area(2.5, 4), 10)
        self.assertEqual(calculate_rectangle_area(0, 5), 0)
        self.assertIsInstance(calculate_rectangle_area(1, 1), (int, float))
        
        # Test invalid inputs
        with self.assertRaises(ValueError):
            calculate_rectangle_area(-4.0, 5.0)
        with self.assertRaises(ValueError):
            calculate_rectangle_area(4.0, -5.0)
        with self.assertRaises(TypeError):
            calculate_rectangle_area("4", "5")
  

    def test_update_score(self):
        """Test Exercise 4: Global vs Local Scope"""
        # Reset global score before testing
        global score
        score = 0
      
         # Test score updates
        self.assertEqual(update_score(5), 5)
        self.assertEqual(update_score(3), 8)
        self.assertEqual(update_score(-2), 6)

        # Test invalid input
        with self.assertRaises(TypeError):
            update_score("5")


    def test_get_circle_properties(self):
        """Test Exercise 5: Multiple Return Values and Tuple Unpacking"""
        # Test with radius 1
        area, circumference = get_circle_properties(1)
        self.assertAlmostEqual(area, math.pi, places=9)
        self.assertAlmostEqual(circumference, 2 * math.pi, places=9)
        
        area, circumference = get_circle_properties(2)
        self.assertAlmostEqual(area, 4 * math.pi, places=9)
        self.assertAlmostEqual(circumference, 4 * math.pi, places=9)
      
        # Test invalid input
        with self.assertRaises(ValueError):
            get_circle_properties(-1.0)


    def test_calculate_bmi(self):
        """Test Exercise 6: Input Validation and Error Handling"""

        # Test normal BMI calculation
        self.assertAlmostEqual(calculate_bmi(70, 1.75), 22.9, places=1)
        self.assertAlmostEqual(calculate_bmi(85, 1.80), 26.2, places=1)
        self.assertIsInstance(calculate_bmi(70, 1.75), float)

        # Test edge cases
        with self.assertRaises(ValueError):
            calculate_bmi(0, 1.75)
        with self.assertRaises(ValueError):
            calculate_bmi(70.0, 0)
        with self.assertRaises(ValueError):
            calculate_bmi(-70.0, 1.75)
        with self.assertRaises(TypeError):
            calculate_bmi("70", "1.75")
  

    def test_factorial(self):
        """Test Exercise 7: Recursion with Base Case and Error Handling"""
        # Test basic factorial calculations
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(10), 3628800)
        with self.assertRaises(ValueError):
            factorial(-1)
        with self.assertRaises(TypeError):
            factorial(1.5)
      

    def test_analyze_numbers(self):
        """Test Exercise 8: Complex Return Types and Dictionary Handling"""
        result = analyze_numbers([1, 2, 3, 4, 5])
        self.assertEqual(result['sum'], 15)
        self.assertEqual(result['average'], 3)
        self.assertEqual(result['maximum'], 5)
        self.assertEqual(result['minimum'], 1)
        
        result = analyze_numbers([-1, 0, 1])
        self.assertEqual(result['sum'], 0)
        self.assertEqual(result['average'], 0)
        self.assertEqual(result['maximum'], 1)
        self.assertEqual(result['minimum'], -1)
        
        # Test empty list handling
        with self.assertRaises(ValueError):
            analyze_numbers([])


    def test_create_profile(self):
        """Test Exercise 9: Default Parameters and Type Checking"""
        # Test with all parameters
        profile = create_profile("Alice", 25, "Student")
        self.assertEqual(profile['name'], "Alice")
        self.assertEqual(profile['age'], 25)
        self.assertEqual(profile['occupation'], "Student")
      
        expected_profile2 = {"name": "Bob", "age": 30, "occupation": "Engineer"}
        self.assertEqual(create_profile("Bob", 30, "Engineer"), expected_profile2)
        
        # Test invalid inputs
        with self.assertRaises(TypeError):
            create_profile(123, 25)
        with self.assertRaises(TypeError):
            create_profile("Alice", "25")
        with self.assertRaises(ValueError):
            create_profile("Alice", -25)
     
       
    def test_validate_password(self):
        """Test Exercise 10: Complex Logic and Multiple Validation"""
        # Valid passwords
        self.assertTrue(validate_password("Abc12345"))
        self.assertTrue(validate_password("ComplexPass1"))
        self.assertTrue(validate_password("Pass1234"))
        
        # Invalid passwords
        self.assertFalse(validate_password("abc123"))  # Too short
        self.assertFalse(validate_password("abcdefgh"))  # No uppercase
        self.assertFalse(validate_password("ABCDEFGH"))  # No lowercase
        self.assertFalse(validate_password("Abcdefgh"))  # No number
        self.assertFalse(validate_password("12345678"))  # No letters
        self.assertFalse(validate_password(""))  # Empty string
        
        # Test type validation
        with self.assertRaises(TypeError):
            validate_password(123)  # Invalid input type
          

if __name__ == '__main__':
    unittest.main()
