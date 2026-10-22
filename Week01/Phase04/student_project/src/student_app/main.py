# src/student_app/main.py
from student_app.logger import logger
from student_app.utils.validation import validate_marks
from student_app.services.calculator import calculate_grade

def main():
    logger.info("Student Information App Started")
    
    student_name = input("Enter Student Name: ").strip()
    if not student_name:
        logger.warning("Empty student name provided.")
        print("Error: Student name cannot be empty.")
        return

    raw_marks = input("Enter Student Marks (0-100): ").strip()

    # Stage 2 & 3: Exception handling and validation
    try:
        marks = validate_marks(raw_marks)
    except ValueError as e:
        logger.error(f"Validation failed for input '{raw_marks}': {e}")
        print(f"Input Error: {e}")
        return

    # Stage 7: Calculate grade
    grade = calculate_grade(marks)
    logger.info(f"Successfully calculated grade '{grade}' for {student_name} ({marks} marks)")

    print("\n--- Student Result ---")
    print(f"Name:  {student_name}")
    print(f"Marks: {marks}")
    print(f"Grade: {grade}")

if __name__ == "__main__":
    main()