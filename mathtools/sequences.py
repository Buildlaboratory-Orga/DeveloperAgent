"""Classic number sequences."""


def factorial(n: int) -> int:
    """Return n! (n >= 0)."""
    if n < 0:
        raise ValueError("n must be >= 0.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def fibonacci(n: int) -> int:
    """Return the n-th Fibonacci number (fibonacci(0) = 0, fibonacci(1) = 1)."""
    if n < 0:
        raise ValueError("n must be >= 0.")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def sum_up_to(n: int) -> int:
    """Return 1 + 2 + ... + n (n >= 0)."""
    if n < 0:
        raise ValueError("n must be >= 0.")
    return n * (n + 1) // 2
