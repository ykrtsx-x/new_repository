import pytest
from string_utils import StringUtils

string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("  skypro", "Skypro"),
    ("\thello", "Hello"),
    ("\npython", "Python"),
])
def test_capitalize_strips_whitespace(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    (" ", " "),
    ("123", "123"),
    ("!@#", "!@#"),
    ("123abc", "123abc"),
    ("_test", "_test"),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected
