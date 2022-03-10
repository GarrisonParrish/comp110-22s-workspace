"""List utility functions."""

__author__ = "730324058"

from utils import only_evens, sub, concat


def test_only_evens_01() -> None:
    """Test only_evens."""
    assert only_evens([1, 2, 3]) == [2]


def test_only_evens_02() -> None:
    """Test only_evens."""
    assert only_evens([1, 5, 3]) == []


def test_only_evens_03() -> None:
    """Test only_evens."""
    assert only_evens([4, 4, 4]) == [4, 4, 4]


def test_sub_01() -> None:
    """Test sub."""
    assert sub([10, 20, 30, 40], 1, 3) == [20, 30]


def test_sub_02() -> None:
    """Test sub."""
    assert sub([1, 2], -1, 1) == [1]


def test_sub_03() -> None:
    """Test sub."""
    assert sub([], -12, 15) == []


def test_concat_01() -> None:
    """Test concat."""
    assert concat([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]


def test_concat_02() -> None:
    """Test concat."""
    assert concat([], [4, 5, 6]) == [4, 5, 6]


def test_concat_03() -> None:
    """Test concat."""
    assert concat([1, 2, 3], []) == [1, 2, 3]
