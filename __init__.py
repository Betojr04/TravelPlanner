from flask import Flask
from config import Config
from models import db
from routes import register_blueprints


def create_app():
    # Initialize Flask app
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize database
    db.init_app(app)

    # Register blueprints (routes)
    register_blueprints(app)

    # Create database tables
    with app.app_context():
        db.create_all()

    return app
