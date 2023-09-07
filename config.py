#!/src/bin/env python3
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = 'your-secret-key'  # Change this to a secure secret key
    # Change this to your preferred database URL
    SQLALCHEMY_DATABASE_URI = 'sqlite:///inventory.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Flask-Mail Configuration (if using email)
    MAIL_SERVER = 'smtp.example.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = 'your-email@example.com'
    MAIL_PASSWORD = 'your-email-password'

    # Flask-Assets Configuration
    ASSETS_DEBUG = False  # Set to True during development for debugging
    ASSETS_AUTO_BUILD = False  # Set to True during development for automatic asset building

    # Tailwind CSS Configuration
    TAILWIND_CSS = {
        'output_path': 'gen/static/css/',
        'entry_file': 'static/css/main.css',  # Path to your main Tailwind CSS file
    }
