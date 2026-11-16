"""Trend report: choose the best polynomial trend and forecast the next value."""

from mathtools.matrix import determinant
from mathtools.regression import normal_matrix, polynomial_fit, predict, r_squared


def is_stable(xs: list[float], degree: int) -> bool:
    """Return True if a fit of this degree is numerically well defined.

    The normal matrix of a well-defined fit has a positive determinant.
    """
    return determinant(normal_matrix(xs, degree)) > 0


def trend_report(xs: list[float], ys: list[float], next_x: float, max_degree: int = 2) -> dict:
    """Fit polynomials up to max_degree and report the best stable one.

    Returns a dict with the keys degree, coefficients, r_squared and forecast.
    Raises ValueError if no stable fit exists.
    """
    best = None
    for degree in range(1, max_degree + 1):
        if len(xs) <= degree or not is_stable(xs, degree):
            continue
        coefficients = polynomial_fit(xs, ys, degree)
        quality = r_squared(xs, ys, coefficients)
        if best is None or quality > best["r_squared"] + 1e-9:
            best = {
                "degree": degree,
                "coefficients": coefficients,
                "r_squared": quality,
                "forecast": predict(coefficients, next_x),
            }
    if best is None:
        raise ValueError("no stable fit found.")
    return best
