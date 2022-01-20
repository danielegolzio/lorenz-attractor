<<<<<<< Updated upstream
'''
curses experimenting
'''
# import curses
# from curses import wrapper
# from curses.textpad import Textbox, rectangle
# import time

# stdscr = initstdscr()
# curses.curs_set(0)

# def main(stdscr):
#     # Clear screen
#     stdscr.clear()

#     rectangle(stdscr, 2, 2, 10, 20)
#     stdscr.refresh()
#     stdscr.getkey()

# wrapper(main)

'''
Typer experimenting
'''
import typer


def main(username: str):
    if username == "root":
        typer.echo("The root user is reserved")
        raise typer.Abort()
    typer.echo(f"New user created: {username}")


if __name__ == "__main__":
    typer.run(main)


=======
import curses
from curses import wrapper


fish = """
           FISHKISSFISHKIS               
       SFISHKISSFISHKISSFISH            F
    ISHK   ISSFISHKISSFISHKISS         FI
  SHKISS   FISHKISSFISHKISSFISS       FIS
HKISSFISHKISSFISHKISSFISHKISSFISH    KISS
  FISHKISSFISHKISSFISHKISSFISHKISS  FISHK
      SSFISHKISSFISHKISSFISHKISSFISHKISSF
  ISHKISSFISHKISSFISHKISSFISHKISSF  ISHKI
SSFISHKISSFISHKISSFISHKISSFISHKIS    SFIS
  HKISSFISHKISSFISHKISSFISHKISS       FIS
    HKISSFISHKISSFISHKISSFISHK         IS
       SFISHKISSFISHKISSFISH            K
         ISSFISHKISSFISHK               
      """

def main(stdscr):
    stdscr.clear()
    fish = curses.newwin(10,10)
    fish.addstr("hello world")
    fish.refresh()
    for i in range(12):
        fish.move(0,1)
        stdscr.refresh()
        stdscr.clear()
    stdscr.getch()
wrapper(main)
>>>>>>> Stashed changes
