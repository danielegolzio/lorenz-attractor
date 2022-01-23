'''
Typer experimenting
'''
import typer
import os 
import time

def main(username: str):
    """
    yo
    """
    if username == "root":
        typer.echo("The root user is reserved")
        raise typer.Abort()
    typer.secho(f"New user created: {username}", fg=typer.colors.MAGENTA, bg=typer.colors.RED)



if __name__ == "__main__":
    typer.run(main)