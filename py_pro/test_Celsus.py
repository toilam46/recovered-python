'''
Write test_Celsus1.py to test the Celsus class using pytest.
'''

import pytest
from Celsus import Celsus

def test_celsus_initialization():
    c = Celsus(25.0)
    assert c.temperature == 25.0

def test_celsus_temperature_setter():
    c = Celsus(25.0)
    c.temperature = -270.0
    assert c.temperature == -270.0

def test_celsus_temperature_setter_below_absolute_zero():
    c = Celsus(25.0)
    with pytest.raises(ValueError):
        c.temperature = -274.15
