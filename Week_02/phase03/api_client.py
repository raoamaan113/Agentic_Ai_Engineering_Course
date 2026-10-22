# phase03/api_client.py
import requests


# Task 14: Retrieve Multiple API Records using a loop
print("\n--- Task 14: Multiple Records ---")
for post_id in [1, 2, 3]:
    res = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}")
    if res.status_code == 200:
        data = res.json()
        print(f"Post {post_id}: {data.get('title')}")

# Task 15: Retrieve and Process a Collection
print("\n--- Task 15: Collection Processing ---")
collection_res = requests.get("https://jsonplaceholder.typicode.com/posts")
if collection_res.status_code == 200:
    posts = collection_res.json()
    print(f"Total posts retrieved: {len(posts)}")
    print("First 5 post titles:")
    for post in posts[:5]:
        print(f"- {post.get('title')}")
        

# Task 11: JSON Student Record to Python Dictionary
student_record = {
    "name": "Ali",
    "marks": 85,
    "program": "BSCS"
}

print("--- Student Record ---")
print("Name:", student_record["name"])
print("Marks:", student_record["marks"])
print("Program:", student_record["program"])

# Task 12: JSON Array as a Python List of Dictionaries
students_list = [
    {"id": 1, "name": "Ali"},
    {"id": 2, "name": "Amaan"},
    {"id": 3, "name": "Hafsa"},
    {"id": 4, "name": "Tooba"}
]

print("\n--- Students List ---")
for student in students_list:
    print(f"ID: {student['id']}, Name: {student['name']}")

# Task 13: Your First Python API Client (GET /posts/1)
print("\n--- API Client Request ---")
url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)

print("Status:", response.status_code)
if response.status_code == 200:
    post_data = response.json()
    print("Post ID:", post_data.get("id"))
    print("Title:", post_data.get("title"))
    print("Body:", post_data.get("body"))