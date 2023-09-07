from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()


def create_app(config_name):
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "had to guess key as the security key in my Flask IMS web_app"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'your_database_uri_here'  # Replace with your actual database URI

    db.init_app(app)
    migrate.init_app(app, db)

    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'  # Specify the login view for authentication

    # Register blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth_bp as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app
