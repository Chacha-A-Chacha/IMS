from flask import Flask
from flask_migrate import Migrate
from flask_login import LoginManager

from config import config


migrate = Migrate()
login_manager = LoginManager()


def create_app(config_name):
    app = Flask(__name__)
    app.template_folder = 'templates'
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

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
