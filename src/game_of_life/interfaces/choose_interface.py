from game_of_life.interfaces.basic import terminal_interface 
from game_of_life.interfaces.curses_ui import init_curses

'''
checks if a choice of UI is valid and handles the error
'''
def is_valid_input() -> None:
    pass

'''
asks the user to choose a UI and runs it
'''
def choose_int() -> None:
    
    ui = int(input("Choose your desired interface:\nBasic[1]\nCurses[2]\n\nYour answer: "))

    if ui == 1:
        terminal_interface()
    elif ui == 2:
        init_curses()