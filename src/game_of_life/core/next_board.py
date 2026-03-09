from .board import dead_state
from itertools import product


def is_valid_index(index1 : int, index2 : int, width: int, height : int) -> bool:
    return 0 <= index1 < height and 0 <= index2 < width 

def neighbours_edges(board_state : list[list[bool]], row : int, cell : int, width, height) -> int:
    neighbours = 0
    for i, j in product([-1,0,1], [-1,0,1]):
        if is_valid_index(row+i, cell+j, width, height) and not (i == 0 and j == 0):
            neighbours += board_state[row+i][cell+j]

    return neighbours

def neighbours_toroidal(board_state : list[list[bool]], row : int, cell : int, width, height) -> int:
    neighbours = 0
    for i, j in product([-1,0,1], [-1,0,1]):
        if not (i == 0 and j == 0):
            neighbours += board_state[(row+i)%height][(cell+j)%width]

    return neighbours


def next_board_state(board_state : list[list[bool]], model : str = 'edges') -> list[list[bool]]:
    
    height = len(board_state)
    width = len(board_state[0])

    next_state = dead_state(width, height)

    if model == 'edges':
        neighbours_func = neighbours_edges
    elif model == 'toroidal':
        neighbours_func = neighbours_toroidal
    else:
        raise ValueError("Model must be 'edges' or 'toroidal'")

    for row in range(height):
            for cell in range(width):
                neighbours = neighbours_func(board_state, row, cell, width, height)

                next_state[row][cell] = neighbours == 3 or (neighbours == 2 and board_state[row][cell])

    return next_state

