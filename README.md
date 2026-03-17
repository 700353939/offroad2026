Offroad is a basic web application built with Django. 
It allows users to manage destinations, vehicles, and travel stories.
Authentication is not implemented.

Features    
    Create, view, update, and delete: Destinations, Vehicles, Stories
    Search destinations by name    
    Sort destinations by name and difficulty    
    Custom CSS styling    
    Custom template tags    
    Custom 404 error page

Project Structure
    Common – shared functionality, template tags, base templates    
    Destinations – destinations to explore    
    Vehicles – offroad vehicles    
    Stories – travel stories related to destinations and vehicles

Technologies Used    
    Python    
    Django    
    PostgreSQL (Supabase)    
    HTML & CSS

Database Configuration
    Create a .env file based on .env.template and fill in the required environment variables.

Installation

    Clone the repository:    
    git clone https://github.com/700353939/offroad2026.git
    cd offroad2026
    
    Create a virtual environment:    
    python -m venv venv
    
    Activate the environment:    
    Windows:    
    venv\Scripts\activate    
    Linux/macOS:    
    source venv/bin/activate
    
    Install dependencies:    
    pip install -r requirements.txt
    
    Apply migrations:    
    python manage.py migrate
    
    Run the server:    
    python manage.py runserver