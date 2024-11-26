import math
"""
Python Functions Workshop Exercises
---------------------------------
This file contains exercises that progress from basic to advanced function concepts.
Each exercise includes detailed documentation and examples of common pitfalls.
"""

# Exercise 1: Basic Function Definition and Documentation
def greet_user():

    """
    Create a function that prints 'Hello, World!'
    
    Common mistakes to avoid:
    - Forgetting parentheses when calling the function
    - Confusing print with return
    - Inconsistent indentation
    """
  # TODO: Implement this function
    word = "Hello, World!"
    print(word)
  

# Exercise 2: Function Parameters and Type Hints
def personalized_greeting(name):
    """
    Create a function that takes a name parameter and returns a personalized greeting
    
    Parameters:
        name (str): The name of the person to greet
        
    Returns:
        str: A personalized greeting message
        
    Raises:
        TypeError: If name is not a string
        
    Examples:
        >>> personalized_greeting("Alice")
        'Hello, Alice!'
        >>> personalized_greeting(123)
        Raises TypeError
    """
    # name = input("Enter name")  # TODO: Implement this function
    if not any(char.isalpha() for char in name):
        raise TypeError("Must be letters only")
    print(f"Hello {name}")
    return f"Hello, {name}!"

# Exercise 3: Multiple Parameters and Default Values
def calculate_rectangle_area(length, width):
    """
    Calculate the area of a rectangle. If width is not provided, calculate area of a square.
    
    Parameters:
        length (float): The length of the rectangle
        width (float, optional): The width of the rectangle. Defaults to length if None.
        
    Returns:
        float: The area of the rectangle
        
    Raises:
        ValueError: If length or width is negative
        TypeError: If inputs are not numbers
        
    Common mistakes to avoid:
    - Not handling negative inputs
    - Not validating parameter types
    - Using mutable default values
    """
      # TODO: Implement this function
    length = input("Length: ")
    width = input("Width: ")
    
    
    if not length.isnumeric() or not width.isnumeric():
        raise TypeError("Length and width must be integer")
    
    else:

        length = int(length)
        width = int(width)
        
        if length < 0 or width < 0:
            raise ValueError("Can't have negative length or negative width")
        
        area_rec = length * width
        area_sqr = length ** 2
        
        if width == length:
            print(area_sqr)
            return area_sqr
        else:
            print(area_rec)
            return area_rec
        
    
# Exercise 4: Global vs Local Scope
score = 0  # Global variable

def update_score(points):
    """
    Update the global score variable by adding points
    
    Parameters:
        points (int): Points to add to the score
        
    Returns:
        int: The new score after adding points
        
    Common mistakes to avoid:
    - Forgetting 'global' keyword
    - Shadowing global variables
    - Overusing global variables
    """
    global score
    
    i = 10
    while i > 5:
        score += 1
        points += score
        i -= 1
    return points
      # TODO: Implement this function
  

# Exercise 5: Multiple Return Values and Tuple Unpacking
def get_circle_properties(radius):
    """
    Calculate area and circumference of a circle
    
    Parameters:
        radius (float): The radius of the circle
        
    Returns:
        tuple: (area(float), circumference(float)) of the circle
        
    Examples:
        >>> area, circumference = get_circle_properties(1)
        >>> print(f"Area: {area:.2f}, Circumference: {circumference:.2f}")
        Area: 3.14, Circumference: 6.28
    """
     # TODO: Implement this function
    
    # Little Error handling implemented because with example input provided, radius will always
    # be an integer so no need to check for isnumeric??
    
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    else:
        area = (2 * math.pi * radius)
        circumference = math.pi * (radius ** 2)
        return (area,circumference)
  

# Exercise 6: Input Validation and Error Handling
def calculate_bmi(weight, height):
    """
    Calculate BMI (Body Mass Index) with proper input validation
    
    Parameters:
        weight (float): Weight in kilograms
        height (float): Height in meters
        
    Returns:
        float: BMI value rounded to 1 decimal place
        
    Raises:
        ValueError: If weight or height is negative or zero
        TypeError: If inputs are not numbers
    """
  # TODO: Implement this function

    # weight = input("Weight: ")
    # height = input("Height: ")
    # ISNUMERIC DOES NOT WORK FOR CHECKING FLOATS< NEED TO USE TRY AND EXCEPT

    try:
        weight = float(weight)
        height = float(height)
    except TypeError:
        raise TypeError("Weight and HEight must be floats")
        
    if weight <= 0 or height <=0:
        raise ValueError("How are you still alive?")
    
    bmi_local = round(weight / (height ** 2),1)
    return bmi_local

  

# Exercise 7: Recursion with Base Case and Error Handling
def factorial(n):
    """
    Calculate the factorial of a number using recursion
    
    Parameters:
        n (int): The number to calculate factorial for
        
    Returns:
        int: The factorial of n
        
    Raises:
        ValueError: If n is negative
        RecursionError: If recursion depth is exceeded
        
    Common mistakes to avoid:
    - Missing base case
    - Not handling negative numbers
    - Not considering stack overflow
    """
    if not any(char.isnumeric() for char in n):
        raise TypeError("N must be a numer")
    
    original_n = int(n)
    running_n = original_n
    if original_n < 0:
        raise ValueError("N cannot be negative")
    
    while original_n > 1:
        running_n = running_n * (original_n-1)
        original_n -= 1
        print(running_n)
    return running_n
        
    
      # TODO: Implement this function
  

