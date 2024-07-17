from flask_wtf import FlaskForm
from wtforms import StringField, DateField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length

class ClientForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=100)])
    surname = StringField('Surname', validators=[DataRequired(), Length(min=2, max=100)])
    passport_id = StringField('Passport ID', validators=[DataRequired(), Length(min=2, max=20)])
    phone_number = StringField('Phone Number', validators=[DataRequired(), Length(min=2, max=20)])
    instagram = StringField('Instagram', validators=[Length(max=100)])
    date_of_birth = DateField('Date of Birth', format='%Y-%m-%d', validators=[DataRequired()])
    gender = StringField('Gender', validators=[DataRequired(), Length(max=10)])
    has_tattoos = BooleanField('Has Tattoos')
    submit = SubmitField('Submit')
