from game_of_life.interfaces.basic import terminal_interface 
from game_of_life.interfaces.curses.curses_ui import init_curses

from time import sleep
'''
checks if a choice of UI is valid and handles the error
'''
def is_valid_input(ui : str) -> bool:
    try:
        num = int(ui)

        if num == 1 or num == 2:
            print("Valid answer, starting...")
            return True
        else:
            print("Your answer must be either [1] or [2].")
            return False
        
    except ValueError:
        print("Your answer must be either [1] or [2].")
        return False
'''
asks the user to choose a UI and runs it
'''
def choose_interface() -> None:
    

    ui = input("Choose your desired interface:\nBasic[1]\nCurses[2]\n\nYour answer: ")

    count = 0
    while count < 2:
        if is_valid_input(ui):
            break
    
        count += 1

        ui = input("\nBasic[1]\nCurses[2]\n\nYour answer: ")


    if count == 2:
        print("\nMaximum number of inputs reached:\nShutting down...")
        return
    
    sleep(1)
    choice = int(ui)
    if choice == 1:
        terminal_interface()
    elif choice == 2:
        init_curses()