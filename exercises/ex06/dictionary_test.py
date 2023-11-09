"""Testing dictionary.py functions."""

__author__ = "730684472"

import pytest

from exercises.ex06.dictionary import invert, favorite_color, count, alphabetizer, update_attendance


def test_invert_uc_1() -> None:
    """Tests first use case for invert."""
    assert invert({"a": "b", "c": "d"}) == {'b': 'a', 'd': 'c'}


def test_invert_uc_2() -> None:
    """Tests second use case for invert."""
    assert invert({"a": "z", "b": "x", "c": "y", "d": "w"}) == {'z': 'a', 'x': 'b', 'y': 'c', 'w': 'd'}


def test_invert_ec_1() -> None:
    """Tests first edge case for invert."""
    with pytest.raises(KeyError):
        invert({"a": "z", "b": "y", "c": "z"}) 


def test_favorite_color_uc_1() -> None:
    """Tests first use case for favorite color."""
    assert favorite_color({"mike": "yellow", "tom": "Purple", "chris": "purple"}) == 'purple'


def test_favorite_color_uc_2() -> None:
    """Tests second use case for favorite color."""
    assert favorite_color({"mike": "yellow", "tom": "Purple", "chris": "purple", "john": "red", "sam": "red", "jimmy": "red"}) == 'red' 


def test_favorite_color_ec_1() -> None:
    """Tests first edge case for favorite color."""
    assert favorite_color({"mike": "yellow", "tom": "Purple", "chris": "17", "john": "none", "sam": "red", "jimmy": "4"}) == 'yellow'


def test_count_uc_1() -> None:
    """Tests first use case for count."""
    assert count(["hi", "hello", "hi", "be gone"]) == {'hi': 2, 'hello': 1, 'be gone': 1}


def test_count_uc_2() -> None:
    """Tests second use case for count."""
    assert count(["hi", "hello", "hi", "get out of my face", "get out of my face", "shut up"]) == {'hi': 2, 'hello': 1, 'get out of my face': 2, 'shut up': 1}


def test_count_ec_1() -> None:
    """Tests first edge case for count."""
    assert count(["hi", "hello", "hi", "-_-", "get out of my face", "-_-"]) == {'hi': 2, 'hello': 1, '-_-': 2, 'get out of my face': 1}


def test_alphabetizer_uc_1() -> None:
    """Tests first use case for alphabetizer."""
    assert alphabetizer(["apple", "gym", "food", "meal", "pizza", "prize", "face pulls"]) == {'a': ['apple'], 'g': ['gym'], 'f': ['food', 'face pulls'], 'm': ['meal'], 'p': ['pizza', 'prize']}


def test_alphabetizer_uc_2() -> None:
    """Tests second use case for alphabetizer."""
    assert alphabetizer(["pizza", "price", "prize", "place", "ace", "apple", "ape"]) == {'p': ['pizza', 'price', 'prize', 'place'], 'a': ['ace', 'apple', 'ape']}


def test_alphabetizer_ec_1() -> None:
    """Tests first edge case for alphabetizer."""
    with pytest.raises(AttributeError):
        alphabetizer([7, "hello", 15]) 


def test_update_attendance_uc_1() -> None:
    """Tests first use case for update_attendance."""
    attendance = {"Monday": ["mike", "john"], "Tuesday": ["john"]}
    assert update_attendance(attendance, "Tuesday", "tom") == {'Monday': ['mike', 'john'], 'Tuesday': ['john', 'tom']}


def test_update_attendance_uc_2() -> None:
    """Tests second use case for update_attendance."""
    attendance = {"Monday": ["tom", "sam"], "Wednesday": ["tom", "meg"]}
    update_attendance(attendance, "Wednesday", "sam")
    update_attendance(attendance, "Friday", "tom")
    assert update_attendance(attendance, "Friday", "sam") == {'Monday': ['tom', 'sam'], 'Wednesday': ['tom', 'meg', 'sam'], 'Friday': ['tom', 'sam']}


def test_update_attendance_ec_1() -> None:
    """Tests first edge case for update_attendance."""
    attendance = {"Monday": ["tom", "sam"], "Wednesday": ["tom", "meg"]}
    update_attendance(attendance, "Wednesday", "sam")
    update_attendance(attendance, "Friday", "tom")
    update_attendance(attendance, "Friday", ["jim", "sally"]) == {'Monday': ['tom', 'sam'], 'Wednesday': ['tom', 'meg', 'sam'], 'Friday': ['tom', 'sam', ['jim', 'sally']]}