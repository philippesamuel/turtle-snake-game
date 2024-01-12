<!-- description from pyproject.toml) -->
# Snake game built with Python's turtle package

Simple snake game built with Python's turtle package. 
- The game is played on a 600x600 pixel screen. 
- The snake is controlled with the arrow keys. 
- The goal is to eat as many apples as possible without hitting the walls or the snake's own body. 
- The game ends when the snake hits the wall or its own body. 
- The score is displayed in the top right corner.

## Installation

### with pip
1. Clone the repository
2. (Optional) Create a virtual environment with `python -m venv .venv` and activate 
   it with `source .venv/bin/activate` (Linux) or `.venv\Scripts\activate` (Windows)
3. Install the dependencies with `pip install -r requirements.txt`
4. Run the game with `python snake_game/main.py`

### with poetry
1. Clone the repository
2. (Optional) Create a virtual environment with `poetry shell` and activate it with 
   `poetry shell` or use venv with `poetry config virtualenvs.in-project true`
3. Install the dependencies with `poetry install`
4. Run the game with `poetry run python snake_game/main.py` or `python snake_game/main.py`


You can customize the game by setting environment variables and/or changing the values in `.env`. (See `example.env`)