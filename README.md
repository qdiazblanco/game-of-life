# Conway's Game of Life

[Game info](https://es.wikipedia.org/wiki/Juego_de_la_vida)

## Rules
1. Any live cell with 0 or 1 live neighbors becomes dead, because of underpopulation
2. Any live cell with 2 or 3 live neighbors stays alive, because its neighborhood is just right
3. Any live cell with more than 3 live neighbors becomes dead, because of overpopulation
4. Any dead cell with exactly 3 live neighbors becomes alive, by reproduction


# About the project
As of today the game runs only on the terminal. It doesn't have a UI but I plan on changing this. When running the game it let's you choose a model for the board between:
- edges: nothing exists outside the edges of the board.
- toroidal: paralel edges are identified, the board behaves like a torus, there ir no 'outside of the board'.
    - For example, a glider that leaves the board on the right side appears from the left side, same with top and bottom.


## Requirements
- Python version 3.13 or newer
- Poetry (for easy installation and use):
    - Install Poetry: https://python-poetry.org/docs/#installation
- Dependencies:
    - pytest (version >=9.0.2 or <10.0.0), (optional, used for testing only)

## Installation

### Easy way: Use poetry
1. Clone the repository.
2. Enter the project folder.
3. (In the terminal) poetry install
    - This creates a virtual environment and adds the required dependencies automatically.

### Less easy but easy still way
1. Clone the repository.
2. Create a virtual environment inside your folder of choice (I usually use a separate .venvs/ folder):
    - `python -m venv ~/.venvs/<venv-name>`
3. Install dependencies in the virtual environment:
    - Activate: `source ~/.venvs/<venv-name>/bin/activate` 
    - Add dependencies: `python -m pip install <dependecies>`


## Run (the way I do it)
1. Open the terminal in vscodium
2. `eval $(poetry env activate)` or `source ~/.venvs/<venv-name>/bin/activate` 
3. `python -m game_of_life`

## Test
1. In `tests/` create a `test_<test-name>.py` or use the ones already there. 
2. Inside `test_<test-name>.py` create functions with names starting with `test_`
3. Open the terminal in vscodium and run `pytest`, you will get imediate feedback.


# To be implemented:

- Load board states from files
- Store states

Interfaces:
- Terminal UI using curses.
- Game UI using pygame.
- Web UI






