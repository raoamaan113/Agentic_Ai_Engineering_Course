# reports/student_report.py
def display_report(student):
    """Formats and prints the student report from a Student instance."""
    print("\nStudent Report")
    print("----------------")
    print(f"Name: {student.name}")
    print(f"Marks: {student.marks}")
    print(f"Grade: {student.grade}")