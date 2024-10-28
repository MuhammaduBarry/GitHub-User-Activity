import requests

def fetch_data(username) -> None:
    url = f"https://api.github.com/users/{username}/events"
    response = requests.get(url)
    if response.status_code == 200:
        github_event_data = response.json()  # Returns GitHub information in JSON format, which is also a dict in Python
        for event in github_event_data:
            if username in event["repo"]["name"]:
                print(event["repo"])
                break # -> Since we only need the first value we break the loop after one run
    else:
        print(f"Failed to retrieve data: {response.status_code}")

