import json
import requests

def fetch_data(username) -> None:
    url = f"https://api.github.com/users/{username}/events"
    response = requests.get(url)
    if response.status_code == 200:
        github_event_data = response.json() # -> Returns github information in json format, which is also a dict in python
        for event in github_event_data:
            print(json.dumps(event["repo"], indent=4))
    else:
        print(f"Failed to retrieve data: {response.status_code}")