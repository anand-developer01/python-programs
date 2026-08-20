Suppose we have:

def hello():
    print("Hello")
# ----------------
# Now we want to print "Starting..." before hello() runs.
# Instead of modifying hello(), we can create a decorator:
def my_decorator(func):
    def wrapper():
        print("Starting...")
        func()
        print("Finished...")
    return wrapper

# Apply it using @:
@my_decorator
def hello():
    print("Hello")

# Now:
hello()

# Output:
# Starting...
# Hello
# Finished...

# -----------------------------------------------
# What actually happens?
# ----------------------------------------------
# This:
@my_decorator
def hello():
    print("Hello")
# is basically equivalent to:
def hello():
    print("Hello")
  
hello = my_decorator(hello)

# So Python takes the original "hello" function and ``passes it to the decorator``.
# The decorator returns a new function (wrapper), and "hello" now refers to that wrapper.

# ----------------------------------------------
#  Example : 2
# ----------------------------------------------
def log_call(func):
    def wrapper():
        print(f"Calling {func.__name__}")
        func()
    return wrapper

@log_call
def calculate():
    print("Calculating...")

@log_call
def save():
    print("Saving...")


calculate()
save()
# Output:
# Calling calculate
# Calculating...
# Calling save
# Saving...


# ---------------------------------------
# Decorators with arguments
# --------------------------------------
def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print("Completed")
        return result
    return wrapper


@log_call
def add(a, b):
    return a + b

result = add(10, 20)
print(result)

# Output:
# Calling add
# Completed
# 30

# -----------------------------
# Dictionary as keyword arguments
# --------------------------------------
def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print("Completed")
        return result
    return wrapper

@log_call
def display_user(name, age, city):
    return {
        "name": name,
        "age": age,
        "city": city
    }

user = {
    "name": "Anand",
    "age": 36,
    "city": "Hyderabad"
}

result = display_user(**user)
print(result)
# Output:------------  
# Calling display_user
# Completed
# {'name': 'Anand', 'age': 36, 'city': 'Hyderabad'}


# -----------------------------
# decorator can handle both positional arguments and a dictionary.
# --------------------------------------
def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")

        print("Positional arguments:", args)
        print("Keyword arguments:", kwargs)

        result = func(*args, **kwargs)

        print("Completed")
        return result
    return wrapper


@log_call
def display_user(name, age, city):
    return {
        "name": name,
        "age": age,
        "city": city
    }


# user = {
#     "name": "Anand",
#     "age": 36,
#     "city": "Hyderabad"
# }

result = display_user("Anand", 36, **{"city": "Hyderabad"})
print(result)
# Output:--------------------
# Calling display_user
# Positional arguments: ('Anand', 36)
# Keyword arguments: {'city': 'Hyderabad'}
# Completed
# {'name': 'Anand', 'age': 36, 'city': 'Hyderabad'}
