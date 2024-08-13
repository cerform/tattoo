from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///E:/Dev_Ops/tattoo_salon_app/instance/clients.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define your models
class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    family_name = db.Column(db.String(80), nullable=False)
    id_number = db.Column(db.String(20), unique=True, nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    gender = db.Column(db.String(10), nullable=False)

# Create the database and tables
with app.app_context():
    print("Creating database and tables...")
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
