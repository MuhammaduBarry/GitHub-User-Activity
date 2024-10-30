import typer
from rich import print

from api import fetch_data

app = typer.Typer()

@app.command()
def get_data(username: str):

    print("\n[bold green]GitHub User Data:[/bold green]")
    fetch_data(username)

if __name__ == '__main__':
    app()