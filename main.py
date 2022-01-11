import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle
import time

stdscr = initstdscr()
curses.curs_set(0)

def main(stdscr):
    # Clear screen
    stdscr.clear()

    rectangle(stdscr, 2, 2, 10, 20)
    stdscr.refresh()
    stdscr.getkey()

wrapper(main)