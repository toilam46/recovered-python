from calculate import add, floor_divide, modulus, power, subtract, multiply, divide   
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
def test_subtract():    
    assert subtract(5, 2) == 3
    assert subtract(0, 5) == -5
    assert subtract(-1, -1) == 0
def test_multiply():    
    assert multiply(4, 5) == 20
    assert multiply(-2, 3) == -6
    assert multiply(0, 10) == 0
def test_divide():    
    assert divide(10, 2) == 5
    assert divide(5, 0) == "Error: Division by zero is not allowed."
    assert divide(-6, 3) == -2  
def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(-2, 4) == 16
def test_modulus():
    assert modulus(10, 3) == 1
    assert modulus(5, 0) == "Error: Modulus by zero is not allowed."
    assert modulus(-7, 4) == -3 
def test_floor_divide():
    assert floor_divide(10, 3) == 3
    assert floor_divide(5, 0) == "Error: Floor division by zero is not allowed."
    assert floor_divide(-7, 4) == -2
        
                                                                 