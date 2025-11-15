import typer
from rich import print

app = typer.Typer()

USERS: dict[str, str] = {"salvador": "12345", "ale": "54321"}


@app.command("list")
def list_():
    print("[yellow]USERS:[/yellow]")
    print("\n".join(USERS.keys()))


@app.command()
def add(
    username: str = typer.Option(..., prompt=True),
    password: str = typer.Option(..., prompt=True, hide_input=True),
):
    USERS[username] = password
    print(f"User added {username}\n")
    # print(USERS)
    list_()
