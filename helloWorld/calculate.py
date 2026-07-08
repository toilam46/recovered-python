def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b
def power(a, b):    return a ** b
def modulus(a, b):
    if b == 0:
        return "Error: Modulus by zero is not allowed."
    return a - int(a / b) * b
def floor_divide(a, b):
    if b == 0:
        return "Error: Floor division by zero is not allowed."
    return a // b