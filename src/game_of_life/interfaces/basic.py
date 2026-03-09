from game_of_life.core.board import random_state
from game_of_life.core.loop_life import infinite_loop

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

def get_board_size(default_width : int = 10, default_height : int = 10) -> tuple[int, int]:
    
    width = default_width
    height = default_height

    count = 0 
    while count < 3:
        try:
            w = input(f"Please choose the width of the board (default = {default_width}, press enter): ").strip()
            
            if not w:
                print('Default selected.')
                w = default_width

            sleep(0.5)

            h = input(f"Please choose the height of the board (default = {default_height}, press enter): ").strip()

            if not h:
                print('Default selected.')
                h = default_height

            sleep(0.5)

            if not w and not h:
                print('Default board selected. Starting...')
                sleep(2)
                return width, height
            else:
                width = int(w)
                height = int(h)

            if width <= 0 or height <= 0:
                count += 1
                print("Board dimensions must be positive")

            elif width > 100 or height > 100:
                count += 1
                print("Board size too large")
            else:
                break

        except ValueError:
            count += 1
            print('The width/height must be a number')
    
        
    if count == 3:
        print("\nMaximum number of inputs reached:\nDefault board assigned.")
        sleep(2)
        return default_width, default_height

    print('\nValid width and height. Starting...')
    sleep(2)
    return width, height


def terminal_interface() -> None:

    model = get_model()

    if model:
        width, height = get_board_size()

        start = random_state(width, height)
        infinite_loop(start, model)