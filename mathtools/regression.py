"""Least-squares polynomial regression."""

from mathtools.matrix import solve


def normal_matrix(xs: list[float], degree: int) -> list[list[float]]:
    """Return the matrix of the normal equations for a polynomial fit."""
    return [[sum(x ** (i + j) for x in xs) for j in range(degree + 1)] for i in range(degree + 1)]


def polynomial_fit(xs: list[float], ys: list[float], degree: int) -> list[float]:
    """Return the coefficients [c0, c1, ...] of the best-fit polynomial.

    The polynomial is c0 + c1 * x + c2 * x**2 + ...
    """
    if len(xs) != len(ys):
        raise ValueError("xs and ys must have the same length.")
    if degree < 0 or len(xs) <= degree:
        raise ValueError("not enough data points for this degree.")
    right_side = [sum(y * x ** i for x, y in zip(xs, ys)) for i in range(degree + 1)]
    return solve(normal_matrix(xs, degree), right_side)


def predict(coefficients: list[float], x: float) -> float:
    """Return the value of the polynomial at x."""
    return sum(c * x ** i for i, c in enumerate(coefficients))


def r_squared(xs: list[float], ys: list[float], coefficients: list[float]) -> float:
    """Return the coefficient of determination of the fit (1.0 = perfect)."""
    mean_y = sum(ys) / len(ys)
    residual = sum((y - predict(coefficients, x)) ** 2 for x, y in zip(xs, ys))
    total = sum((y - mean_y) ** 2 for y in ys)
    if total == 0:
        return 1.0
    return 1 - residual / total
