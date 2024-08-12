# client_base/forms/client_form.py

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, SelectField, BooleanField
from wtforms.validators import DataRequired, Length

class ClientForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=100)])
    surname = StringField('Surname', validators=[DataRequired(), Length(max=100)])
    passport_id = StringField('Passport ID', validators=[DataRequired(), Length(max=20)])
    phone_number = StringField('Phone Number', validators=[DataRequired(), Length(max=20)])
    instagram = StringField('Instagram', validators=[Length(max=100)])
    date_of_birth = DateField('Date of Birth', format='%Y-%m-%d', validators=[DataRequired()])
    gender = SelectField('Gender', choices=[('Male', 'Male'), ('Female', 'Female')], validators=[DataRequired()])
    has_tattoos = BooleanField('Has Tattoos')
    photos = StringField('Photos')  # Adjust based on how you want to handle photo uploads
    submit = SubmitField('Submit')
