def filter_prime(numbers):
    result = []

    for number in numbers:
        if number < 2:
            continue

        prime = True

        for i in range(2, number):
            if number % i == 0:
                prime = False
                break

        if prime:
            result.append(number)

    return result


numbers = list(map(int, input().split()))

print(filter_prime(numbers))
