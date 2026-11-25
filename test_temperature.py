"""A module for testing the temperature class"""

import pytest
from temperature import Temperature


class TestTemperature:
    """Functionality-testing the Temperature-class"""

    @pytest.mark.parametrize("x, expected", [
        [(2.3, "K"), (2.3, "K")],
        [(4, "f"), (4.0, "F")],
        [("3"), (3.0, "C")]])
    def test_init(self, x: tuple[float | int, str], expected: tuple[float | int | str, str]) -> None:
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

    def test_validation(self):
        """Test if the class throws an error if it passed an invalid input"""
        with pytest.raises(ValueError):
            Temperature(1.0, "o")   # Test invalid unit
            Temperature(-1.0, "K")  # Below absolute zero
            Temperature(-274, "C")  # Below absolute zero
            Temperature(-460, "F")  # Below absolute zero

    @pytest.mark.parametrize("c, f, k", [
        [(-273.15, "C"), (-459.67, "F"), (0, "K")],
        [(-40, "C"), (-40, "F"), (233.15, "K")],
        [(0, "C"), (32, "F"), (273.15, "K")],
        [(37, "C"), (98.6, "F"), (310.15, "K")],
        [(100, "C"), (212, "F"), (373.15, "K")]])
    def test_conversion(self,
        c: tuple[float | int, str],
        f: tuple[float | int, str],
        k: tuple[float | int, str]) -> None:
        """Test several conversions between different measurements of the same temperature"""
        for t in [c, f, k]:
            # Gpes through every combination
            c_temp = Temperature(c[0], c[1])
            f_temp = Temperature(f[0], f[1])
            k_temp = Temperature(k[0], k[1])
            t_temp = Temperature(t[0], t[1])
            assert (
                pytest.approx((c_temp.convert_to(t[1])).value, c_temp.tol)
                == pytest.approx(t_temp.value, t_temp.tol)
            )
            assert (
                pytest.approx((f_temp.convert_to(t[1])).value, f_temp.tol)
                == pytest.approx(t_temp.value, t_temp.tol)
            )
            assert (
                pytest.approx((k_temp.convert_to(t[1])).value, k_temp.tol)
                == pytest.approx(t_temp.value, t_temp.tol)
            )
        del c_temp, f_temp, k_temp, t_temp

    def test_round_trip(self):
        """Checks if a temperature can keep (more or less) the same temperature if its converted over and over"""
        t = Temperature(30.0, "C")
        for unit in ["F", "K", "C"]:
            t.convert_to(unit)
        assert pytest.approx(t.value, t.tol) == Temperature(30.0, "C").value

    def comparison(self):
        """Does cross-unit comparison to test logical methods"""
        assert Temperature(0, "C").__eq__(Temperature(32, "F"))         # ==
        assert Temperature(0, "C").__ne__(Temperature(-40, "F"))        # !=
        assert Temperature(0, "C").__gt__(Temperature(233.15, "K"))     # >
        assert Temperature(32, "F").__ge__(Temperature(0, "C"))         # >= (==)
        assert Temperature(0, "C").__ge__(Temperature(2, "K"))          # >= (>)
        assert Temperature(0, "C").__lt__(Temperature(98.6, "F"))       # <
        assert Temperature(273.15, "K").__le__(Temperature(32, "F"))    # <= (==)
        assert Temperature(0, "C").__le__(Temperature(373.15, "K"))     # <= (<)

    def format(self):
        """Testing formatting output of Temperaure"""
        assert str(Temperature(20.0, "K")) == "20.00°K"
        assert str(Temperature(137.84, "F")) == "137.84°F"
        assert str(Temperature(-28.178, "C")) == "-28.18°C"
        assert repr(Temperature(45.0, "C")) == "<Temperature(45.00, 'C')>"
        assert repr(Temperature(1.008, "K")) == "<Temperature(1.01, 'K')>"
        assert repr(Temperature(78, "F")) == "<Temperature(78.00, 'F')>"
