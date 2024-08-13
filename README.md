<h1>Tattoo Salon Administration System</h1>

<h2>Overview</h2>
<p>This project is a <strong>Tattoo Salon Administration System</strong> designed to manage client details, tattoo scheduling, and client-related data efficiently. The application is built using Flask, with a focus on a user-friendly interface and robust backend to handle client management, appointments, and other essential features for the salon.</p>

<h2>Project Structure</h2>
<p>The project follows a structured layout, separating concerns into different modules for better organization and maintainability. Below is an overview of the directory structure:</p>

<h3>Project File Tree</h3>
<details>
<summary>Click to expand the project file tree</summary>

<pre>
./
│
├── client_base/
│   ├── forms.py
│   ├── models.py
│   ├── __init__.py
│   ├── calendar/
│   │   ├── forms.py
│   │   ├── routes.py
│   ├── forms/
│   │   ├── client_form.py
│   ├── models/
│   │   ├── client.py
│   ├── routes/
│   │   ├── calendar_routes.py
│   │   ├── client_routes.py
│   │   ├── main_routes.py
│   ├── static/
│   │   ├── css/
│   │   │   ├── styles.css
│   │   ├── img/
│   │   ├── js/
│   │   │   ├── scripts.js
│   ├── templates/
│   │   ├── base.html
│   │   ├── calendar.html
│   │   ├── calendar_view.py
│   │   ├── dashboard.html
│   │   ├── edit_client.html
│   │   ├── new_appointment.html
│   │   ├── new_client.html
│   │   ├── search_clients.html
│   │   ├── view_client.html
│   ├── utils/
│   │   ├── helpers.py
├── instance/
│   ├── clients.db
├── migrations/
│   ├── alembic.ini
│   ├── env.py
│   ├── README
│   ├── script.py.mako
│   ├── versions/
│   │   ├── 89b868e4991b_initial_migration.py
├── retrieve.py
├── run.py
├── tree.py
├── wsgi.py
</pre>
</details>

<h3>Directory and File Descriptions</h3>

<h4>client_base/</h4>
<ul>
    <li><strong>forms.py</strong>: Contains form classes for client-related forms, such as client creation and editing.</li>
    <li><strong>models.py</strong>: Includes the database models that define the structure of the database tables used in the application.</li>
    <li><strong>__init__.py</strong>: Initializes the client_base module, setting up the Flask blueprint and other configurations.</li>
</ul>

<h5>client_base/calendar/</h5>
<ul>
    <li><strong>forms.py</strong>: Contains form classes related to calendar events and scheduling.</li>
    <li><strong>routes.py</strong>: Handles routing and logic for calendar-related functionalities, including scheduling and viewing appointments.</li>
</ul>

<h5>client_base/forms/</h5>
<ul>
    <li><strong>client_form.py</strong>: Manages form classes specifically for client management, including validations and input handling.</li>
</ul>

<h5>client_base/models/</h5>
<ul>
    <li><strong>client.py</strong>: Defines the database model for clients, including fields such as name, family name, ID number, phone number, and gender.</li>
</ul>

<h5>client_base/routes/</h5>
<ul>
    <li><strong>calendar_routes.py</strong>: Routes and logic related to calendar functionalities.</li>
    <li><strong>client_routes.py</strong>: Handles routing and logic for client-related operations like adding, viewing, and editing clients.</li>
    <li><strong>main_routes.py</strong>: Contains the main application routes, managing the dashboard and other core functionalities.</li>
</ul>

<h5>client_base/static/</h5>
<ul>
    <li><strong>css/styles.css</strong>: Contains the stylesheets for the application, defining the visual appearance of the UI.</li>
    <li><strong>img/</strong>: Stores static image files used in the application.</li>
    <li><strong>js/scripts.js</strong>: Contains JavaScript files for client-side interactivity and functionality.</li>
</ul>

<h5>client_base/templates/</h5>
<ul>
    <li><strong>base.html</strong>: The base template for all HTML files, containing common elements like header and footer.</li>
    <li><strong>calendar.html</strong>: Template for the calendar view, displaying scheduled appointments.</li>
    <li><strong>calendar_view.py</strong>: Provides logic for rendering the calendar and managing views.</li>
    <li><strong>dashboard.html</strong>: Template for the dashboard, showing an overview of the current day, week, and month schedules.</li>
    <li><strong>edit_client.html</strong>: Template for editing existing client details.</li>
    <li><strong>new_appointment.html</strong>: Template for creating new appointments.</li>
    <li><strong>new_client.html</strong>: Template for adding new clients.</li>
    <li><strong>search_clients.html</strong>: Template for searching clients by name, phone, or ID number.</li>
    <li><strong>view_client.html</strong>: Template for viewing client details.</li>
</ul>

<h5>client_base/utils/</h5>
<ul>
    <li><strong>helpers.py</strong>: Utility functions and helper methods used across different modules in the application.</li>
</ul>

<h4>instance/</h4>
<ul>
    <li><strong>clients.db</strong>: SQLite database file storing client and appointment data.</li>
</ul>

<h4>migrations/</h4>
<ul>
    <li><strong>alembic.ini</strong>: Configuration file for Alembic, used for managing database migrations.</li>
    <li><strong>env.py</strong>: Sets up the environment for database migrations.</li>
    <li><strong>README</strong>: Provides information about the migration scripts.</li>
    <li><strong>script.py.mako</strong>: Template used by Alembic for generating migration scripts.</li>
    <li><strong>versions/89b868e4991b_initial_migration.py</strong>: The initial database migration script.</li>
</ul>

<h3>Root Files</h3>
<ul>
    <li><strong>retrieve.py</strong>: Script for retrieving and displaying data from the database.</li>
    <li><strong>run.py</strong>: The main entry point of the application, initializing the Flask app and starting the server.</li>
    <li><strong>tree.py</strong>: Script for displaying the project’s file tree structure.</li>
    <li><strong>wsgi.py</strong>: WSGI entry point for deploying the application.</li>
</ul>

<h2>Getting Started</h2>

<h3>Prerequisites</h3>
<ul>
    <li>Python 3.x</li>
    <li>Flask</li>
    <li>SQLite</li>
    <li>Alembic</li>
</ul>

<h3>Installation</h3>
<ol>
    <li>Clone the repository:
        <pre><code>git clone https://github.com/cerform/tattoo.git
cd tattoo</code></pre>
    </li>
    <li>Set up a virtual environment and install dependencies:
        <pre><code>python3 -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
pip install -r requirements.txt</code></pre>
    </li>
    <li>Initialize the database:
        <pre><code>flask db upgrade</code></pre>
    </li>
    <li>Run the application:
        <pre><code>python run.py</code></pre>
    </li>
</ol>

<h2>Development Workflow</h2>

<h3>Adding new features:</h3>
<ul>
    <li>Develop your feature in a separate branch and create a pull request for review.</li>
    <li>Follow the project structure and conventions outlined in this README.</li>
</ul>

<h3>Database migrations:</h3>
<ul>
    <li>If you modify the database schema, create a new migration script using Alembic:
        <pre><code>flask db migrate -m "Description of change"
flask db upgrade</code></pre>
    </li>
</ul>

<h3>Testing:</h3>
<ul>
    <li>Ensure that new features and bug fixes are well-tested before merging into the main branch.</li>
</ul>

<h2>Contribution Guidelines</h2>
<ul>
    <li>Follow the coding standards and best practices as specified in the <code>CONTRIBUTING.md</code> file.</li>
    <li>Write clear and concise commit messages.</li>
    <li>Document new features and code changes adequately.</li>
</ul>
