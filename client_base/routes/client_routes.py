# client_base/routes/client_routes.py

from flask import Blueprint, render_template, jsonify, request, redirect, url_for  # Import redirect and url_for
from client_base.models.client import Client
from client_base.forms.client_form import ClientForm
from client_base.models.event import Event  # Moved to the top for clarity
from client_base import db  # Import db to be able to use it for database operations

calendar = Blueprint('calendar', __name__)
clients = Blueprint('clients', __name__)

@clients.route('/clients/new', methods=['GET', 'POST'])
def new_client():
    form = ClientForm()
    if form.validate_on_submit():
        # Logic for adding a new client
        new_client = Client(
            name=form.name.data,
            surname=form.surname.data,
            passport_id=form.passport_id.data,
            phone_number=form.phone_number.data,
            instagram=form.instagram.data,
            date_of_birth=form.date_of_birth.data,
            gender=form.gender.data,
            has_tattoos=form.has_tattoos.data,
            photos=form.photos.data  # Adjust this line based on your form structure
        )
        db.session.add(new_client)
        db.session.commit()
        return redirect(url_for('clients.get_clients'))  # Adjust redirect as needed
    return render_template('new_client.html', form=form)

@calendar.route('/calendar')
def calendar_view():
    return render_template('calendar.html', title='Calendar')

@calendar.route('/events', methods=['GET'])
def events():
    events = Event.query.all()
    event_data = []
    for event in events:
        event_data.append({
            'id': event.id,
            'title': event.title,
            'start': event.start_time.isoformat(),
            'end': event.end_time.isoformat() if event.end_time else None,
            'description': event.description
        })
    return jsonify(event_data)

@calendar.route('/add_event', methods=['POST'])
def add_event():
    data = request.json
    new_event = Event(
        title=data['title'],
        start_time=data['start'],
        end_time=data['end'],
        description=data['description']
    )
    db.session.add(new_event)
    db.session.commit()
    return jsonify({'message': 'Event added successfully'}), 201

@clients.route('/clients', methods=['GET'])
def get_clients():
    clients = Client.query.all()
    client_data = []
    for client in clients:
        client_data.append({
            'id': client.id,
            'name': client.name,
            'surname': client.surname,
            'phone_number': client.phone_number
        })
    return jsonify(client_data)
