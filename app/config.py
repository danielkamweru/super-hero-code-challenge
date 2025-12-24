pwfimport os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///superheroes.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Flask-Mail configuration
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME', 'kamwerudaniel5@gmail.com')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD', '@#876543')
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER', 'kamwerudaniel5@gmail.com')
