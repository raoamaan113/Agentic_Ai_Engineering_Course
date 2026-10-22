# src/student_app/main.py
import json
from pathlib import Path
from student_app.config import APP_NAME, DEBUG, MAX_STUDENTS, API_KEY

def main():
    # 1. Display Environment Configuration
    print(f"=== {APP_NAME} ===")
    print(f"Debug Mode: {DEBUG}")
    print(f"Max Capacity: {MAX_STUDENTS}")
    if API_KEY:
        print("Security Status: API Key Authenticated")
    print("-" * 30)

    # 2. Read and Display JSON Student Data
    json_path = Path("data/student.json")
    if json_path.exists():
        with open(json_path, "r") as f:
            student_data = json.load(f)
            
        print("\nLoaded Student Record:")
        print(f"ID:       {student_data.get('id')}")
        print(f"Name:     {student_data.get('name')}")
        print(f"Program:  {student_data.get('program')}")
        print(f"Semester: {student_data.get('semester')}")
        print(f"Marks:    {student_data.get('marks')}")
    else:
        print("Error: data/student.json file not found.")

if __name__ == "__main__":
    main()