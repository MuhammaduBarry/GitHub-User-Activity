from src.api import grab_data

def test_data_success():
    username = "MuhammaduBarry"
    status_code = grab_data(username)
    assert status_code == 200

def test_data_username_failure():
    username = "Muhammadu Barry"
    status_code = grab_data(username)
    assert status_code == 404