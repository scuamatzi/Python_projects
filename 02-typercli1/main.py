# set enviroment variable before running this script:q
# export SMART_CAR_KEY="super secure key"
#
import typer
import os
from enum import StrEnum
from rich import print

# from typercli1 import users
import users

app = typer.Typer(name="Electric Car")
app.add_typer(users.app, name="users")

# USERS: dict[str, str] = {"salvador": "12345", "ale": "54321"}


class Direction(StrEnum):
    NORTH = "north"
    SOUTH = "south"
    EAST = "east"
    WEST = "west"


@app.command()
def drive(
    distance: int,
    direction: Direction = typer.Option(Direction.NORTH, "--direction", "-d"),
):
    print(
        f" [green] Going on an {distance} kms emission-free drive to {direction} [/green]"
    )


@app.command()
def stop():
    print("[red]Stopping the car.[/red]")


@app.command()
def unlock(
    username: str = typer.Option(..., prompt=True),
    password: str = typer.Option(..., prompt=True, hide_input=True),
):
    # if USERS.get(username) != password:
    if users.USERS.get(username) != password:
        print("[red] Incorrect username or password [/red]")
        raise typer.Exit(code=1)
    print(f"[green] Unlocking the car for {username}! [/green]")


@app.callback()
def check_for_key():
    if os.getenv("SMART_CAR_KEY") != "super secure key":
        print("[red] You need a key to access the car! [/red]")
        raise typer.Exit(code=1)


if __name__ == "__main__":
    app()
