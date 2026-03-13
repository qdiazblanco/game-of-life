import curses
from curses import color_pair, wrapper
from time import sleep

from game_of_life.interfaces.curses.title_screen import title_screen
from game_of_life.interfaces.curses.transition import transition
from game_of_life.interfaces.curses.game_screen import game_screen




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
