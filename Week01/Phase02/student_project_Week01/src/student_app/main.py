# main.py

# src/student_app/main.py
from student_app.utils.validate import validate_name, validate_marks
from student_app.services.Calculator import calculate_grade
from student_app.models.student import Student
from student_app.Reports.student_report import display_report

""""
def validate_name(name):
    return name != ""

def validate_marks(marks):
    return marks >= 0 or marks<=100

def calculate_grade(marks):
      # Calculate grade
        if marks >= 80:
            return  "A"
        elif marks >= 70:
            return  "B"
        elif marks >= 60:
            return "C"
        elif marks >= 50:
            return "D"
        else:
            return  "F"
    """

def main():
    name = input("Enter student name: ")
    if not validate_name(name):
        print("Invalid name")
        return  
    
    marks = int(input("Enter marks: "))
    if not validate_marks(marks):
        print("Invalid marks")
        return

    grade=calculate_grade(marks)
    student = Student(name, marks, grade)
    display_report(student)

  
    # Calculation
   # marks = 80
    #bonus = 5
    #total_marks = marks + bonus
    #print(f"Student: {name}")
    #print(f"Total Marks: {total_marks}")

"""""
    print("\nStudent Report")
    print("----------------")
    print(f"Name: {name}")
    print(f"Marks: {marks}")
    print(f"Grade: {grade}")
    """


if __name__ == "__main__":
    main()