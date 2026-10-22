
import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve API key securely without hardcoding[cite: 3, 4]
API_KEY = os.getenv("API_KEY")

if not API_KEY:
    print("Error: API_KEY is not set in the environment variables or .env file.")
else:
    # Construct headers with Bearer token authentication[cite: 3, 4]
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Accept": "application/json"
    }

    # Example protected endpoint request (using JSONPlaceholder as a demo structure)
    url = "https://jsonplaceholder.typicode.com/posts/1"
    
    print("Sending request with Authorization header...")
    response = requests.get(url, headers=headers)

    print("Status Code:", response.status_code)
    if response.status_code == 200:
        print("Success! Protected resource retrieved securely.")
        print(response.json())
    else:
        print("Authentication or request failed.")