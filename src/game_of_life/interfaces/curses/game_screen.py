import curses
from game_of_life.core.board import random_state, render

from time import sleep

def get_number(stdscr, y : int, x : int) -> int:
    stdscr.move(y, x)
    num = ""
    count = 0 
    while True:
        key = stdscr.getkey()

        if key == "\n":
            if is_valid_num(num):
                return int(num)
            
            stdscr.move(y, x)
            stdscr.addstr(' '*len(num))
            stdscr.refresh()
            stdscr.move(y, x)

            num = ''
            count = 0

        elif key in ('KEY_BACKSPACE', '\b', '\x7f') and num:
            num = num[:-1]
            count -= 1
        
            stdscr.addstr(y, x + count, ' ')
            stdscr.move(y, x + count)

        elif key.isdigit():
            num += key
            stdscr.addstr(y, x + count, key)
            stdscr.refresh()
            count += 1


def is_valid_num(num : str) -> bool:

    try:
        n = int(num)

        if n <= 0 or n > 100:
            return False

        return True

    except ValueError:
        return False



'''     
function to get the board size
'''
def choose_size(stdscr, half_col: int) -> tuple[int,int]:
    stdscr.clear()

    stdscr.addstr(5 , half_col - 11 , "CHOOSE BOARD SIZE:", curses.A_BOLD)
    stdscr.addstr(8 , half_col - 11 , "Width: ")
    stdscr.addstr(9 , half_col - 11 , "Height: ")

    stdscr.refresh()

    width = get_number(stdscr, 8, half_col - 4 )
    height = get_number(stdscr, 9, half_col - 3 )

    return width, height



def game_screen(stdscr) -> None:
    curses.update_lines_cols()

    stdscr.clear()
    
    cols = curses.COLS
    rows = curses.LINES
    half_col = cols//2
    half_row = rows//2
    
    stdscr.addstr(5 , half_col - 11 , "CHOOSE:", curses.A_BOLD)
    stdscr.addstr(8 , half_col - 11 , "[r]: Random board")

    choice = stdscr.getkey()
    if choice == 'r':

        width, height = choose_size(stdscr, half_col)
        render_width = min(cols, width*2 + 3)
        render_height = min(rows, height + 2)

        board_coordy = half_row - height//2
        board_coordx = half_col - width//2
        
        #stdscr.move(max(0, half_row - height//2), max(0, half_col - width//2))

        rand_board = render(random_state(render_width//2 - 1, render_height - 2)).splitlines()

        stdscr.clear()
        for i, line in enumerate(rand_board):
            stdscr.addstr(board_coordy+i , board_coordx , line)

        stdscr.move(rows-1, cols-1)
  
    stdscr.refresh()

    '''
    hacer funcion render especifica para curses
    '''