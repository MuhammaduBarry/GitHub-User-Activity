from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING

import requests

if TYPE_CHECKING:
    from collections.abc import Iterator
    from typing import Any


# A function to test if data was received successfully
def grab_data(username: str):
    url = f"https://api.github.com/users/{username}/events"
    response = requests.get(url)
    return response.status_code

def parse_data(param1, param2, info) -> Iterator[Any]:
    return map(lambda x: x.get(param1).get(param2), info)

def parse_repo_urls(json_data) -> list[str]:
    return list(parse_data("repo", "url", json_data))

def fetch_data(username: str) -> None:
    url = f"https://api.github.com/users/{username}/events"
    response = requests.get(url)
    if response.status_code != HTTPStatus.OK:
        print(f"Failed to retrieve data: {response.status_code}")
        return

    github_data: list[dict[str, Any]] = response.json()
    print(github_data[0])

    # Grabbing values needed without for loop variable since we only need one value
    github_repo_url_data = parse_repo_urls(github_data)

    commit_counter = 0
    issue_counter = 0
    closed_issue_counter = 0

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
