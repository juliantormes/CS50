import pytest
from bank import value
def test_hello():
    assert value("hello") == 0

def test_hello_uppercase():
    assert value("Hello") == 0

def test_hello_mixed_case():
    assert value("hElLo") == 0

def test_start_with_h():
    assert value("hi") == 20

def test_start_with_h_uppercase():
    assert value("Hi") == 20

def test_start_with_h_mixed_case():
    assert value("hI") == 20

def test_other():
    assert value("greetings") == 100

def test_empty_string():
    assert value("") == 100

def test_space_string():
    assert value(" ") == 100

def test_non_string_input():
    with pytest.raises(AttributeError):
        value(123)
