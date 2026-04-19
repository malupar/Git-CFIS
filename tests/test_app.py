from src.app import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(0, 5) == -5

def test_multiply():
    assert multiply(10, 5) == 50
    assert multiply(0, 5) == 0
    assert multiply(-1, -1) == 1
    assert multiply(-1, 5) == -5

def test_divide():
    assert divide(10, 5) == 2
    assert divide(20, 3) == 6
    assert divide(-1, -1) == 1
    assert divide(-1, 5) == 0