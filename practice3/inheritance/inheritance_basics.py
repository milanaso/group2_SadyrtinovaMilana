# Here is the parent class.
class Person:

    # Here is a method that introduces a person.
    def introduce(self):
        print("I am a person.")


# Here is the child class that inherits from Person.
class Student(Person):

    # Here is a method specific to Student.
    def study(self):
        print("I am studying.")


# Here is an object created from the Student class.
student = Student()

# Here is the method inherited from Person.
student.introduce()

# Here is the method from Student.
student.study()
