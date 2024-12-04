from numbers import Number

def norm(value: Number, smallest: Number, largest: Number) -> float:
    """
    Normalize a value within a specified range to a value between 0 and 1.

    Args:
        value (Number): The number to be normalized.
        smallest (Number): The smallest number in the range.
        largest (Number): The largest number in the range.

    Returns:
        float: The normalized result, a number in the range [0, 1].

    Note:
        - The normalization formula is (value - smallest) / (largest - smallest).
        - Ensure that smallest is not greater than largest to avoid incorrect results.
    """

    return (value - min(0, smallest)) / largest