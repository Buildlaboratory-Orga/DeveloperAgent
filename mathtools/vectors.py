"""Operations on vectors represented as lists of numbers."""


def _check_same_length(a: list[float], b: list[float]) -> None:
    if len(a) != len(b):
        raise ValueError("Vectors must have the same length.")


def add_vectors(a: list[float], b: list[float]) -> list[float]:
    """Return the element-wise sum of two vectors."""
    _check_same_length(a, b)
    return [x + y for x, y in zip(a, b)]


def scale_vector(v: list[float], factor: float) -> list[float]:
    """Return the vector multiplied by a scalar."""
    return [x * factor for x in v]


def dot_product(a: list[float], b: list[float]) -> float:
    """Return the dot product of two vectors."""
    _check_same_length(a, b)
    return sum(x * y for x, y in zip(a, b))


def vector_length(v: list[float]) -> float:
    """Return the Euclidean length of a vector."""
    return sum(x * x for x in v) ** 0.5
