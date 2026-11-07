"""Percentage calculations."""


def percent_of(percent: float, value: float) -> float:
    """Return `percent` % of `value`, e.g. percent_of(20, 50) -> 10."""
    return value * percent / 100


def percent_change(old: float, new: float) -> float:
    """Return the percentage change from old to new, e.g. 100 -> 120 = 20.0."""
    if old == 0:
        raise ValueError("old must not be 0.")
    return (new - old) / old * 100


def apply_discount(price: float, discount_percent: float) -> float:
    """Return the price after subtracting a discount in percent."""
    return price * (1 - discount_percent / 100)


def add_vat(net_price: float, vat_percent: float = 19) -> float:
    """Return the gross price incl. VAT (default: German 19 %)."""
    return net_price * (1 + vat_percent / 100)
