# Here is the first parent class.
class Addition:

    # Here is a method for addition.
    def add(self, a, b):
        return a + b


# Here is the second parent class.
class Multiplication:

    # Here is a method for multiplication.
    def multiply(self, a, b):
        return a * b


# Here is a child class inheriting from two parent classes.
class Calculator(Addition, Multiplication):
    pass


# Here is a Calculator object.
calculator = Calculator()

# Here is a method inherited from Addition.
print("Addition:", calculator.add(5, 3))

# Here is a method inherited from Multiplication.
print("Multiplication:", calculator.multiply(5, 3))
