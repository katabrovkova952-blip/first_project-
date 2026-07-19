from lection_8.homework_8_2 import is_palindrome
import pytest

@pytest.mark.parametrize("text, expected", [
    ("", True),
    ("AbBa", True),
    ('0P', False),
    (",,lev.el,,", True),
    ("f", True)
])

def test_is_palindrome(text, expected):
    assert is_palindrome(text) == expected
