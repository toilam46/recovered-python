'''
Unit tests for the Celsus class.
These tests use pytest to verify the behavior of the Celsus class, including initialization, temperature setting, and validation against absolute zero.
execute: pytest -q test_Celsus1.py
with -q: pytest usually shows only a compact result summary
'''
import pytest

from Celsus import Celsus


def test_initial_temperature_is_stored():
    c = Celsus(25.0)
    assert c.temperature == 25.0


def test_temperature_can_be_updated_to_a_valid_value():
    c = Celsus(25.0)
    c.temperature = -270.0
    assert c.temperature == -270.0


def test_temperature_cannot_be_below_absolute_zero():
    c = Celsus(25.0)
    with pytest.raises(ValueError, match="absolute zero"):
        c.temperature = -274.15


def test_temperature_can_be_equal_to_absolute_zero():
    c = Celsus(25.0)
    c.temperature = -273.15
    assert c.temperature == -273.15


def test_temperature_can_be_zero():
    c = Celsus(25.0)
    c.temperature = 0.0
    assert c.temperature == 0.0


def test_temperature_can_be_set_to_a_positive_value():
    c = Celsus(25.0)
    c.temperature = 100.0
    assert c.temperature == 100.0


