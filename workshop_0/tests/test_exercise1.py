import exercise1
from math import pi

def test_add():
    sum = exercise1.add(2,3)
    assert sum == 5

def test_square():
    squared = exercise1.square(2)
    assert squared == 4

def test_area():
    circleArea = exercise1.area(5)
    assert circleArea == (pi*(5**2))

def test_calculateInterestRate():
    rate = exercise1.calculateInterestRate(100, 1000)
    assert rate == (100 / 1000) * 100

