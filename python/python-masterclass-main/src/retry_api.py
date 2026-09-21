import time
import requests

retries = 3

for attempt in range(retries):
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/posts")
        response.raise_for_status()
        print("request successful")
        break
    except Exception as e:
        print(f"Attempt {attempt + 1} failed")
        time.sleep(2)
