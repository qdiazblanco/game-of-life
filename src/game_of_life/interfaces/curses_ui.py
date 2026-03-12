import curses
from curses import color_pair, wrapper
from time import sleep

from game_of_life.core.board import random_state, render

'''
glider = render([
    [False, False, True,  False, False, False, False, False, False, False],
    [False, False, False, True,  False, False, False, False, False, False],
    [False, True,  True,  True,  False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    ]).splitlines()
'''


def title_screen(stdscr) -> None:
    curses.update_lines_cols()

    stdscr.clear()

    half_col = curses.COLS//2
    
    stdscr.addstr(5 , half_col - 11 , "CONWAY'S GAME OF LIFE", curses.A_BOLD | curses.A_UNDERLINE)

    stdscr.addstr(15, half_col - 9 , "Press any key to")
    stdscr.addstr(16, half_col - 6 , "begin Life", curses.A_STANDOUT)
    stdscr.refresh()

def get_number(stdscr, axis: int, half_col: int) -> int:
    stdscr.clear()

    stdscr.addstr(5 , half_col - 11 , "CHOOSE BOARD SIZE:", curses.A_BOLD)
    stdscr.addstr(8 , half_col - 11 , "Width: ")
    stdscr.addstr(9 , half_col - 11 , "Height: ")

    stdscr.refresh()

    num = ''
    key = stdscr.getkey()

    if key == "\n":  # ENTER
        if num:
            return int(num)

    elif key.isdigit():
        num += key
        if axis == 1:
            stdscr.addstr(8, half_col - 1, num)
            stdscr.refresh()
            sleep(1)
            return int(num)
        
        elif axis == 2: 
            stdscr.addstr(9, half_col - 1, num)
            stdscr.refresh()
            sleep(1)
            return int(num)


def game_screen(stdscr) -> None:
    curses.update_lines_cols()

    stdscr.clear()

    half_col = curses.COLS//2
    
    stdscr.addstr(5 , half_col - 11 , "CHOOSE:", curses.A_BOLD)
    stdscr.addstr(8 , half_col - 11 , "[r]: Random board")

    choice = stdscr.getkey()
    if choice == 'r':

        width = get_number(stdscr, 1,  half_col)
        height = get_number(stdscr, 2, half_col)

        rand_board = render(random_state(width,height)).splitlines()

        stdscr.clear()
        for i, line in enumerate(rand_board):
            stdscr.addstr(10+i , half_col - 11 , line)
        
        stdscr.move(curses.LINES-1, curses.COLS-1)
  
    stdscr.refresh()


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




def curses_main(stdscr) -> None:
    stdscr.clear()
    stdscr.refresh()


    while True:
        title_screen(stdscr)
        
        key = stdscr.getch()

        if key:
            break

    transition(stdscr)

    while True:
        game_screen(stdscr)

        key = stdscr.getch()

        if key:
            break

        



def init_curses() -> None:
    wrapper(curses_main)
