import requests

def fetch_data(username) -> None:
    url = f"https://api.github.com/users/{username}/events"
    response = requests.get(url)
    if response.status_code == 200:
        github_data = response.json()

        def lambda_grab(param1, param2, info) -> list:
            return list(map(lambda x: x.get(param1).get(param2), info))

        # Grabbing values needed without for loop variable since we only need one value
        github_repo_url_data = lambda_grab("repo", "url", github_data)

        commit_counter = issue_counter = closed_issue_counter = 0  # New Technique i learned :)

        for data in github_data:
            if "commits" in data["payload"]:
                commit_counter += 1
            if "issue" in data["payload"]:
                issue_counter += 1
            if "closed_at" in data["payload"] is not None:
                closed_issue_counter += 1

        print(f" - {username} is currently working on the repo: {github_repo_url_data[0].split("/")[5]}")
        print(f" - Recent data on repo: {github_repo_url_data[0]}")
        print(f" - {username} recently pushed {commit_counter} commits") # -> Total commits not repo :)
        print(f" - {username} has {issue_counter} open issue and closed {closed_issue_counter} issue\n")
    else:
        print(f"Failed to retrieve data: {response.status_code}")

