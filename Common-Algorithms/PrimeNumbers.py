# A prime is a natural number greater than 1 that has no positive divisors other than 1 and itself.

def is_prime(n):
    """
    Returns True if n is prime.
    Assumes that n is a positive natural number
    """
    # We know 1 is not a prime number
    if n == 1:
        return False

    i = 2
    # This will loop from 2 to int(sqrt(x))
    while i*i <= n:
        # Check if i divides x without leaving a remainder
        if n % i == 0:
            # This means that n has a factor in between 2 and sqrt(n)
            # So it is not a prime number
            return False
        i += 1

    # If we did not find any factor in the above loop,
    # then n is a prime number
    return True
