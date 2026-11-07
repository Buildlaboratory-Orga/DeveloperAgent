"""Descriptive statistics for lists of numbers."""


def mean(values: list[float]) -> float:
    """Return the arithmetic mean."""
    if not values:
        raise ValueError("values must not be empty.")
    return sum(values) / len(values)


def median(values: list[float]) -> float:
    """Return the median (middle value of the sorted list)."""
    if not values:
        raise ValueError("values must not be empty.")
    sorted_values = sorted(values)
    n = len(sorted_values)
    middle = n // 2
    if n % 2 == 1:
        return sorted_values[middle]
    return (sorted_values[middle - 1] + sorted_values[middle]) / 2


def minimum(values: list[float]) -> float:
    """Return the smallest value."""
    if not values:
        raise ValueError("values must not be empty.")
    smallest = values[0]
    for v in values:
        if v < smallest:
            smallest = v
    return smallest


def maximum(values: list[float]) -> float:
    """Return the largest value."""
    if not values:
        raise ValueError("values must not be empty.")
    largest = values[0]
    for v in values:
        if v > largest:
            largest = v
    return largest


def value_range(values: list[float]) -> float:
    """Return the difference between maximum and minimum."""
    return maximum(values) - minimum(values)
