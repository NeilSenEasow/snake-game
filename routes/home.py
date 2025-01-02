from bottle import template
from .home_html import get_template

# Route for the home page
def setup(app):
    @app.route('/')
    def home():
        return template(get_template())
