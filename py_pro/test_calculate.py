import pytest

from calculate import Calculator


@pytest.fixture
def cal():
    return Calculator()


def test_add(cal):
    assert cal.add(2, 3) == 5
    assert cal.add(-1, 1) == 0
    assert cal.add(0, 0) == 0


def test_subtract(cal):
    assert cal.subtract(5, 2) == 3
    assert cal.subtract(0, 5) == -5
    assert cal.subtract(-1, -1) == 0


def test_multiply(cal):
    assert cal.multiply(4, 5) == 20
    assert cal.multiply(-2, 3) == -6
    assert cal.multiply(0, 10) == 0


def test_divide(cal):
    assert cal.divide(10, 2) == 5
    assert cal.divide(-6, 3) == -2
    with pytest.raises(ValueError, match="Division by zero"):
        cal.divide(5, 0)


def test_power(cal):
    assert cal.power(2, 3) == 8
    assert cal.power(5, 0) == 1
    assert cal.power(-2, 4) == 16


def test_modulus(cal):
    assert cal.modulus(10, 3) == 1
    assert cal.modulus(7, 4) == 3
    with pytest.raises(ValueError, match="Modulus by zero"):
        cal.modulus(5, 0)


def test_floor_divide(cal):
    assert cal.floor_divide(10, 3) == 3
    assert cal.floor_divide(-7, 4) == -2
    with pytest.raises(ValueError, match="Floor division by zero"):
        cal.floor_divide(5, 0)

        
                                                                 