"""
Main entry point for the Superheroes API Flask application.
"""

from app import create_app
from app.routes import register_routes

# Create the Flask application instance
app = create_app()

# Run the application in debug mode if executed directly
if __name__ == '__main__':
    app.run(debug=True, port=5007)
