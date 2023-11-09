"""Testing my sumation function"""

from lessons.sum_even import sum_evens_in_list

def test_empty_sum() -> None:
    """sum_evens_in_list of empty list should be 0"""
    assert sum_evens_in_list([]) == 0

def test_list_length_1() -> None:
    """testing on a list with one element"""
    test_list: list[int] = [2]
    assert sum_evens_in_list(test_list) == 2

def test_list_positives() -> None:
    """Testing sum on a list of positie integers"""
    test_list: list[int] = [1,2,3,4]
    assert sum_evens_in_list(test_list) == 6

def test_list_negs_and_pos() -> None:
    """Testing sum of negatives and positives"""
    test_list: list = [1, -2, 3, 4]
    assert sum_evens_in_list(test_list) == 2