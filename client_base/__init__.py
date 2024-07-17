# client_base/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/clients.db'
    app.config['SECRET_KEY'] = 'your_secret_key'

    db.init_app(app)

    # Import blueprints after initializing app to avoid circular import
    from client_base.routes.main_routes import main
    from client_base.routes.client_routes import clients
    from client_base.routes.calendar_routes import calendar

    # Register blueprints
    app.register_blueprint(main)
    app.register_blueprint(clients)  # Ensure clients blueprint is registered
    app.register_blueprint(calendar)

    return app
