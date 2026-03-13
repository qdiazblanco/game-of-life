import curses
from time import sleep

def transition(stdscr) -> None:
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    WHITE_AND_BLACK = curses.color_pair(1)
    stdscr.attron(WHITE_AND_BLACK)

    curses.update_lines_cols()

    stdscr.clear()

    rows = curses.LINES
    cols = curses.COLS

    for i in range(cols-1):
        stdscr.addstr(rows-1, i, "\u2588")
        stdscr.refresh()
        sleep(0.01)
