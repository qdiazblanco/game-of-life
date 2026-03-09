from .board import render
from .next_board import next_board_state

from time import sleep

def infinite_loop(board_state: list[list[bool]], model : str = 'edges') -> None:

    render(board_state)

    new_state = next_board_state(board_state, model)

    while board_state != new_state:
        sleep(0.2)
        render(new_state)
        board_state = new_state
        new_state = next_board_state(board_state, model)
        
    
