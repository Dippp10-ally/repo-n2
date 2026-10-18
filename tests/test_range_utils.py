import pytest

from src.range_utils import is_within_range


def test_includes_lower_boundary():
    assert is_within_range(1, 1, 5)


def test_includes_upper_boundary():
    assert is_within_range(5, 1, 5)


def test_includes_middle_value():
    assert is_within_range(3, 1, 5)


def test_excludes_values_outside_range():
    assert not is_within_range(0, 1, 5)
    assert not is_within_range(6, 1, 5)


def test_rejects_reversed_range():
    with pytest.raises(ValueError):
        is_within_range(3, 5, 1)
