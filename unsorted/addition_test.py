import pytest

from python_refactored_waddle.addition import addition


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ((2, 3), 5),
        ((-3, -6), -9),
        ((7, 3), 10),
        ((88, 2), 90),
    ],
)
def test_eval(test_input, expected):
    return addition(*test_input) == expected
