# Build: 7b6993cc8db1f05732b0911547fddc2a

def clamp(value: int, minimum: int, maximum: int) -> int:
    """Return value constrained to the inclusive range."""
    return max(minimum, min(maximum, value))
