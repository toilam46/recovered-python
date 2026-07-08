from is_prime import is_prime
import pytest

# parameterize the test with different inputs and expected outputs
@pytest.mark.parametrize("n, expected", [
    (0, False),
    (1, False), 
    (2, True),
    (3, True),
    (4, False),
    (5, True),
    (10, False),
    (13, True),
    (17, True),
    (20, False)
])

# Before runnung "pytest filename", change dir, if needed, to the directory where the test file is located. In this case: ~/Python_CC++_C#/Python_programs
def test_is_prime(n, expected):
    assert is_prime(n) == expected  
