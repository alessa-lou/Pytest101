from calculator import Calculator

def test_add():
    calculator = Calculator()
    result = calculator.add(2, 3)

    assert result == 5

def test_subtract():
    calculator = Calculator()
    result = calculator.subtract(5, 1)
    
    assert result == 4

def test_multiply():
    calculator = Calculator()
    result = calculator.multiply(2, 3)

    assert result == 6