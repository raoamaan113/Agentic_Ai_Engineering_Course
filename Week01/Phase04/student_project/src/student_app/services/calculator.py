# src/student_app/services/calculator.py

def calculate_grade(marks):
    """
    Calculates letter grade based on marks standard.
    """
    if marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"