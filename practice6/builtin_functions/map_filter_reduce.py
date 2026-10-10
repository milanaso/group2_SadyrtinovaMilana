
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

squared = list(map(lambda x: x ** 2, numbers))
print("Squares:", squared)

even = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even)

total = reduce(lambda x, y: x + y, numbers)
print("Sum:", total)

print("Length:", len(numbers))
print("Sum:", sum(numbers))
print("Minimum:", min(numbers))
print("Maximum:", max(numbers))
print("Sorted descending:", sorted(numbers, reverse=True))
