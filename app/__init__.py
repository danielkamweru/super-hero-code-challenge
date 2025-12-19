from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

from app.config import Config

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class: type[Config] = Config) -> Flask:
    """
    Application factory used by the CLI and tests.
    """
    app = Flask(__name__, instance_relative_config=True)

    # Load default configuration
    app.config.from_object(config_class)

    # Enable CORS for all routes (simple API use-case)
    CORS(app)

    # Initialise extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Import models so they are registered with SQLAlchemy metadata
    with app.app_context():
        from app import models  # noqa: F401

    return app

