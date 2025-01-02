from bottle import template

# Route for the game page
def setup(app):
    @app.route('/game')
    def game():
        # You can pass data to the template like this:
        game_title = "Snake Game"
        grid_size = 20
        return template('game', 
            title=game_title,
            size=grid_size
        )
