import pytest
from plates import is_valid

def test_valid_plates():
    assert is_valid("AB1234")
    assert is_valid("XY12")
    assert is_valid("GH90")

def test_length_constraints():
    assert not is_valid("A")  # Too short
    assert not is_valid("ABCDEFG")  # Too long
    
def test_starting_characters():
    assert not is_valid("1AB234")  # Starts with a number
    assert not is_valid("4XYZ")    # Starts with a number
    assert not is_valid("A1234")   # Starts with only one letter
    assert not is_valid("9X345")   # Starts with a number
    assert is_valid("AB123")       # Correctly formatted plate


def test_invalid_characters():
    assert not is_valid("AB 123")
    assert not is_valid("AB-12")
    assert not is_valid("AB@34")

def test_number_placement_and_formatting():
    assert not is_valid("A1B234")  # Number in the middle
    assert not is_valid("AB0123")  # Starts with '0'
    assert not is_valid("AB12A3")  # Letter after number

def test_case_insensitivity():
    assert is_valid("ab1234")
    assert not is_valid("aB1C")

# Run the tests
if __name__ == "__main__":
    pytest.main()
