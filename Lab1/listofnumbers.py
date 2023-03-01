from random import randint


def list_numbers():
    numbers = []
    numbers_even = []

    for i in range(20):
        numbers.append(randint(-10, 10))
        if not numbers[i] % 2:
            numbers_even.append(numbers[i])

    print(numbers)
    return print(numbers_even)