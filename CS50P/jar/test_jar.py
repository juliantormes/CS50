import pytest
from jar import Jar

def test_initialization():
    jar = Jar(10)
    assert jar.capacity == 10
    assert jar.size == 0
    with pytest.raises(ValueError):
        Jar(-1)
    with pytest.raises(ValueError):
        Jar("10")

def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5
    with pytest.raises(ValueError):
        jar.deposit(8)
    with pytest.raises(ValueError):
        jar.deposit(-1)

def test_withdraw():
    jar = Jar(20)
    jar.deposit(10)
    jar.withdraw(5)
    assert jar.size == 5
    with pytest.raises(ValueError):
        jar.withdraw(6)
    with pytest.raises(ValueError):
        jar.withdraw(-1)

def test_str_representation():
    jar = Jar()
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"

def test_capacity_and_size_properties():
    jar = Jar(5)
    assert jar.capacity == 5
    jar.deposit(2)
    assert jar.size == 2
    jar.withdraw(1)
    assert jar.size == 1
