from . import home
from .game import game

def setup_routes(app):
    home.setup(app)
    game.setup(app)
