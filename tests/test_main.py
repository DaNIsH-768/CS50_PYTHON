from main import square
import pytest

def test_positive():
    assert square(2) == 4
    assert square(11) == 121

def test_negative():
    assert square(-1) == 1
    assert square(-11) == 121

def test_zero():
    assert square(0) == 0