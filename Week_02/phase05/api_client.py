
# phase05/api_client.py
import requests
from requests.exceptions import Timeout, RequestException

def fetch_post_safely(post_id):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    
    try:
        print(f"\n--- Sending request for Post ID: {post_id} ---")
        # Task 21: Add a timeout parameter to prevent hanging indefinitely
        response = requests.get(url, timeout=5)
        
        # Task 20: Handle multiple HTTP error categories[cite: 2, 3]
        if response.status_code == 200:
            print("Status: 200 - Successful request[cite: 2, 3]!")
            data = response.json()
            print(f"Title: {data.get('title')}")
        elif response.status_code == 400:
            print("Status: 400 - Bad Request. The request was invalid.")
        elif response.status_code == 401:
            print("Status: 401 - Unauthorized. Authentication credentials missing or invalid[cite: 2, 3].")
        elif response.status_code == 404:
            # Task 19: Specific 404 Not Found handling[cite: 2, 3]
            print("Request failed. Status Code: 404 - Resource not found[cite: 2].")
        elif response.status_code == 429:
            print("Status: 429 - Too Many Requests. Rate limit exceeded[cite: 3].")
        elif response.status_code >= 500:
            print(f"Status: {response.status_code} - Server error. Please try again later[cite: 2, 3].")
        else:
            print(f"Unexpected HTTP status code: {response.status_code}")

    except Timeout:
        # Task 21 & 22: Timeout error handling[cite: 2, 3]
        print("Error: Request timed out. The server took too long to respond.")
    except RequestException as e:
        # Task 22: General network/connection failure handling[cite: 2, 3]
        print(f"Error: Network or request failure occurred: {e}")

if __name__ == "__main__":
    # Test a valid resource
    fetch_post_safely(1)
    
    # Test an invalid resource (Triggers 404)[cite: 2, 3]
    fetch_post_safely(99999)