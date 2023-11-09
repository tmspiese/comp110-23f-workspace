"""3-different ways to do a sum."""


def w_sum(vals: list[float]) -> float:
    """Sum using while loop."""
    idx: int = 0
    output: float = 0
    while (idx < len(vals)):
        output = output + vals[idx]
        idx = idx + 1
    return output


def f_sum(vals: list[float]) -> float:
    """Sum using for loop."""
    output: float = 0
    for elem in vals:
        output = output + elem
    return output


def f_range_sum(vals: list[float]) -> float:
    """Sum using for loops with range."""
    output: float = 0
    for idx in range(0, len(vals)):
        output = output + vals[idx]
    return output
