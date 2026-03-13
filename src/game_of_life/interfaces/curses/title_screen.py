import curses

def title_screen(stdscr) -> None:
    curses.update_lines_cols()

    stdscr.clear()

    rows = curses.LINES
    cols = curses.COLS

    half_col = cols//2
    half_row = rows//2

    stdscr.addstr(max(1, half_row - 10) , half_col - 11 , "CONWAY'S GAME OF LIFE", curses.A_BOLD | curses.A_UNDERLINE)

    stdscr.addstr(max(2, half_row), half_col - 9 , "Press any key to")
    stdscr.addstr(max(3, half_row + 1), half_col - 6 , "begin Life", curses.A_STANDOUT)
    stdscr.refresh()