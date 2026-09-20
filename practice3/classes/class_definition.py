# Here is a class that works with a number.
class Number:

    # Here is a method that doubles the number.
    def double(self, number):
        return number * 2


# Here is an object created from the Number class.
my_number = Number()

# Here is the object using the class method.
result = my_number.double(10)
print("Result:", result)
