"""A module for testing the temperature class"""

import pytest
from temperature import Temperature

#from deliverable_4_G4_2_answers.ipynb import Temperature

class TestTemperature:
    """Functionality-testing the Temperature-class"""

    @pytest.mark.parametrize("x, expected", [
        [(2.3, "K"), (2.3, "K")],
        [(4, "f"), (4.0, "F")],
        [("3"), (3.0, "C")]
    ])
    def test_init(self, x: tuple[float | int | str, str], expected: tuple[float | int | str, str]) -> None:
        """We test the class's ability to correct values, give a default unit, and its read-only behavior"""
        if len(x) == 1:
            # In this case, we get to see if the unit defaults to "C" or not
            temp = Temperature(x[0])
        else:
            temp = Temperature(x[0], x[1])
        # First we check if the values and units match what we expect
        assert (temp._value, temp._unit) == (expected[0], expected[1])
        # Then we check if the read-only values match as well (implying read == protected)
        assert (temp.value, temp.unit) == (expected[0], expected[1])

    #@pytest.mark.parametrize("x, expected", [
        #[(2.3, "K"), (2.3, "K")],
        #[(4, "f"), (4.0, "F")],
        #[("3"), (3.0, "C")]
    #])
    def test_validation(x, expected):

"""
    def test_conversion():

    def test_round_trip():

    def test_comparison():

    def test_formatting():

"""
