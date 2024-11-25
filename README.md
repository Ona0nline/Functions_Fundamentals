# Python Functions Workshop

## Description
Functions, functions, functions...

### 1. Function Fundamentals
#### 1.1 Basic Concepts
- Why we need functions
  - Code reusability
  - Modularity
  - Abstraction
  - Testing and maintenance
- Function definition syntax
- Function definition using `def`
- Function calling
- Function documentation (docstrings)
```python
# Basic function structure
def function_name(parameters):
    """Docstring explaining what the function does"""
    # Function body
    return result  # Optional return statement
```
- Proper indentation rules
- Naming conventions (snake_case for functions)

#### 1.2 Function Documentation
- Docstring formatting
- Type hints
- Function annotations
```python
def calculate_bmi(weight: float, height: float) -> float:
    """
    Calculate Body Mass Index (BMI).

    Args:
        weight: Person's weight in kilograms
        height: Person's height in meters

    Returns:
        float: Calculated BMI value

    Raises:
        ValueError: If weight or height is negative
    """
    if weight <= 0 or height <= 0:
        raise ValueError("Weight and height must be positive")
    return weight / (height ** 2)
```


### 2. Parameters and Arguments
#### 2.1 Understanding Function Parameters
- **What are Parameters?**
  - Parameters are variables defined in a function signature that specify what values (arguments) the function expects when it is called.

- **How Are Arguments Passed?**
  - Arguments are the actual values or expressions passed to the function when it is called, corresponding to the parameters.

- **Multiple Parameters**
  - Functions can accept more than one parameter, allowing them to handle multiple values when called.

- **Types of Parameters**
  - Parameters can be categorized into different types based on how they are used and how values are passed.

- **Positional Parameters**
  - These parameters must be passed to the function in the order they are defined. The argument values are assigned to the parameters based on their position in the function call.

- **Keyword Parameters**
  - These parameters are passed to the function by explicitly naming them when calling the function. This allows you to specify the order of the arguments and makes the function call more readable.

- **Default Parameters**
  - A parameter can have a default value that is used if no argument is provided for that parameter. This allows the function to work with fewer arguments in some cases.

- **Parameter Ordering Rules**
  - There are specific rules about how parameters should be ordered in the function signature to ensure the correct function behavior. These include:
    - **Positional-only parameters** must appear before the `/` symbol.
    - **Parameters that can be passed in any order** (standard parameters) come next.
    - **Keyword-only parameters** must appear after the `*` symbol.

**Example Function with Ordered Parameters:**
```python
def function(
    positional_only_params, /,    # Must be passed positionally
    standard_params,              # Can be passed either way
    *, keyword_only_params        # Must be passed as keywords
):
    pass
```

#### 2.2 Common Issues with Parameters
- **Mutable Default Arguments Problem**
  - **The Issue**: When you use a mutable object (like a list) as a default argument in a function, the default value is shared across function calls. This can lead to unexpected behavior, as changes made to the default value in one call affect future calls.
  
  **Incorrect Example**:
  ```python
  def append_to(element, target=[]):    # WRONG!
      target.append(element)
      return target
  ```
  - This function causes issues because the `target` list will persist across calls, and items will accumulate in the list every time the function is called.

  **Correct Approach**:
  - Instead of using a mutable default value, use `None` as the default value and create a new list inside the function if needed. This ensures that each function call gets its own separate list.
  
  **Corrected Example**:
  ```python
  def append_to(element, target=None):
      if target is None:
          target = []
      target.append(element)
      return target
  ```

This solution avoids modifying the default argument across calls and guarantees correct behavior.


### 3. Variable Scope and Lifetime
#### 3.1 Scope Rules (LEGB)
- Global variables
- Local variables
- Best practices for variable scope
- Local scope
- Enclosing scope
- Global scope
- Built-in scope


#### 3.2 Common Scope Issues
```python
total = 0

def update_total(value):
    total += value    # UnboundLocalError
    return total

# Correct approach
def update_total(value):
    global total
    total += value
    return total
```

### 4. Return Values
#### 4.1 Return Statement Behavior
- Function termination
- Storing returned values
- Implicit vs explicit returns
- Multiple return values
- Early returns

```python
# Multiple return values
def get_dimensions():
    return 100, 200  # Returns tuple (100, 200)

# Early returns for validation
def divide(a, b):
    if b == 0:
        return None  # Early return for invalid input
    return a / b
```

#### 4.2 Common Return Mistakes
```python
def calculate_average(numbers):
    if not numbers:
        print("List is empty")  # WRONG: printing instead of returning
        
    total = sum(numbers)
    avg = total / len(numbers)
    print(avg)  # WRONG: printing instead of returning

# Correct approach
def calculate_average(numbers):
    if not numbers:
        return None  # Return value for error case
    
    total = sum(numbers)
    return total / len(numbers)  # Return actual result
```

### 5. Advanced Function Concepts
#### 5.1 First-Class Functions
- Functions as objects
- Higher-order functions
- Closures
```python
def create_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier

double = create_multiplier(2)
triple = create_multiplier(3)
```

#### 5.2 Lambda Functions
```python
# Lambda function limitations
square = lambda x: x ** 2  # Not recommended

# Better approach
def square(x):
    return x ** 2
```

