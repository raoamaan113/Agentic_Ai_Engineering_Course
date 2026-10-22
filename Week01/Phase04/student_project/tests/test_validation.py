# tests/test_validation.py
import pytest
from student_app.utils.validation import validate_marks

def test_valid_marks():
    assert validate_marks("85") == 85.0
    assert validate_marks("0") == 0.0
    assert validate_marks("100") == 100.0

def test_invalid_out_of_bounds():
    with pytest.raises(ValueError):
        validate_marks("-5")
    with pytest.raises(ValueError):
        validate_marks("105")

def test_non_numeric_input():
    with pytest.raises(ValueError):
        validate_marks("abc")