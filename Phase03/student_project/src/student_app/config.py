# src/student_app/config.py
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

APP_NAME = os.getenv("APP_NAME", "Student App")
DEBUG = os.getenv("DEBUG", "False") == "True"
MAX_STUDENTS = int(os.getenv("MAX_STUDENTS", "50"))
API_KEY = os.getenv("API_KEY")