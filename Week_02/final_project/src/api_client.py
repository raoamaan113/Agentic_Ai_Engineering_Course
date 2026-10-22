# final_project/src/api_client.py
import os
import requests
from dotenv import load_dotenv
from requests.exceptions import Timeout, RequestException

# Load environment variables securely
load_dotenv()
API_KEY = os.getenv("API_KEY", "default_dummy_token")

def fetch_resource_securely(endpoint_path, post_id=1):
    base_url = "https://jsonplaceholder.typicode.com"
    url = f"{base_url}/{endpoint_path}/{post_id}"
    
    # Configure headers with authorization support
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Accept": "application/json"
    }
    
    try:
        print(f"\n[INFO] Requesting: {url} with a 5-second timeout...")
        # Request with timeout handling
        response = requests.get(url, headers=headers, timeout=5)
        
        # Status code validation
        if response.status_code == 200:
            print("[SUCCESS] Status: 200 OK")
            data = response.json()
            print(f"Data retrieved successfully. Title: {data.get('title', 'N/A')}")
            return data
        elif response.status_code == 400:
            print("[ERROR] Status: 400 Bad Request.")
        elif response.status_code == 401:
            print("[ERROR] Status: 401 Unauthorized. Check your API key.")
        elif response.status_code == 404:
            print("[ERROR] Status: 404 Not Found. The resource does not exist[cite: 2].")
        elif response.status_code == 429:
            print("[ERROR] Status: 429 Too Many Requests. Rate limit hit[cite: 3].")
        elif response.status_code >= 500:
            print(f"[ERROR] Status: {response.status_code} Server Error.")
        else:
            print(f"[WARNING] Unexpected status code: {response.status_code}")
            
    except Timeout:
        print("[ERROR] Request timed out. Server took too long to respond.")
    except RequestException as e:
        print(f"[ERROR] Network or connection failure occurred: {e}")

if __name__ == "__main__":
    print("=== Running Week 02 Final Integration Client ===")
    # Test valid request
    fetch_resource_securely("posts", 1)
    # Test 404 error handling
    fetch_resource_securely("posts", 99999)