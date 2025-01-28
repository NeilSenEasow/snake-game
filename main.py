from bottle import Bottle
from routes import setup_routes

app = Bottle()
setup_routes(app)

if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)