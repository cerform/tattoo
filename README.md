Tattoo Salon Administration System
Overview
This project is a Tattoo Salon Administration System designed to manage client details, tattoo scheduling, and client-related data efficiently. The application is built using Flask, with a focus on a user-friendly interface and robust backend to handle client management, appointments, and other essential features for the salon.

Project Structure
The project follows a structured layout, separating concerns into different modules for better organization and maintainability. Below is an overview of the directory structure:
<details>
<summary>Project File Tree</summary>
./
│
├── client_base/
│ ├── forms.py
│ ├── models.py
│ ├── init.py
│ ├── calendar/
│ │ ├── forms.py
│ │ ├── routes.py
│ ├── forms/
│ │ ├── client_form.py
│ ├── models/
│ │ ├── client.py
│ ├── routes/
│ │ ├── calendar_routes.py
│ │ ├── client_routes.py
│ │ ├── main_routes.py
│ ├── static/
│ │ ├── css/
│ │ │ ├── styles.css
│ │ ├── img/
│ │ ├── js/
│ │ │ ├── scripts.js
│ ├── templates/
│ │ ├── base.html
│ │ ├── calendar.html
│ │ ├── calendar_view.py
│ │ ├── dashboard.html
│ │ ├── edit_client.html
│ │ ├── new_appointment.html
│ │ ├── new_client.html
│ │ ├── search_clients.html
│ │ ├── view_client.html
│ ├── utils/
│ │ ├── helpers.py
├── instance/
│ ├── clients.db
├── migrations/
│ ├── alembic.ini
│ ├── env.py
│ ├── README
│ ├── script.py.mako
│ ├── versions/
│ │ ├── 89b868e4991b_initial_migration.py
├── retrieve.py
├── run.py
├── tree.py
├── wsgi.py
</details>
Directory and File Descriptions
client_base/
forms.py: Contains form classes for client-related forms, such as client creation and editing.
models.py: Includes the database models that define the structure of the database tables used in the application.
init.py: Initializes the client_base module, setting up the Flask blueprint and other configurations.
client_base/calendar/
forms.py: Contains form classes related to calendar events and scheduling.
routes.py: Handles routing and logic for calendar-related functionalities, including scheduling and viewing appointments.
client_base/forms/
client_form.py: Manages form classes specifically for client management, including validations and input handling.
client_base/models/
client.py: Defines the database model for clients, including fields such as name, family name, ID number, phone number, and gender.
client_base/routes/
calendar_routes.py: Routes and logic related to calendar functionalities.
client_routes.py: Handles routing and logic for client-related operations like adding, viewing, and editing clients.
main_routes.py: Contains the main application routes, managing the dashboard and other core functionalities.
client_base/static/
css/styles.css: Contains the stylesheets for the application, defining the visual appearance of the UI.
img/: Stores static image files used in the application.
js/scripts.js: Contains JavaScript files for client-side interactivity and functionality.
client_base/templates/
base.html: The base template for all HTML files, containing common elements like header and footer.
calendar.html: Template for the calendar view, displaying scheduled appointments.
calendar_view.py: Provides logic for rendering the calendar and managing views.
dashboard.html: Template for the dashboard, showing an overview of the current day, week, and month schedules.
edit_client.html: Template for editing existing client details.
new_appointment.html: Template for creating new appointments.
new_client.html: Template for adding new clients.
search_clients.html: Template for searching clients by name, phone, or ID number.
view_client.html: Template for viewing client details.
client_base/utils/
helpers.py: Utility functions and helper methods used across different modules in the application.
instance/
clients.db: SQLite database file storing client and appointment data.
migrations/
alembic.ini: Configuration file for Alembic, used for managing database migrations.
env.py: Sets up the environment for database migrations.
README: Provides information about the migration scripts.
script.py.mako: Template used by Alembic for generating migration scripts.
versions/89b868e4991b_initial_migration.py: The initial database migration script.
Root Files
retrieve.py: Script for retrieving and displaying data from the database.
run.py: The main entry point of the application, initializing the Flask app and starting the server.
tree.py: Script for displaying the project’s file tree structure.
wsgi.py: WSGI entry point for deploying the application.
Getting Started
Prerequisites
Python 3.x
Flask
SQLite
Alembic
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/cerform/tattoo.git
cd tattoo
Set up a virtual environment and install dependencies:

bash
Copy code
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
Initialize the database:

Copy code
flask db upgrade
Run the application:

arduino
Copy code
python run.py
Development Workflow
Adding new features:

Develop your feature in a separate branch and create a pull request for review.
Follow the project structure and conventions outlined in this README.
Database migrations:

If you modify the database schema, create a new migration script using Alembic:
arduino
Copy code
flask db migrate -m "Description of change"
flask db upgrade
Testing:

Ensure that new features and bug fixes are well-tested before merging into the main branch.
Contribution Guidelines
Follow the coding standards and best practices as specified in the CONTRIBUTING.md file.
Write clear and concise commit messages.
Document new features and code changes adequately.
