# Here is the parent class.
class Person:

    # Here is the parent constructor.
    def __init__(self, name):
        self.name = name


# Here is the child class.
class Student(Person):

    # Here is the child constructor.
    def __init__(self, name, grade):

        # Here is super() calling the parent constructor.
        super().__init__(name)

        self.grade = grade


# Here is a Student object.
student = Student("Alina", 5)
print("Name:", student.name)
print("Grade:", student.grade)
