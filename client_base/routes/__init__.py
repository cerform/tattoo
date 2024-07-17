from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Blueprint, render_template

calendar = Blueprint('calendar', __name__)

@calendar.route('/calendar')
def calendar_view():
    # Your logic for handling the calendar view
    return render_template('calendar.html', title='Calendar')

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clients.db'
    app.config['SECRET_KEY'] = 'your_secret_key'

    db.init_app(app)
    migrate.init_app(app, db)

    from client_base.routes.main_routes import main
    from client_base.routes.client_routes import clients
    from client_base.routes.calendar_routes import calendar

    app.register_blueprint(main)
    app.register_blueprint(clients)
    app.register_blueprint(calendar)

    return app
