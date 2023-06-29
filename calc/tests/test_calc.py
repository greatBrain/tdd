import pytest
from calc import calc

#Testing the sum function:
def test_sum_func():
    suma = calc.sumar(8,2)
    assert suma == 10

def test_resta():
    resta = calc.restar(5,3)
    assert resta == 2
