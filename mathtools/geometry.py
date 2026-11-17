"""Areas and perimeters of simple shapes."""

import math


def rectangle_area(width: float, height: float) -> float:
    """Return the area of a rectangle."""
    return width * height


def rectangle_perimeter(width: float, height: float) -> float:
    """Return the perimeter of a rectangle."""
    return 2 * (width + height)


def triangle_area(base: float, height: float) -> float:
    """Return the area of a triangle."""
    return base * height / 2


def circle_area(radius: float) -> float:
    """Return the area of a circle."""
    return math.pi * radius ** 2


def circle_circumference(radius: float) -> float:
    """Return the circumference of a circle."""
    return 2 * math.pi * radius
