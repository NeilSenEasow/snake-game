from bottle import template

# Route for the game page
def setup(app):
    @app.route('/game')
    def game():
        return template('''
            <h1>Snake Game</h1>
            <div id="game-container">
                <!-- Game will be added here later -->
                <p>Game coming soon!</p>
            </div>
        ''')
