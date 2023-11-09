"""Tests my zip function."""

__author__ = "730684472"

from zip import zip


def test_lists_are_equal() -> None:
    """Makes sure zip input lists are even."""
    assert zip(["milk"], [1, 2]) == {}


def test_milk_and_honey() -> None:
    """Makes sure when zip gets milk and honey it returns the correct values."""
    assert zip(["milk", "honey"], [1, 2]) == {'milk': 1, 'honey': 2}


def test_milk_honey_water() -> None:
    """Makes sure when zip gets milk, honey, and water it returns correct values."""
    assert zip(["milk", "honey", "water"], [1, 2, 3]) == {'milk': 1, 'honey': 2, 'water': 3}