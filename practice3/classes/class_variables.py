# Here is a class demonstrating class and instance variables.
class Student:

    # Here is a class variable shared by all students.
    school = "ABC School"

    # Here is the constructor with an instance variable.
    def __init__(self, name):
        self.name = name


# Here are two different Student objects.
student_one = Student("Ayan")
student_two = Student("Alice")

# Here is the shared class variable.
print(student_one.school)
print(student_two.school)

# Here are individual instance variables.
print(student_one.name)
print(student_two.name)
