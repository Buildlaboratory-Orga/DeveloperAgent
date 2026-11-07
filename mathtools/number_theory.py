"""Simple number theory functions for integers."""


def is_even(n: int) -> bool:
    """Return True if n is even."""
    return not n % 2


def is_prime(n: int) -> bool:
    """Return True if n is a prime number.

    Raises ValueError for negative numbers.
    """
    if n < 0:
        raise ValueError("is_prime is not defined for negative numbers")
    if n < 2:
        return False
    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            return False
    return True


def gcd(a: int, b: int) -> int:
    """Return the greatest common divisor (Euclidean algorithm)."""
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    """Return the least common multiple."""
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)
