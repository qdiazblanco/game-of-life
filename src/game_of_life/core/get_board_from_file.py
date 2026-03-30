from importlib import resources

def load_board(board_name: str):

    with resources.files("game_of_life.premade_boards").joinpath(f"{board_name}.txt").open(encoding="utf-8") as file:
        return [[bool(int(cell)) for cell in row] for row in file.read().split("\n")]