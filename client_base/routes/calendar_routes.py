from flask import Blueprint, jsonify, request, render_template
from datetime import datetime
from client_base.models.event import Event  # Assuming you have an Event model to handle events
from client_base import db  # Assuming you have a database instance

calendar = Blueprint('calendar', __name__)

@calendar.route('/events', methods=['GET'])
def get_events():
    """Fetch all events from the database."""
    events = Event.query.all()  # Fetch all events from the database
    events_data = [{
        'id': event.id,
        'title': event.title,
        'start': event.start.isoformat(),  # Convert to ISO format for JSON serialization
        'end': event.end.isoformat()        # Convert to ISO format for JSON serialization
    } for event in events]
    return jsonify(events_data)

@calendar.route('/events', methods=['POST'])
def create_event():
    """Create a new event."""
    data = request.json
    new_event = Event(
        title=data.get('title'),
        start=datetime.fromisoformat(data.get('start')),
        end=datetime.fromisoformat(data.get('end'))
    )
    db.session.add(new_event)
    db.session.commit()
    return jsonify({'message': 'Event created successfully'}), 201

@calendar.route('/calendar_view', methods=['GET'])  # Add this line
def calendar_view():
    """Render the calendar view."""
    return render_template('calendar_view.html')  # Ensure this template exists
