import pytest

from python_refactored_waddle.is_palindrome import is_palindrome


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (-121, False),
        (121, True),
        (10, False),
    ],
)
def test_eval(test_input, expected):
    return is_palindrome(test_input) == expected
