import pytest
from um import count

def test_basic_usage():
    assert count("hello, um, world") == 1

def test_case_insensitivity():
    assert count("Um, who are you? um, I am me.") == 2

def test_no_um():
    assert count("This sentence has no target word.") == 0

def test_um_in_word():
    assert count("The drummer played a rhythm.") == 0

def test_multiple_ums():
    assert count("um, this is um... kind of um... weird.") == 3
