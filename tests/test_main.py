""" test_main.py """
from src.main import sum_even_numbers, sum_odd_numbers


def test_sum_even_numbers() -> None:
    """Test sum even numbers"""
    # Test case 1: Basic case with even numbers
    assert sum_even_numbers([1, 2, 3, 4, 5, 6]) == 12

    # Test case 2: No even numbers
    assert sum_even_numbers([1, 3, 5, 7]) == 0

    # Test case 3: Empty list
    assert sum_even_numbers([]) == 0

    # Add more test cases as needed


def test_sum_even_numbers_coverage() -> None:
    """Test sum even numbers coverage"""
    # Additional test case to check coverage
    assert sum_even_numbers([2, 4, 6, 8]) == 20


def test_sum_odd_numbers() -> None:
    """Test sum odd numbers"""
    # Test case 1: Basic case with odd numbers
    assert sum_odd_numbers([1, 2, 3, 4, 5, 6]) == 9

    # Test case 2: No odd numbers
    assert sum_odd_numbers([2, 4, 6, 8]) == 0

    # Test case 3: Empty list
    assert sum_odd_numbers([]) == 0

    # Add more test cases as needed


def test_sum_odd_numbers_coverage() -> None:
    """Test sum odd numbers coverage"""
    # Additional test case to check coverage
    assert sum_odd_numbers([1, 3, 5, 7]) == 16