#### 5.3 Decorators
```python
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time} seconds")
        return result
    return wrapper

@timing_decorator
def slow_function():
    time.sleep(1)
```

### 6. Function Design Principles
#### 6.1 Clean Code Principles
- Single Responsibility Principle
- Pure functions vs functions with side effects
- Input validation
- Error handling
```python
# Good function design
def calculate_discount(price: float, discount_percent: float) -> float:
    """
    Calculate discounted price.
    
    Args:
        price: Original price
        discount_percent: Discount percentage (0-100)
        
    Returns:
        float: Discounted price
        
    Raises:
        ValueError: If inputs are invalid
    """
    if not isinstance(price, (int, float)) or not isinstance(discount_percent, (int, float)):
        raise TypeError("Price and discount must be numbers")
        
    if price < 0:
        raise ValueError("Price cannot be negative")
        
    if not 0 <= discount_percent <= 100:
        raise ValueError("Discount must be between 0 and 100")
        
    discount = price * (discount_percent / 100)
    return round(price - discount, 2)
```

## Common Pitfalls and Solutions
- Forgetting to return values from functions
- Confusion between global and local scope
- Improper indentation in function definitions
- Missing function parameters
- Infinite recursion in recursive functions

### 1. Parameter Handling
```python
# Pitfall: Modifying mutable parameters
def add_item(item, list=[]):  # WRONG
    list.append(item)
    return list

# Solution
def add_item(item, list=None):
    if list is None:
        list = []
    list.append(item)
    return list
```

### 2. Scope Issues
```python
# Pitfall: Accessing outer scope
def outer():
    x = 1
    def inner():
        print(x)  # Works: reading from outer scope
        x += 1    # UnboundLocalError: can't modify
    inner()

# Solution
def outer():
    x = [1]  # Use mutable object
    def inner():
        x[0] += 1  # Works: modifying mutable object
    inner()
```

### 3. Return Statement Issues
```python
# Pitfall: Missing return
def add(a, b):
    c = a + b
    # Missing return statement

# Solution
def add(a, b):
    c = a + b
    return c
```

### Running Unit Tests
```bash
python -m unittest tests/test_day1.py
python -m unittest tests/test_day2.py
# etc.
```

### Writing Your Own Tests
```python
import unittest

class TestMyFunctions(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)
        self.assertEqual(add_numbers(-1, 1), 0)
        with self.assertRaises(TypeError):
            add_numbers("2", 3)
```

### Recursion
Let's take a bit of detour and talk about recursion.

What is recursion?

Recursion is a programming concept where a function calls itself in order to solve a problem. It's like a task asking a smaller version of itself to help out until the task becomes so small and straightforward that it can be easily solved.

#The anatomy of a recursive function

def some_function(some_argument):

    if some_argument <= some_predetermined_limit: #This is called a base case check
        # Do something and terminate
        
    else:
        # Function will execute
        some_function(some_argument_modified) #This is a recursive call
Base Case Check: Inside the function, there's an if statement checking if some_argument is less than or equal to a certain limit (determined_some_limit). This is known as the base case. If this condition is met, the function performs some specific actions and then terminates.

Recursive Call: If the base case is not met (i.e., some_argument is greater than the limit), the function goes to the else block. Inside the else block, the function calls itself (some_function) with a potentially modified argument (some_argument_modified). This is the recursive step

NOTE: It's important to ensure that with each recursive call, the function moves towards the base case, where it can eventually terminate. If this condition is not met, the function will keep calling itself indefinitely, leading to a situation known as "infinite recursion."

#Let's put it into practice
#Let's start with a while loop
#Write a while loop that counts down from a user-specified number to 0 and prints "Blastoff!"

while something_something: 

    #Blah blah blah


------------------------------------------------------------------------------------

#Let's do the same thing recursively

def count_down(n):

    if 'basecase check':
        print("Blastoff!")

    else:
        #Do something here
        count_down('modify me here')

# Call the function with 5 as the starting point
count_down(10)
That's the end of our detour.

## Best Practices Checklist
- [ ] Use clear, descriptive function names
- [ ] Write comprehensive docstrings
- [ ] Validate input parameters
- [ ] Handle errors appropriately
- [ ] Write unit tests
- [ ] Keep functions focused (single responsibility)
- [ ] Avoid global variables when possible
- [ ] Use type hints for clarity
- [ ] Follow PEP 8 style guidelines
- [ ] Document exceptions and edge cases

## Debug Tips
1. Use print statements strategically
2. Utilize Python debugger (pdb)
3. Check function scope with locals() and globals()
4. Test edge cases separately
5. Verify parameter types

## Additional Resources
1. [Python Official Documentation - Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
2. [Real Python - Python Functions](https://realpython.com/defining-your-own-python-function/)


## Learning Outcomes
After completing this workshop, students should be able to:
1. Define and call functions with appropriate parameters
2. Understand and use function scope correctly
3. Implement return statements effectively
4. Write basic recursive functions
5. Debug common function-related issues


## Contributing
Feel free to submit pull requests for:
- Additional exercises
- Bug fixes
- Documentation improvements
- New test cases

## License
This project is licensed under the MIT License 








