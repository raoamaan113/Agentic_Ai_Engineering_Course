# src/student_app/utils/validation.py

def validate_marks(marks_str):
    """
    Validates and converts input marks.
    Raises ValueError if invalid, out of bounds (< 0 or > 100), or non-numeric.
    """
    try:
        marks = float(marks_str)
    except ValueError:
        raise ValueError("Marks must be a numeric value.")

    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100.")

    return marks