from bottle import template
from .game_html import get_template

# Game state
GRID_SIZE = 20
INITIAL_SNAKE = [210, 211, 212]  # Middle of grid, 3 cells long
DIRECTION = {
    "UP": -GRID_SIZE,
    "DOWN": GRID_SIZE,
    "LEFT": -1,
    "RIGHT": 1
}

# Route for the game page
def setup(app):
    @app.route('/game')
    def game():
        snake = INITIAL_SNAKE
        score = 0
        food_position = 55  # Random position for food
        return template(get_template(), 
            snake=snake,
            score=score,
            food=food_position
        )
