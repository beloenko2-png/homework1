import pytest
from string_utils import StringUtils 

utils = StringUtils()

# Тесты для capitalize
@pytest.mark.parametrize("input_str, expected_output", [
    ("skypro", "Skypro"),
    ("123", "123"),
    ("", ""),
    ("Skypro", "Skypro")
])
def test_capitalize(input_str, expected_output):
    assert utils.capitalize(input_str) == expected_output


# Тесты для trim
@pytest.mark.parametrize("input_str, expected_output", [
    ("   skypro", "skypro"),
    ("skypro", "skypro"),
    ("   sky pro  ", "sky pro  "),
    (" ", ""),
    ])

def test_trim(input_str, expected_output):
    assert utils.trim(input_str) == expected_output


# Тесты для contains
@pytest.mark.parametrize("input_str, symbol, expected_output", [
    ("SkyPro", "S", True),
    ("SkyPro", "U", False),
    ("", "a", False),
    ("123", "1", True)
])
def test_contains(input_str, symbol, expected_output):
    assert utils.contains(input_str, symbol) == expected_output


# Тесты для delete_symbol
@pytest.mark.parametrize("input_str, symbol, expected_output", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("SkyPro", "x", "SkyPro"), 
    ("aaaa", "a", ""),         
    ("123123", "1", "2323"),
])
def test_delete_symbol(input_str, symbol, expected_output):
    assert utils.delete_symbol(input_str, symbol) == expected_output