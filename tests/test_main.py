""" test_main.py """
from src.main import sum_even_numbers


def test_sum_even_numbers():
    """Test sum even numbers"""
    # Test case 1: Basic case with even numbers
    assert sum_even_numbers([1, 2, 3, 4, 5, 6]) == 12

    # Test case 2: No even numbers
    assert sum_even_numbers([1, 3, 5, 7]) == 0

    # Test case 3: Empty list
    assert sum_even_numbers([]) == 0

    # Add more test cases as needed


def test_sum_even_numbers_coverage():
    """Test sum even numbers coverage"""
    # Additional test case to check coverage
    assert sum_even_numbers([2, 4, 6, 8]) == 20
