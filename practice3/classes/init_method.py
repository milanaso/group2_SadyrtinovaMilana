# Here is a class that represents a person.
class Person:

    # Here is the __init__ method that sets the person's information.
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Here is an object created from the Person class.
person = Person("Ayan", 20)
print("Name:", person.name)
print("Age:", person.age)
