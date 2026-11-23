"""A module for testing the Fraction class"""

#import pytest

#from deliverable_4_G4_2_answers.ipynb import Fraction

class Fraction:
    def __init__(self, numerator, denominator=1):
        """Makes a fraction with the given numerator and denominator. The denominator must be a positive integer."""
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError("Numerator and denominator must be integers.")
        if denominator <= 0:
            raise ValueError("Denominator must be a positive integer.")
        self._num = numerator
        self._den = denominator

    # -- comparison operators --
    def __eq__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return self._num * other._den == self._den * other._num


    def __ne__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return self._num * other._den != self._den * other._num


    def __lt__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return self._num * other._den < self._den * other._num


    def __le__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return self._num * other._den <= self._den * other._num


    def __gt__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return self._num * other._den > self._den * other._num


    def __ge__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return self._num * other._den >= self._den * other._num

    # -- arithmetic operators --
    def __add__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return Fraction(self._num * other._den + self._den * other._num, 
                        self._den * other._den)


    def __sub__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return Fraction(self._num * other._den - self._den * other._num, 
                        self._den * other._den)

    # -- text representation --
    def __str__(self):
        return f"{self._num}/{self._den}"


    def __repr__(self):
        return f"Fraction({self._num}, {self._den})"