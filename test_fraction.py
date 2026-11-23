"""A module for testing the Fraction class"""

import pytest

from fraction import Fraction


def test_equality():
    assert Fraction(1, 2) == Fraction(2, 4)
    assert Fraction(3, 4) != Fraction(2, 3)


def test_ordering():
    assert Fraction(1, 2) < Fraction(2, 3)
    assert Fraction(3, 4) > Fraction(1, 2)
    assert Fraction(1, 2) <= Fraction(1, 2)
    assert Fraction(3, 4) >= Fraction(1, 2)


def test_addition():
    assert Fraction(1, 2) + Fraction(1, 3) == Fraction(5, 6)
    assert Fraction(2, 5) + Fraction(3, 10) == Fraction(7, 10)


def test_subtraction():
    assert Fraction(3, 4) - Fraction(1, 2) == Fraction(1, 4)
    assert Fraction(5, 6) - Fraction(1, 3) == Fraction(1, 2)


def test_negative_denominator():
    with pytest.raises(ValueError):
        Fraction(1, -2)


def test_zero_denominator():
    with pytest.raises(ValueError):
        Fraction(1, 0)


def test_non_integer_input():
    with pytest.raises(TypeError):
        Fraction(1.5, 2)


def test_string_output():
    assert str(Fraction(1, 2)) == "1/2"
    assert str(Fraction(3, 4)) == "3/4"


def test_repr_output():
    assert repr(Fraction(1, 2)) == "Fraction(1, 2)"
    assert repr(Fraction(3, 4)) == "Fraction(3, 4)"

