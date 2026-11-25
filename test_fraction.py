"""A module for testing the Fraction class"""

import pytest

from fraction import Fraction


def test_equality():
    """Tests the equality and inequality operators for the Fraction class."""
    assert Fraction(1, 2) == Fraction(2, 4)
    assert Fraction(3, 4) != Fraction(2, 3)


def test_ordering():
    """Tests the ordering operators for the Fraction class."""
    assert Fraction(1, 2) < Fraction(2, 3)
    assert Fraction(3, 4) > Fraction(1, 2)
    assert Fraction(1, 2) <= Fraction(1, 2)
    assert Fraction(3, 4) >= Fraction(1, 2)


def test_addition():
    """Tests the addition operator for the Fraction class."""
    assert Fraction(1, 2) + Fraction(1, 3) == Fraction(5, 6)
    assert Fraction(2, 5) + Fraction(3, 10) == Fraction(7, 10)


def test_subtraction():
    """Tests the subtraction operator for the Fraction class."""
    assert Fraction(3, 4) - Fraction(1, 2) == Fraction(1, 4)
    assert Fraction(5, 6) - Fraction(1, 3) == Fraction(1, 2)


def test_negative_denominator():
    """Tests the handling of negative denominators."""
    with pytest.raises(ValueError):
        Fraction(1, -2)


def test_zero_denominator():
    """Tests the handling of zero denominators."""
    with pytest.raises(ValueError):
        Fraction(1, 0)


def test_non_integer_input():
    """Tests the handling of non-integer inputs."""
    with pytest.raises(TypeError):
        Fraction(1.5, 2)


def test_string_output():
    """Tests the string representation of the Fraction class."""
    assert str(Fraction(1, 2)) == "1/2"
    assert str(Fraction(3, 4)) == "3/4"


def test_repr_output():
    """Tests the repr representation of the Fraction class."""
    assert repr(Fraction(1, 2)) == "Fraction(1, 2)"
    assert repr(Fraction(3, 4)) == "Fraction(3, 4)"


def test_comparison_with_non_fraction():
    """Tests the comparison operators with non-Fraction types."""
    assert (Fraction(1, 2) == 0.5) is False
    assert (Fraction(1, 2) != 0.5) is True