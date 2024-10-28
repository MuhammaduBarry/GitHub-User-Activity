import typer

from api import fetch_data

app = typer.Typer()

@app.command()
def get_data(username: str):
    fetch_data(username)

if __name__ == '__main__':
    app()