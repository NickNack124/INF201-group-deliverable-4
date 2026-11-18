"""A module for the class-definition of the Temperature class"""


class Temperature:
    """A representation of temperature, as well as a unit-conversion tool"""

    def __init__(self, value, unit) -> None:
        """
        Initialization of the class
        Args:
            * value (>= absolute zero): The measure of temperature
            * unit ("C" | "K" | "F"): The unit of measurement
        """

        self.tol = 1e-9
        # Checking for illegal attribute combinations
        abs_zero = {
            "K": 0.00,
            "C": -273.15,
            "F": -459.67
        }
        if unit.upper() in abs_zero.keys():
            if value < abs_zero[unit.upper()]:
                raise ValueError("Can't go below Absolute Zero")
        else:
            raise ValueError("Invalid unit")

        self._unit = unit
        self._value = value

    # Primary methods
    def to_celsius(self) -> float:
        """Conversion from Kelvin/Fahrenheit to Celsius"""
        conversion = {
            "C": self._value,
            "F": (self._value - 32) * (5 / 9),
            "K": self._value - 273.15
        }
        self._value = conversion[self.unit]
        self._unit = "C"
        return self._value

    def to_fahrenheit(self) -> float:
        """Conversion from Kelvin/Celsius to Fahrenheit"""
        conversion = {
            "C": (self._value * (9 / 5)) + 32,
            "F": self._value,
            "K": ((self._value - 273.15) * (9 / 5)) + 32
        }
        self._value = conversion[self.unit]
        self._unit = "F"
        return self._value

    def to_kelvin(self) -> float:
        """Conversion from Fahrenheit/Celsius to Kelvin"""
        conversion = {
            "C": self._value + 273.15,
            "F": ((self._value - 32) * (5 / 9)) + 273.15,
            "K": self._value
        }
        self._value = conversion[self.unit]
        self._unit = "K"
        return self._value

    def convert_to(self, target_unit: str) -> Temperature:
        """Converts from one temperature unit to another"""
        if target_unit.upper() == "K":
            value = self.to_kelvin()
        elif target_unit.upper() == "C":
            value = self.to_celsius()
        elif target_unit.upper() == "F":
            value = self.to_fahrenheit
        else:
            raise ValueError("Invalid unit")
        return Temperature(value, target_unit)

    # Logic
    def __eq__(self, other: Temperature) -> bool:
        """How self == other behaves"""
        if not isinstance(other, Temperature):
            return NotImplemented
        other_value = other.convert_to(self._unit).value
        return abs(self._value - other_value) <= self.tol

    def __ne__(self, other: Temperature) -> bool:
        """How self != other behaves"""
        if not isinstance(other, Temperature):
            return NotImplemented
        other_value = other.convert_to(self._unit).value
        return abs(self._value - other_value) > self.tol

    def __lt__(self, other: Temperature) -> bool:
        """How self < other behaves"""
        if not isinstance(other, Temperature):
            return NotImplemented
        other_value = other.convert_to(self._unit).value
        return self._value < (other_value - self.tol)

    def __le__(self, other: Temperature) -> bool:
        """How self <= other behaves"""
        if not isinstance(other, Temperature):
            return NotImplemented
        other_value = other.convert_to(self._unit).value
        return self._value <= (other_value + self.tol)

    def __gt__(self, other: Temperature) -> bool:
        """How self > other behaves"""
        if not isinstance(other, Temperature):
            return NotImplemented
        other_value = other.convert_to(self._unit).value
        return self._value > (other_value + self.tol)

    def __ge__(self, other: Temperature) -> bool:
        """How self >= other behaves"""
        if not isinstance(other, Temperature):
            return NotImplemented
        other_value = other.convert_to(self._unit).value
        return self._value >= (other_value - self.tol)

    # Representation
    def __repr__(self) -> str:
        """A representation of the object when it is ran with no call"""
        return f"Temperature({self._value:.2f}, '{self._unit}')"

    def __str__(self) -> str:
        """A string representation of the object when it is in a string"""
        return f"{self._value:.2f}°{self._unit}"

    # Properties
    @property
    def unit(self) -> str:
        """Read-only property of unit"""
        return self._unit

    @property
    def value(self) -> float:
        """Read-only property of value"""
        return self._value
