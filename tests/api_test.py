from http import HTTPStatus

from github_user_activity.api import grab_data

def test_data_success():
    username = "MuhammaduBarry"
    status_code = grab_data(username)
    assert status_code == HTTPStatus.OK

def test_data_username_failure():
    username = "Muhammadu Barry"
    status_code = grab_data(username)
    assert status_code == HTTPStatus.NOT_FOUND
