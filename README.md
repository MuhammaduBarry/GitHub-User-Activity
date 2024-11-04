# GitHub User Activity

A Python project designed to retrieve, analyze, and display GitHub user activity. Using the GitHub API, this tool provides insights into user contributions, repositories, and recent activities. This project can be used to monitor GitHub profiles, track contributions over time, and present user data in a readable format.

---
## Features

- Fetch user profile data from GitHub.
- Retrieve a user's recent activity and contributions.
- Display GitHub user statistics in a formatted output using the `rich` library.
- Command-line interface (CLI) powered by `typer` for easy interaction.

---
## Requirements

- Python 3.8 or above

---
## Installation Guide

1. **Clone the repository:**
```bash
  git clone https://github.com/MuhammaduBarry/github-user-activity.git
  cd github-user-activity
```
2. **Install dependencies:**
- Use `pip` to install the required packages listed in `requirements.txt`:
```bash
  pip install -r requirements.txt
```

---
## Usage

This tool is run from the command line and provides a variety of commands to interact with GitHub user data. Make sure to replace `<username>` with the GitHub username you want to analyze.

1. **Fetch User Profile:**
```bash
  github-activity <username>
```
 - **Example**:
```bash
    github-actvity "MuhammaduBarry"
 ```
** Do not add a space inside the string!! **

---
## Project Structure

- **`main.py`**: CLI interface to interact with the user activity functions.
- **`api.py`**: Contains functions to call the GitHub API and process user data.
- **`api_test.py`**: Test cases for the API functions, ensuring the correct data is fetched and processed.
- **`requirements.txt`**: Lists the required Python packages.

---
## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push the branch.
4. Submit a pull request with a detailed description of the changes.

---
## Acknowledgments

This project was inspired by the GitHub User Activity roadmap on roadmap.sh. Special thanks to all contributors and open-source libraries.

Roadmap.sh link: