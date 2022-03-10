"""Utility functions."""

__author__ = "730324058"


def only_evens(num_list: list[int]) -> list[int]:
    """Given a list of integers, returns a list of only the even integers."""
    i: int = 0
    result_list: list[int] = []
    while i < len(num_list):
        if num_list[i] % 2 == 0:
            result_list.append(num_list[i])
        i += 1
    return result_list


def sub(num_list: list[int], start: int, end: int) -> list[int]:
    """Returns a subset of a given list."""
    if start < 0:
        start = 0
    if end > len(num_list):
        end = len(num_list)
    i: int = start
    result_list: list[int] = []
    while i < end:
        result_list.append(num_list[i])
        i += 1
    return result_list


def concat(first_list: list[int], second_list: list[int]) -> list[int]:
    """Concatenates two lists together."""
    i: int = 0
    result_list: list[int] = first_list
    while i < len(second_list):
        result_list.append(second_list[i])
        i += 1
    return result_list
