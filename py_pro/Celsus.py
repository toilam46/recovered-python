'''
Use @property decorator to create property for the Celsus class.
'''
class Celsus:
    def __init__(self, temp: float):
        self.temperature = temp

    @property
    def temperature(self) -> float:
        return self._temp

    @temperature.setter
    def temperature(self, value: float):
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero (-273.15°C).")
        self._temp = value


'''
Use pytest to test the Celsus class instead of unittest. So compare the test_Celsus.py file with the Celsus.py file and write test cases for the Celsus class using pytest.
if __name__ == "__main__":
    c = Celsus(25.0)
    print(c.temperature)

    c.temperature = 30.0
    print(c.temperature)
'''