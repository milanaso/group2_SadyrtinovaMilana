# Here is a function with a required argument and a default argument.
def introduce_student(name, age, city="Almaty"):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")


# Here is an example of using positional arguments.
introduce_student("Milana", 18)

# Here is an example of changing the default argument.
introduce_student("Alice", 21, "Astana")
