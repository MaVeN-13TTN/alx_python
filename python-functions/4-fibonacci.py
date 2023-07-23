def fibonacci_sequence(n):
    if n <= 0:
        return []

    fib_numbers = [0, 1]
    for i in range(2, n + 1):
        fib_numbers.append(fib_numbers[i - 1] + fib_numbers[i - 2])

    return fib_numbers
