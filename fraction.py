"""A module for the fraction class"""


class Fraction:
    """A class representing fractions"""

    def __init__(self, numerator: int, denominator: int):
        """
        Makes a fraction with the given numerator and denominator.
        Args:
            * numerator (int): the number being divided
            * denominator (int): the number you are dividing by (> 0.0)
        """
        # We start by correcting certain values to integers
        try:
            # float and certain string values can be parsed as int, so we try to correct first
            numerator = int(round(float(numerator)))
            denominator = int(round(abs(float(denominator))))
        except ValueError as err:
            raise ValueError("Numerator and denominator must be integers.") from err
        else:
            if denominator <= 0:
                raise ValueError("Denominator must be a positive integer.")

        # We can then initialize our protected attributes
        self._num = numerator
        self._den = denominator

    # Logic methods
    def __eq__(self, other: object) -> bool:
        """Checks if two fractions are equal by cross-multiplying."""
        if not isinstance(other, Fraction):
            return NotImplemented

        return self._num * other._den == self._den * other._num

    def __ne__(self, other: object) -> bool:
        """Checks if two fractions are not equal by cross-multiplying."""
        if not isinstance(other, Fraction):
            return NotImplemented

        return self._num * other._den != self._den * other._num

    def __lt__(self, other: Fraction) -> bool:
        """Checks if this fraction is less than another fraction by cross-multiplying."""
        if not isinstance(other, Fraction):
            return NotImplemented

        return self._num * other._den < self._den * other._num

    def __le__(self, other: Fraction) -> bool:
        """Checks if this fraction is less than or equal to another fraction by cross-multiplying."""
        if not isinstance(other, Fraction):
            return NotImplemented
        return self._num * other._den <= self._den * other._num

    def __gt__(self, other: Fraction) -> bool:
        """Checks if this fraction is greater than another fraction by cross-multiplying."""
        if not isinstance(other, Fraction):
            return NotImplemented

        return self._num * other._den > self._den * other._num

    def __ge__(self, other: Fraction) -> bool:
        """Checks if this fraction is greater than or equal to another fraction by cross-multiplying."""
        if not isinstance(other, Fraction):
            return NotImplemented

        return self._num * other._den >= self._den * other._num

    # Mathematical methods
    def __add__(self, other: Fraction) -> Fraction:
        """Adds two fractions by cross-multiplying and returns a new Fraction object."""
        if not isinstance(other, Fraction):
            return NotImplemented

        return Fraction(
            self._num * other._den + self._den * other._num,
            self._den * other._den
        )

    def __sub__(self, other: Fraction) -> Fraction:
        """Subtracts two fractions by cross-multiplying and returns a new Fraction object."""
        if not isinstance(other, Fraction):
            return NotImplemented

        return Fraction(
            self._num * other._den - self._den * other._num,
            self._den * other._den
        )

    # Representation methods
    def __str__(self):
        """Returns a string representation of the fraction in the form 'numerator/denominator'"""
        return f"{self._num}/{self._den}"

    def __repr__(self):
        """Returns a string representation of the fraction for debugging"""
        return f"Fraction({self._num}, {self._den})"

    # Properties
    @property
    def num(self):
        """Read-only unit of numerator"""
        return self._num

    @property
    def den(self):
        """Read-only unit of denominator"""
        return self._den
