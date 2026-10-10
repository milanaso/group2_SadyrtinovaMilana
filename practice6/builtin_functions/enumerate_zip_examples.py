names = ["Anna", "Milana", "Alex"]
grades = [90, 95, 85]

print("Enumerate:")
for index, name in enumerate(names, start=1):
    print(index, name)

print("Zip:")
for name, grade in zip(names, grades):
    print(name, grade)

number = "123"
print(int(number))
print(float(number))
print(str(100))
print(bool(1))

print("Type:", type(number))
print("Is integer:", isinstance(123, int))
