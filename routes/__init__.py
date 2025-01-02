from . import home
from . import game

def setup_routes(app):
    home.setup(app)
    game.setup(app)
