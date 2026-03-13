from random import random # random() returns a 'random' float between 0 and 1

def dead_state( width : int , height : int ) -> list[list[bool]]:
    return([[False for _ in range(width)] for _ in range(height)])

def random_cell_state() -> bool:
    random_number = random()

    if random_number >= 0.7 :
        return True
    
    else:
        return False

def random_state( width : int , height : int ) -> list[list[bool]]:
    return([[random_cell_state() for _ in range(width)] for _ in range(height)])


def render(board_state : list[list[bool]]) -> None:
    width = len(board_state[0])
    height = len(board_state)

    top = bottom = '-' * (width * 3 + 2)

    board = top 
    for row in board_state:

        board += '\n' + '|'

        for cell in row:
            if cell == True:
                board += ' O '
            else:
                board += ' - '
        
        board += '|'

    board += '\n' + bottom

    print(board)
