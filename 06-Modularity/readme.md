# Exercise: Modularity in Python

## Objective
The goal of this exercise is to practice modular programming in Python by creating and using modules. This will help you understand how to organize your code into reusable and maintainable components.

## Instructions

1. **Create a Module:**
   - Create a new Python file named `math_operations.py`.
   - In this file, define the following functions:
     - `add(a, b)`: Returns the sum of `a` and `b`.
     - `subtract(a, b)`: Returns the difference between `a` and `b`.
     - `multiply(a, b)`: Returns the product of `a` and `b`.
     - `divide(a, b)`: Returns the quotient of `a` divided by `b`.

2. **Create Another Module:**
   - Create another Python file named `geometry.py`.
   - In this file, define the following functions:
     - `area_of_circle(radius)`: Returns the area of a circle given its `radius`.
     - `perimeter_of_circle(radius)`: Returns the perimeter of a circle given its `radius`.
     - `area_of_rectangle(length, width)`: Returns the area of a rectangle given its `length` and `width`.
     - `perimeter_of_rectangle(length, width)`: Returns the perimeter of a rectangle given its `length` and `width`.

3. **Create a Main Program:**
   - Create a new Python file named `main.py`.
   - In this file, import the functions from `math_operations.py` and `geometry.py`.
   - Use these functions to perform the following tasks:
     - Calculate and print the sum, difference, product, and quotient of two numbers.
     - Calculate and print the area and perimeter of a circle with a given radius.
     - Calculate and print the area and perimeter of a rectangle with given length and width.

## Example Code

### math_operations.py
```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero is not allowed"
```

### geometry.py
```python
import math

def area_of_circle(radius):
    return math.pi * (radius ** 2)

def perimeter_of_circle(radius):
    return 2 * math.pi * radius

def area_of_rectangle(length, width):
    return length * width

def perimeter_of_rectangle(length, width):
    return 2 * (length + width)
```

### main.py
```python
from math_operations import add, subtract, multiply, divide
from geometry import area_of_circle, perimeter_of_circle, area_of_rectangle, perimeter_of_rectangle

# Math operations
a = 10
b = 5
print(f"Sum: {add(a, b)}")
print(f"Difference: {subtract(a, b)}")
print(f"Product: {multiply(a, b)}")
print(f"Quotient: {divide(a, b)}")

# Geometry calculations
radius = 7
length = 10
width = 5
print(f"Area of circle: {area_of_circle(radius)}")
print(f"Perimeter of circle: {perimeter_of_circle(radius)}")
print(f"Area of rectangle: {area_of_rectangle(length, width)}")
print(f"Perimeter of rectangle: {perimeter_of_rectangle(length, width)}")
```

## Conclusion
By completing this exercise, you will gain hands-on experience with modular programming in Python. This will help you write more organized, reusable, and maintainable code.

Happy coding!
