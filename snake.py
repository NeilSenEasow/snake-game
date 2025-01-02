from bottle import Bottle, run, template, static_file

# Create a Bottle application instance
app = Bottle()

# Route for the home page
@app.route('/')
def home():
    return template('''
        <h1>Welcome to Snake Game</h1>
        <a href="/game">Play Game</a>
    ''')

# Route for the game page
@app.route('/game')
def game():
    return template('''
        <h1>Snake Game</h1>
        <div id="game-container">
            <!-- Game will be added here later -->
            <p>Game coming soon!</p>
        </div>
        <button onclick="window.location.href='/'">Back to Home</button>
    ''')

# Start the server
if __name__ == '__main__':
    # Run the application in debug mode (remove debug=True in production)
    app.run(host='localhost', port=8080, debug=True)