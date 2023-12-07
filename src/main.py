from typing import Iterable

import os

def sum_even_numbers(numbers):
    return sum(
        num for num in numbers
        if num % 2 == 0
    )