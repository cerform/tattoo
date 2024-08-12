# client_base/models/client.py

from .. import db  # Import db from the parent module (client_base)

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    passport_id = db.Column(db.String(20), unique=True, nullable=False)
    phone_number = db.Column(db.String(20), unique=True, nullable=False)
    instagram = db.Column(db.String(100), nullable=True)
    date_of_birth = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    has_tattoos = db.Column(db.Boolean, nullable=False)
    photos = db.Column(db.PickleType, nullable=True)  # To store a list of photo file paths

    def __repr__(self):
        return f'<Client {self.name} {self.surname}>'
