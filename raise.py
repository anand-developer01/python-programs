# Examples of using raise in Python

# 1. Raise a built-in exception
age = 15
if age < 18:
    raise ValueError("Age must be 18 or older.")
# Output:
# Traceback (most recent call last):
#   File "main.py", line 5, in <module>
#     raise ValueError("Age must be 18 or older.")
# ValueError: Age must be 18 or older.

# 2. Raise a custom exception
class MyError(Exception):
    pass

number = -3
if number < 0:
    raise MyError("Negative numbers are not allowed.")
# Output:
# Traceback (most recent call last):
#   File "main.py", line 11, in <module>
#     raise MyError("Negative numbers are not allowed.")
# MyError: Negative numbers are not allowed.

# 3. Raise inside a function

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

# Output when calling divide(10, 0):
# Traceback (most recent call last):
#   File "main.py", line 19, in <module>
#     print(divide(10, 0))
#   File "main.py", line 16, in divide
#     raise ZeroDivisionError("Cannot divide by zero.")
# ZeroDivisionError: Cannot divide by zero.

# 4. Catch the exception and handle it
try:
    print(divide(10, 0))
except ZeroDivisionError as e:
    print("Caught error:", e)
# Output:
# Caught error: Cannot divide by zero.

# 5. Re-raise exception after logging
try:
    value = int("abc")
except ValueError:
    print("Conversion failed.")
    raise
# Output:
# Conversion failed.
# Traceback (most recent call last):
#   File "main.py", line 32, in <module>
#     value = int("abc")
# ValueError: invalid literal for int() with base 10: 'abc'

# 6. Real-time example: validating login input

def login(username, password):
    if not username:
        raise ValueError("Username is required.")
    if len(password) < 6:
        raise ValueError("Password must be at least 6 characters long.")
    return "Login successful"

# Example call
# login("", "12345")
# Output:
# Traceback (most recent call last):
#   File "main.py", line 45, in <module>
#     login("", "12345")
#   File "main.py", line 39, in login
#     raise ValueError("Username is required.")
# ValueError: Username is required.
