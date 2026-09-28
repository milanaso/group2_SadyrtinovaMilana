# 1. Generator that generates squares of numbers up to N

def squares_up_to(n):
    for i in range(n + 1):
        yield i ** 2


n = int(input("Enter N: "))

for square in squares_up_to(n):
    print(square)


# 2. Generator that prints even numbers from 0 to n

def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i


n = int(input("Enter n: "))

print(",".join(str(num) for num in even_numbers(n)))


# 3. Generator for numbers divisible by 3 and 4

def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i


n = int(input("Enter n: "))

for num in divisible_by_3_and_4(n):
    print(num)


# 4. Generator squares from a to b

def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2


a = int(input("Enter a: "))
b = int(input("Enter b: "))

for value in squares(a, b):
    print(value)


# 5. Generator that returns numbers from n down to 0

def countdown(n):
    while n >= 0:
        yield n
        n -= 1


n = int(input("Enter n: "))

for num in countdown(n):
    print(num)