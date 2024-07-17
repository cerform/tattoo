from flask import Blueprint, render_template, jsonify, request
from client_base import db  # Assuming 'db' is your SQLAlchemy instance
from client_base.models.event import Event  # Adjust based on your actual structure

calendar = Blueprint('calendar', __name__)

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
            'start': event.start.isoformat(),
            'end': event.end.isoformat() if event.end else None,
            'description': event.description
        })
    return jsonify(event_data)

@calendar.route('/add_event', methods=['POST'])
def add_event():
    data = request.json
    new_event = Event(
        title=data['title'],
        start=data['start'],
        end=data['end'],
        description=data['description']
    )
    db.session.add(new_event)
    db.session.commit()
    return jsonify({'message': 'Event added successfully'}), 201
