def prime_factors(n):
    """This returns all factors of N.

    >>> prime_factors(8)
    2
    2
    2
    >>> prime_factors(9)
    3
    3
    >>> prime_factors(10)
    2
    5
    >>> prime_factors(11)
    11
    >>> prime_factors(12)
    2
    2
    3
    >>> prime_factors(858)
    2
    3
    11
    13
    """
    while n > 1:
        k = smallest_prime_factor(n)
        n = n / k
        print(k)

def smallest_prime_factor(n):
    g = 2
    while n % g != 0:
      g = g + 1
    return g
