"""Small, reusable numeric range utilities."""


def is_within_range(value, lower, upper):
    """Return whether value is inside the inclusive range."""
    if lower > upper:
        raise ValueError("lower must be less than or equal to upper")
    return lower <= value <= upper
