"""Test dictionary functions."""


__author__ = "730324058"


import pytest
from dictionary import invert, favorite_color, count


def test_invert_01() -> None:
    """Docstring!"""
    input_dict: dict[str, str] = {"hello": "goodbye", "morning": "night", "apples": "oranges"}
    assert invert(input_dict) == {"goodbye": "hello", "night": "morning", "oranges": "apples"}


def test_invert_02() -> None:
    """Docstring!"""
    with pytest.raises(KeyError):
        my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
        invert(my_dictionary)


def test_favorite_color_01() -> None:
    """Docstring!"""
    input_dict: dict[str, str] = {"marc": "red", "ezri": "yellow", "garrison": "red", "kris": "blue"}
    assert favorite_color(input_dict) == "red"


def test_count_01() -> None:
    """Docstring!"""
    input_list: list[str] = ["red", "yellow", "red", "blue"]
    assert count(input_list) == {"red": 2, "yellow": 1, "blue": 1}