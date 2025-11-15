# python main.py main --help
# python main.py goodbye --help
# python main.py goodbye --formal diablo
import typer

app = typer.Typer()


@app.command()
def main(name: str):
    print(f"Hello {name}.")


@app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        print(f"Goodbye Ms {name}. Have a good day.")
    else:
        print(f"Bye {name}.")


if __name__ == "__main__":
    #    typer.run(main)
    app()
