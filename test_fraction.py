"""A module for testing the Fraction class"""

import pytest

from fraction import Fraction

def test_comparisons():
    assert Fraction(1, 2) == Fraction(2, 4)
    assert Fraction(1, 3) <= Fraction(1, 2)
    assert Fraction(3, 4) >= Fraction(2, 3)


def test_addition():
    assert Fraction(1, 2) + Fraction(1, 3) == Fraction(5, 6)
    assert Fraction(2, 5) + Fraction(3, 10) == Fraction(7, 10)



