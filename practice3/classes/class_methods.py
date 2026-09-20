# Here is a class that represents a calculator.
class Calculator:

    # Here is a method that adds two numbers.
    def add(self, first_number, second_number):
        return first_number + second_number

    # Here is a method that multiplies two numbers.
    def multiply(self, first_number, second_number):
        return first_number * second_number


# Here is a Calculator object.
calculator = Calculator()

# Here is an example of using the class methods.
print("Addition:", calculator.add(5, 3))
print("Multiplication:", calculator.multiply(5, 3))
