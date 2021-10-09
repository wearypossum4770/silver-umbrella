import pytest

from python_refactored_waddle.defangIPaddr import defangIPaddr


@pytest.mark.parametrize(
    "test_input,expected",
    [("1.1.1.1", "1[.]1[.]1[.]1"), ("255.100.50.0", "255[.]100[.]50[.]0")],
)
def test_defangIPaddr(test_input, expected):
    assert defangIPaddr(test_input) == expected
