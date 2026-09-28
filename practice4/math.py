import math
from math import pi, radians, tan

# 1. Convert degree to radian

degree = float(input("Input degree: "))

radian = radians(degree)

print("Output radian:", radian)


# 2. Area of a trapezoid

height = float(input("Height: "))
base1 = float(input("Base, first value: "))
base2 = float(input("Base, second value: "))

area = ((base1 + base2) / 2) * height

print("Expected Output:", area)


# 3. Area of a regular polygon

n = int(input("Input number of sides: "))
side = float(input("Input the length of a side: "))

# Formula:
# Area = n * side^2 / (4 * tan(pi/n))

area = (n * side ** 2) / (4 * tan(pi / n))

print("The area of the polygon is:", area)


# 4. Area of a parallelogram

base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))

area = base * height

print("Expected Output:", area)