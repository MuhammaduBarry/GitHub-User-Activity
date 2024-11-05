import typer
from rich import print as rich_print

from github_user_activity.api import fetch_data

app = typer.Typer()

@app.command()
def get_data(username: str):

    rich_print("\n[bold green]GitHub User Data:[/bold green]")
    fetch_data(username)

if __name__ == '__main__':
    app()
