from app import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    # id of the user in database (primary
    id = db.Column('user_id', db.Integer(), primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    


    # You can add additional fields like 'team_id', 'role', etc.

    def __repr__(self):
        return '<User {}>'.format(self.username)
