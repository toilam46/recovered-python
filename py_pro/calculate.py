class Calculator:
    """A simple calculator class for basic arithmetic operations."""

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b

    def power(self, a, b):
        return a ** b

    def modulus(self, a, b):
        if b == 0:
            raise ValueError("Modulus by zero is not allowed.")
        return a % b

    def floor_divide(self, a, b):
        if b == 0:
            raise ValueError("Floor division by zero is not allowed.")
        return a // b


calculator = Calculator()


def add(a, b):
    return calculator.add(a, b)


def subtract(a, b):
    return calculator.subtract(a, b)


def multiply(a, b):
    return calculator.multiply(a, b)


def divide(a, b):
    return calculator.divide(a, b)


def power(a, b):
    return calculator.power(a, b)


def modulus(a, b):
    return calculator.modulus(a, b)


def floor_divide(a, b):
    return calculator.floor_divide(a, b)


def _parse_args():
    import argparse

    parser = argparse.ArgumentParser(description="Simple calculator")
    parser.add_argument("operation", choices=["add", "subtract", "multiply", "divide", "power", "modulus", "floor_divide"], help="Operation to perform")
    parser.add_argument("a", type=float, help="First operand")
    parser.add_argument("b", type=float, help="Second operand")
    return parser.parse_args()


if __name__ == "__main__":
    args = _parse_args()
    ops = {
        "add": calculator.add,
        "subtract": calculator.subtract,
        "multiply": calculator.multiply,
        "divide": calculator.divide,
        "power": calculator.power,
        "modulus": calculator.modulus,
        "floor_divide": calculator.floor_divide,
    }

    try:
        result = ops[args.operation](args.a, args.b)
    except ValueError as exc:
        print(f"Error: {exc}")
    else:
        print(result)
