"""main.py"""

from typing import Iterable


def sum_even_numbers(numbers: Iterable[int]) -> int:
    """Sum even numbers

    Args:
        numbers (Iterative[int]): And iterative of ints

    Returns:
        int: The sum of ints
    """
    return sum(num for num in numbers if num % 2 == 0)
