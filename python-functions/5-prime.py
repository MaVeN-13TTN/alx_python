def is_prime(number):
    if number <= 1:
        return False
    # We only need to check divisibility up to the square root of the number.
    #If the number is not prime, it must have a divisor smaller than or equal to its square root.
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False

    return True
