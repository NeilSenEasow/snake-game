from bottle import template

# Route for the home page
def setup(app):
    @app.route('/')
    def home():
        return template('''
            <h1>Welcome to Snake Game</h1>
            <a href="/game">Play Game</a>
        ''')
