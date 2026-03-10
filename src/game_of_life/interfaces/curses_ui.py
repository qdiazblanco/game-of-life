import curses
from curses import wrapper

def curses_main(stdscr) -> None:
    stdscr.clear()
    stdscr.refresh()
    stdscr.addstr(3,35, "CONWAY'S GAME OF LIFE", curses.A_BOLD)
    stdscr.getch()

def init_curses() -> None:
    wrapper(curses_main)