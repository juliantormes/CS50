import pytest
from working import convert


def test_valid_input():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    # Add more valid test cases

def test_valid_input_without_minutes():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    # Add more valid test cases without minutes

def test_invalid_format():
    with pytest.raises(ValueError):
        convert("9 to 5 PM")
    # Add more invalid format test cases

def test_invalid_time():
    with pytest.raises(ValueError):
        convert("13:00 PM to 2:00 PM")
    # Add more invalid time test cases
    
def test_ommited_to():
    with pytest.raises(ValueError):
        convert("13:00 2:00 PM")

