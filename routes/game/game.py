from bottle import template
from .game_html import get_template

# Route for the game page
def setup(app):
    @app.route('/game')
    def game():
        return template(get_template())