# Exercise 8: Complex Return Types and Dictionary Handling
def analyze_numbers(numbers):
    """
    Analyze a list of numbers and return various statistics
    
    Parameters:
        numbers (list): List of numbers to analyze
        
    Returns:
        dict: Dictionary containing:
            - 'sum': Sum of numbers
            - 'average': Average of numbers
            - 'maximum': Maximum number
            - 'minimum': Minimum number
            
    Raises:
        ValueError: If the list is empty
        TypeError: If any element is not a number
        
    Example:
        >>> stats = analyze_numbers([1, 2, 3, 4, 5])
        >>> print(f"Average: {stats['average']}")
        Average: 3.0
    """
    # TODO: Implement this function

    numbers_split = numbers.split(",")
    print(numbers_split)

    # Items in numbvers_split are not integers therefore max and min will not work.
    # Oppourtunity to see list comprehension in practice
    numbers_int_split = [int(num) for num in numbers_split]
    max_num = max(numbers_int_split)
    min_num = min(numbers_int_split)

    stats_dict = {}

    
    if not numbers:
        raise ValueError("List cannot be empty")
    
    sum_item = 0
    running_sum = 0
    
    for index,item in enumerate(numbers_split):
        if not item.isnumeric():
            raise TypeError("Items in list must be numeric")
        
        item = int(item)

        running_sum += item
        
        if index + 1 < len(numbers_split):
            next_item = int(numbers_split[index + 1])
            item += next_item
            
         
        sum_item = running_sum
            # print(sum_item)
            
    average =  sum_item / len(numbers_split) 
    
    
    stats_dict['sum'] = sum_item
    stats_dict['average'] = average
    stats_dict['maximum'] = max_num
    stats_dict['minimum'] = min_num

    print(stats_dict)
    print(f"{stats_dict['maximum']}")
    
    print(f"Average: {stats_dict['maximum']}")
    return stats_dict
  

# Exercise 9: Default Parameters and Type Checking
def create_profile(name, age, occupation="Student"):
    """
    Create a user profile with optional occupation
    
    Parameters:
        name (str): User's name
        age (int): User's age
        occupation (str, optional): User's occupation. Defaults to "Student"
        
    Returns:
        dict: User profile dictionary
        
    Raises:
        TypeError: If name is not str or age is not int
        ValueError: If age is negative
    """

    profile_dict = {}

    name = input("Name: ")
    age = input("Age: ")
    occupation = input("Occupation: ")

    if not isinstance(name,str):
        raise TypeError("Name must be in string format")
    
    try:
        age = int(age)

    except ValueError:
        pass
    
    profile_dict['name'] = name
    profile_dict['age'] = age
    profile_dict['oocupation'] = occupation
    
    print(profile_dict)
    return profile_dict
    # TODO: Implement this function
  

# Exercise 10: Complex Logic and Multiple Validation
def validate_password(password):
  
    """
    Validate a password based on multiple criteria
    
    Password must:
    - Be at least 8 characters long
    - Contain at least one uppercase letter
    - Contain at least one lowercase letter
    - Contain at least one number
    
    Parameters:
        password (str): Password to validate
        
    Returns:
        bool: True if password meets all criteria, False otherwise
        
    Raises:
        TypeError: If password is not a string
        
    Examples:
        >>> validate_password("Abc12345")
        True
        >>> validate_password("abc123")  # Too short
        False
        >>> validate_password("12345678")  # No letters
        False
        >>> validate_password("abcdefgh")  # No numbers or uppercase
        False
        >>> validate_password(12345)  # Not a string
        Raises TypeError
        
    Common mistakes to avoid:
    - Not handling non-string inputs
    - Using regular expressions without proper error handling
    - Not checking all criteria independently
    - Forgetting to validate input type before processing
    """
      # TODO: Implement this function
      
    password = input("Password: ")
    truth = 0
    
    if isinstance(password,int):
        print("Password must be string")
        truth -= 1
    
    if len(password) < 8:
        print("Password too short")
        truth -= 1
    
    if not any(char.isnumeric() for char in password):
        print("Password must have numbers")
        truth -= 1
        
    if password.isalnum():
        print("Password has no letters")
        truth -= 1
            
    if not any(char.isupper() for char in password):
        print("No uppercase letters")
        truth -= 1
        
    if not any(char.islower() for char in password):
        print("No lowercase letters")
        truth -= 1
        return truth
        
    if truth < 6:
        return True
    else:
        return False

if __name__ == "__main__":
    
    # Example usage of functions
    # print("Testing greet_user():")
    # greet_user()
    
    # print("\nTesting personalized_greeting():")
    # greeting = personalized_greeting("Alice")
    # print(greeting)
    
    # print("\nTesting calculate_rectangle_area():")
    # area = calculate_rectangle_area(5, 3)
    # print(f"Rectangle area: {area}")
    
    # print("\nTesting update_score():")
    # points = update_score(2)
    # print(f"Points: {points}")
    
    # print("\nTesting get_circle_properties():")
    # props = get_circle_properties(1)
    # print(f"Area: {props[0]:.2f}, Circumference: {props[1]:.2f}")
    
    # print("\nTesting calculate_bmi():")
    # try:
    #     weight = input("Weight: ")
    #     height = input("Height: ")
    #     bmi = calculate_bmi(weight,height)
    #     print(f"Bmi: {bmi}")
    # except Exception as e:
    #     print(e)
        
    print("\nTesting factorial:")
    n = input("n: ")
    factorial_n = factorial(n)
    print(f"Factorial: {factorial_n}")
        
    # print("\nTesting analyzing_numbers:")
    # list_num = input("Numbers: ")
    # numbers = analyze_numbers(list_num)

    # print("\nTesting create_profile():")
    # profile = create_profile("Onalerona",19,"Student")
    # print(f"Profile: {profile}")
    
    # print("\nTesting password():")
    # password = validate_password("Zwan30n@")
    # print(f"Password: {password}")

    
        
        
    