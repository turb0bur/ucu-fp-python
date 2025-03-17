def is_prime(n: int) -> bool:
    if n <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    if n <= 3:
        return True  # 2 and 3 are prime numbers
    if n % 2 == 0 or n % 3 == 0:
        return False  # Any number divisible by 2 or 3 is not prime

    def is_prime_rec(i: int) -> bool:
        if i * i > n:
            return True  # If i squared is greater than n, n is prime
        if n % i == 0 or n % (i + 2) == 0:
            return False  # If n is divisible by i or i + 2, n is not prime
        return is_prime_rec(i + 6)

    return is_prime_rec(5)