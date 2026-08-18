# Dependency Injection is a design pattern where an object's dependencies are provided from outside rather than being created by the object itself. It helps achieve loose coupling and improves testability and maintainability.
# <b>7. Types of Dependency Injection</b>
# There are three commonly discussed types:
# <b>1. Constructor Injection ⭐</b>
# Most common and recommended.
class UserService:
    def __init__(self, database):
        self.database = database
# Dependency is passed through the constructor.


# <b>2. Setter/Property Injection</b>
# Dependency is assigned after object creation.
class UserService:
    def set_database(self, database):
        self.database = database
# Usage:
service = UserService()
service.set_database(database)


# <b>3. Method Injection</b>
# Dependency is passed directly to a method.
class UserService:
    def create_user(self, user, database):
        database.save(user)
# Usage:
service = UserService()
service.create_user("Anand", database)


# ---------------------------------------------------------
# -------------------------------------------------------
class marks:
    def __init__(self):
        pass

    def get_marks(self, name, m1, m2, m3):
        result = {
            "user_name": name,
            "total_marks": m1 + m2 + m3
        }
        return result


class student:
    def __init__(self, calc_marks, name, m1, m2, m3):
        self.calc_marks = calc_marks
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def get_stu_marks(self):
        return self.calc_marks.get_marks(
            self.name,
            self.m1,
            self.m2,
            self.m3
        )


ob_marks = marks()

ob_student = student(
    ob_marks,
    "John",
    85,
    90,
    78
)

print(ob_student.get_stu_marks())

# Output:
# {'user_name': 'John', 'total_marks': 253}

# Where is Dependency Injection?
# The important part is:

class student:
    def __init__(self, calc_marks, name, m1, m2, m3):
        self.calc_marks = calc_marks

# student depends on the marks object.
# But student does not create the marks object.
# Instead, we create it outside:
ob_marks = marks()

# and then inject it into student:
ob_student = student(ob_marks, "John", 85, 90, 78)

# So:
# marks object
#      ↓
#    inject
#      ↓
# student object
# That's Dependency Injection.
