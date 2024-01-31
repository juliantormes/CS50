import pytest
from twttr import shorten  # Assuming your main script is named twttr.py

def test_regular_word():
    assert shorten("hello") == "hll", "Failed to remove vowels from a regular word"

def test_empty_string():
    assert shorten("") == "", "Failed with an empty string"

def test_all_vowels():
    assert shorten("aeiouAEIOU") == "", "Failed to remove all vowels"

def test_no_vowels():
    assert shorten("rhythm") == "rhythm", "Altered a word with no vowels"

def test_mixed_case():
    assert shorten("HelloWorld") == "HllWrld", "Failed with mixed case"

def test_special_characters():
    assert shorten("h3ll0!#") == "h3ll0!#", "Altered non-vowel characters"

def test_spaces():
    assert shorten("hello world") == "hll wrld", "Failed to handle spaces"
