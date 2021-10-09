import pytest
from python_refactored_waddle.give_me_something import give_me_something
@pytest.mark.parametrize(
    "test_input,expected",
    [
("a", "something a"),
("is cooking", "something is cooking"),
(" is cooking", "something  is cooking"),
 
    ],
)
def test_give_me_something(test_input, expected):
    cases = give_me_something(test_input)
    assert cases == expected
