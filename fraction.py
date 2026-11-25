"""A module for the fraction class"""

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
        """Checks if two fractions are equal by cross-multiplying."""
        if not isinstance(other, Fraction):
            return NotImplemented
        return self._num * other._den == self._den * other._num


    def __ne__(self, other):
        """Checks if two fractions are not equal by cross-multiplying."""
        if not isinstance(other, Fraction):
            return NotImplemented
        return self._num * other._den != self._den * other._num


    def __lt__(self, other):
        """Checks if this fraction is less than another fraction by cross-multiplying."""
        if not isinstance(other, Fraction):
            return NotImplemented
        return self._num * other._den < self._den * other._num


    def __le__(self, other):
        """Checks if this fraction is less than or equal to another fraction by cross-multiplying."""
        if not isinstance(other, Fraction):
            return NotImplemented
        return self._num * other._den <= self._den * other._num


    def __gt__(self, other):
        """Checks if this fraction is greater than another fraction by cross-multiplying."""
        if not isinstance(other, Fraction):
            return NotImplemented
        return self._num * other._den > self._den * other._num


    def __ge__(self, other):
        """Checks if this fraction is greater than or equal to another fraction by cross-multiplying."""
        if not isinstance(other, Fraction):
            return NotImplemented
        return self._num * other._den >= self._den * other._num

    # -- arithmetic operators --
    def __add__(self, other):
        """Adds two fractions by cross-multiplying and returns a new Fraction object."""
        if not isinstance(other, Fraction):
            return NotImplemented
        return Fraction(self._num * other._den + self._den * other._num, 
                        self._den * other._den)


    def __sub__(self, other):
        """Subtracts two fractions by cross-multiplying and returns a new Fraction object."""
        if not isinstance(other, Fraction):
            return NotImplemented
        return Fraction(self._num * other._den - self._den * other._num, 
                        self._den * other._den)

    # -- text representation --
    def __str__(self):
        """Returns a string representation of the fraction in the form 'numerator/denominator'"""
        return f"{self._num}/{self._den}"


    def __repr__(self):
        """Returns a string representation of the fraction for debugging"""
        return f"Fraction({self._num}, {self._den})"