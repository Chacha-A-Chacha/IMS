from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = "had to guess key as the security key in my falsk IMS web_app"

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# login manager for user authentication and authorization
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
