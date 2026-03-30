from game_of_life.core.board import random_state
from game_of_life.core.loop_life import infinite_loop
from game_of_life.core.get_board_from_file import load_board

from time import sleep

def get_model() -> str:

    model = input("Please choose a model for the board between 'edges' and 'toroidal': ").strip().lower()

    count = 1 
    while count < 3:

        if model in ('edges', 'toroidal'):
            break

        count += 1
        model = input("Invalid option. Please choose 'edges' or 'toroidal': ").strip().lower() 
    
    if count == 3:
        print("\nMaximum number of inputs reached:\nShutting down...")
        return ''

    return model 


def check_dimension(dim : str) -> None:
    if not dim:
        print('Default selected.')
        #w = default_width
    elif int(dim) <= 0:
        print('The width/height must be a positive number')
        raise ValueError
    elif int(dim) > 100:
        print("Board size too large")
        raise ValueError

def get_board_size(default_width : int = 10, default_height : int = 10) -> tuple[int, int]:
    
    width = default_width
    height = default_height

    count = 0 
    while count < 3:
        try:
            w = input(f"Please choose the width of the board (default = {default_width}, press enter): ").strip()
            
            check_dimension(w)

            sleep(0.5)

            h = input(f"Please choose the height of the board (default = {default_height}, press enter): ").strip()

            check_dimension(h)

            sleep(0.5)

            if not w and not h:
                print('Default board selected. Starting...')
                sleep(2)
                return width, height
            else:
                width = int(w)
                height = int(h)
                break

        except ValueError:
            count += 1
    
        
    if count == 3:
        print("\nMaximum number of inputs reached:\nDefault board assigned.")
        sleep(2)
        return default_width, default_height

    
    print('\nValid width and height. Starting...')
    sleep(2)
    return width, height


def choose_game_mode() -> str:

    mode = input("'random' or 'premade' board? ").strip().lower()

    count = 1 
    while count < 3:

        if mode in ('random', 'premade'):
            break

        count += 1
        mode = input("Invalid option. Please choose 'random' or 'premade'(yet to implement): ").strip().lower() 
    
    if count == 3:
        print("\nMaximum number of inputs reached:\nShutting down...")
        return ''

    return mode

def list_premade_boards() -> None:

    pass

def choose_premade_board() -> list[list[bool]] | None:
    input("Choose a premade board from the list above please: ")
    pass

def terminal_interface() -> None:

    model = get_model()
    mode = choose_game_mode()

    if model:
        if mode == 'random':
            width, height = get_board_size()

            start = random_state(width, height)
            infinite_loop(start, model)
        else:
            list_premade_boards()
            start = choose_premade_board()
            infinite_loop(start, model)