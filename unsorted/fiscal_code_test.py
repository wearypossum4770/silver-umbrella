import pytest

from python_refactored_waddle.fiscal_code import fiscal_code


@pytest.mark.parametrize(
    "test_input,expected",
    [
({ "name": "Brendan", "surname": "Eich", "gender": "M", "dob": "1/12/1961" }, "CHEBND61T01"),
({ "name": "Helen", "surname": "Yu", "gender": "F", "dob": "1/12/1950" }, "YUXHLN50T41"),
({ "name": "Al", "surname": "Capone", "gender": "M", "dob": "17/1/1899" }, "CPNLAX99A17"),
({ "name": "Mickey", "surname": "Mouse", "gender": "M", "dob": "16/1/1928" }, "MSOMKY28A16"),
({ "name": "Marie", "surname": "Curie", "gender": "F", "dob": "7/11/1867" }, "CRUMRA67S47"),    ],
)
def test_eval(test_input, expected):
    return fiscal_code(*test_input) == expected


