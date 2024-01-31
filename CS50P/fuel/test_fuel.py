import pytest
from fuel import convert, gauge

# Tests for convert function
def test_convert_valid_fraction():
    assert convert("1/2") == 50.0

def test_convert_numerator_greater_than_denominator():
    with pytest.raises(ValueError):
        convert("3/2")

def test_convert_zero_denominator():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

# Tests for gauge function
def test_gauge_empty():
    assert gauge(1) == "E"

def test_gauge_full():
    assert gauge(99) == "F"

def test_gauge_normal():
    assert gauge(50) == "50%"
