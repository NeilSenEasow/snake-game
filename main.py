from bottle import Bottle, run, template, static_file
import routes.home as home
import routes.game as game  

# Create a Bottle application instance
app = Bottle()

home.setup(app)
game.setup(app)

# Start the server
if __name__ == '__main__':
    # Run the application in debug mode (remove debug=True in production)
    app.run(host='localhost', port=8080, debug=True)