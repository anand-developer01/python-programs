# Custom Exceptions in Python

# 1. Simple custom exception
class AgeError(Exception):
    pass

try:
    age = 15
    if age < 18:
        raise AgeError("Age must be 18 or older.")
except AgeError as e:
    print("Caught custom exception:", e)
# Output:
# Caught custom exception: Age must be 18 or older.

# 2. Custom exception with a message and extra details
class InvalidMarksError(Exception):
    def __init__(self, marks):
        self.marks = marks
        super().__init__(f"Invalid marks: {marks}. Marks must be between 0 and 100.")

try:
    marks = 120
    if marks < 0 or marks > 100:
        raise InvalidMarksError(marks)
except InvalidMarksError as e:
    print(e)
# Output:
# Invalid marks: 120. Marks must be between 0 and 100.

# 3. Custom exception for a login system
class LoginError(Exception):
    pass

def login(username, password):
    if not username:
        raise LoginError("Username is required.")
    if len(password) < 6:
        raise LoginError("Password must be at least 6 characters long.")
    return "Login successful"

try:
    print(login("", "12345"))
except LoginError as e:
    print("Login failed:", e)
# Output:
# Login failed: Username is required.

# 4. Custom exception for invalid user role
class RoleError(Exception):
    pass

def assign_role(role):
    valid_roles = ["admin", "user", "manager"]
    if role not in valid_roles:
        raise RoleError(f"Invalid role: {role}")
    return f"Role assigned: {role}"

try:
    print(assign_role("guest"))
except RoleError as e:
    print(e)
# Output:
# Invalid role: guest

# 5. Real-time example: user registration validation
class RegistrationError(Exception):
    pass

def register_user(username, email, age):
    if not username:
        raise RegistrationError("Username is required.")
    if "@" not in email:
        raise RegistrationError("Email is invalid.")
    if age < 18:
        raise RegistrationError("User must be at least 18 years old.")
    return "Registration successful"

try:
    print(register_user("alice", "alicegmail.com", 17))
except RegistrationError as e:
    print("Registration failed:", e)
# Output:
# Registration failed: Email is invalid.
