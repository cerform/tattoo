from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize the database and migration
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    # Create the Flask application
    app = Flask(__name__)

    # Set configuration values
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clients.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a strong secret key

    # Initialize the database and migration with the app
    db.init_app(app)
    migrate.init_app(app, db)

    # Import blueprints here to avoid circular imports
    from client_base.routes.main_routes import main
    from client_base.routes.client_routes import clients
    from client_base.routes.calendar_routes import calendar

    # Register blueprints
    app.register_blueprint(main)
    app.register_blueprint(clients)
    app.register_blueprint(calendar)

    return app
