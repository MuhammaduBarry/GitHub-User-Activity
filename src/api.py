import requests

def fetch_data(username) -> None:
    url = f"https://api.github.com/users/{username}/events"
    response = requests.get(url)
    if response.status_code == 200:
        github_event_data = response.json()  # Returns GitHub information in JSON format, which is also a dict in Python
        # Grabbing sub set data from the response
        for event in github_event_data:
            event_repo_url = event["repo"].get("url")
            event_commit_message = event["payload"]["commits"][1].get("message")
            print(event_repo_url)
            print(event_commit_message)
            break
    else:
        print(f"Failed to retrieve data: {response.status_code}")

