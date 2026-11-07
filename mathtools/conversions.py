"""Unit conversions."""


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert degrees Celsius to Fahrenheit."""
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert degrees Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9


def km_to_miles(km: float) -> float:
    """Convert kilometres to miles."""
    return km / 1.609344


def miles_to_km(miles: float) -> float:
    """Convert miles to kilometres."""
    return miles * 1.609344
