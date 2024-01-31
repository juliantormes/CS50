import pytest
from numb3rs import validate

def test_false ():
    assert validate ("256.255.255.1") == False
    assert validate ("Cat") == False
    assert validate("") == False
    assert validate("192.168.1.1!") == False
    assert validate("abc.def.ghi.jkl") == False
    assert validate("123.456.789.000,") == False
    assert validate("19216811") == False
    assert validate("19216811") == False
    assert validate("192.168.1.1.1") == False
    assert validate("1.2.3.4.5") == False
    assert validate(" 192 .168.1.1") == False
    assert validate("192.168.1.1 ") == False
    assert validate("-192.168.1.1") == False
    assert validate("192.168.1.1/24") == False
    assert validate("192.168.1.1:8080") == False
    assert validate("192.168.0.256") == False
    assert validate("192.168") == False
    assert validate("10.0") == False
def test_true ():
    assert validate("0.0.0.0") == True
    assert validate("0.255.255.255") == True
    assert validate("255.0.255.255") == True
    assert validate("255.255.255.0") == True
    assert validate("001.001.001.001") == True
    assert validate("192.168.001.001") == True


