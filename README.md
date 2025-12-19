# Superheroes API

A comprehensive Flask-based JSON API for managing superheroes, their powers, and the relationships between them. This project demonstrates RESTful API design, database relationships, and CRUD operations using Flask and SQLAlchemy.

## Description

This is a Phase 4 code challenge project that provides a backend API for a superhero management system. Users can view heroes and their associated powers, manage power descriptions, and create associations between heroes and powers with strength ratings.

## Features

- **Hero Management**: View all heroes or get detailed information about a specific hero including their powers
- **Power Management**: List all powers, view individual powers, and update power descriptions
- **Hero-Power Associations**: Create relationships between heroes and powers with strength classifications
- **Data Validation**: Ensures data integrity with model validations (e.g., description length, strength values)
- **Cascade Deletes**: Automatically removes related hero-power associations when heroes or powers are deleted
- **RESTful Design**: Follows REST principles with proper HTTP status codes and JSON responses
- **Database Migrations**: Uses Flask-Migrate for database schema management
- **CORS Support**: Enabled for cross-origin requests

## Technologies Used

- **Flask**: Web framework for building the API
- **Flask-SQLAlchemy**: ORM for database interactions
- **Flask-Migrate**: Database migration management
- **Flask-CORS**: Cross-origin resource sharing
- **SQLite**: Database for development (easily configurable for production)
- **Python 3.12+**: Programming language

## Project Structure

```
Phase4-codechallenge-1/
├── Pipfile                # Dependency management (pipenv)
├── superheroes-api/
│   ├── app.py             # Main application entry point
│   ├── seed.py            # Database seeding script
│   ├── requirements.txt   # Python dependencies (pip)
│   ├── README.md          # Project documentation
│   ├── instance/
│   │   └── superheroes.db # SQLite database file
│   ├── migrations/        # Database migration files
│   │   ├── alembic.ini
│   │   ├── env.py
│   │   ├── script.py.mako
│   │   └── versions/
│   │       └── 2fb4af6ac5bc_create_tables.py
│   └── app/
│       ├── __init__.py    # Flask app factory
│       ├── config.py      # Application configuration
│       ├── models.py      # Database models (Hero, Power, HeroPower)
│       └── routes.py      # API route definitions
```

## Installation

### Prerequisites

- Python 3.12 or higher
- pip (Python package installer)

### Setup Steps

1. **Clone the repository** (if applicable) and navigate to the project directory:

```bash
cd superheroes-api
```

2. **Create and activate a virtual environment** (recommended):

```bash
python3 -m venv venv
source venv/bin/activate  
```

3. **Install dependencies**:

Using pip:
```bash
pip install -r requirements.txt
```

Or using pipenv (if preferred):
```bash
pipenv install
pipenv shell
```

## Database Setup

1. **Apply database migrations** to create the database schema:

```bash
flask db upgrade
```

This creates the following tables in `superheroes.db`:
- `heroes`: Stores hero information
- `powers`: Stores power information
- `hero_powers`: Junction table for hero-power relationships

## Seeding Data

Populate the database with sample data:

```bash
python3 seed.py
```

This creates sample heroes (Superman, Wonder Woman, Invisible Woman) and powers (Flight, Super Strength, Invisibility) with their associations.

## Running the Application

Start the development server:

```bash
python3 app.py
```

The API will be available at `http://127.0.0.1:5002` (or the port specified in `app.py`).

## API Endpoints

### Heroes

- **GET /heroes**
  - Returns a list of all heroes
  - Response: `[{"id": 1, "name": "Clark Kent", "super_name": "Superman"}, ...]`

- **POST /heroes**
  - Creates a new hero
  - Body: `{"name": "Kamweru", "super_name": "Sharpspear"}`
  - Response: Created hero object

- **GET /heroes/<id>**
  - Returns detailed information about a specific hero including their powers
  - Response: `{"id": 1, "name": "Clark Kent", "super_name": "Superman", "hero_powers": [...]}`

- **DELETE /heroes/<id>**
  - Deletes a hero and all associated hero-power relationships
  - Response: `{"message": "Hero deleted successfully"}`

### Powers

- **GET /powers**
  - Returns a list of all powers
  - Response: `[{"id": 1, "name": "Flight", "description": "..."}, ...]`

- **POST /powers**
  - Creates a new power
  - Body: `{"name": "Super Speed", "description": "Allows the hero to move at incredible speeds."}`
  - Response: Created power object

- **GET /powers/<id>**
  - Returns information about a specific power
  - Response: `{"id": 1, "name": "Flight", "description": "..."}`

- **PATCH /powers/<id>**
  - Updates a power's description
  - Body: `{"description": "New description (min 20 characters)"}`
  - Response: Updated power object

- **DELETE /powers/<id>**
  - Deletes a power and all associated hero-power relationships
  - Response: `{"message": "Power deleted successfully"}`

### Hero Powers

- **POST /hero_powers**
  - Creates a new association between a hero and a power
  - Body: `{"strength": "Strong", "hero_id": 1, "power_id": 2}`
  - Strength values: "Strong", "Weak", "Average"
  - Response: Created hero-power association with nested hero and power data

- **DELETE /hero_powers/<id>**
  - Deletes a specific hero-power association
  - Response: `{"message": "Hero power deleted successfully"}`

### Error Handling

The API returns appropriate HTTP status codes:
- `200`: Success
- `201`: Created
- `404`: Not Found
- `422`: Unprocessable Entity (validation errors)

## Database Schema

### Hero
- `id` (Integer, Primary Key)
- `name` (String)
- `super_name` (String)

### Power
- `id` (Integer, Primary Key)
- `name` (String)
- `description` (String, minimum 20 characters)

### HeroPower
- `id` (Integer, Primary Key)
- `strength` (String: "Strong", "Weak", "Average")
- `hero_id` (Integer, Foreign Key to heroes.id)
- `power_id` (Integer, Foreign Key to powers.id)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the License of * Daniel Kamweru


