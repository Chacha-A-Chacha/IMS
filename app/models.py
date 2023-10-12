# from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from . import db, login_manager  # Import db from the main __init__.py file


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    # id of the user in database (primary)
    id = db.Column('user_id', db.Integer(), primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    # You can add additional fields like 'team_id', 'role', etc.
    # @password.setter
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    items = db.relationship('Item', backref='category', lazy=True)


class Item(db.Model):
    __tablename__ = 'item'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)


# def init_db():
#     db.create_all()
#
#     # Create a test user
#     new_user = User()
#     new_user.display_name = 'Nathan'
#     db.session.add(new_user)
#     db.session.commit()
#
#     new_user.datetime_subscription_valid_until = datetime.datetime(2019, 1, 1)
#     db.session.commit()

def init_db():
    # Create categories
    category1 = Category(name='Networking Devices')
    category2 = Category(name='Cabling Tools')
    category3 = Category(name='Climbers, Belts, Espression, Spellaton Machine, Optical Fiber Identifier')
    category4 = Category(name='Splitter Sizes 1*2, 1*4, 1*8, *16, *32')

    # Add categories to the session
    db.session.add_all([category1, category2, category3, category4])

    # Commit the session to the database
    db.session.commit()

    # Create items for Category 1
    item1 = Item(name='Routers', category=category1)
    item2 = Item(name='Batchcoil', category=category1)
    item3 = Item(name='ATB', category=category1)
    item4 = Item(name='Clips', category=category1)
    item5 = Item(name='Tape', category=category1)
    item6 = Item(name='Steel Nails', category=category1)

    # Create items for Category 2
    item7 = Item(name='Overhead Cable', category=category2)
    item8 = Item(name='Jeuk', category=category2)
    item9 = Item(name='UBP', category=category2)
    item10 = Item(name='Tension Clamp', category=category2)
    item11 = Item(name='Bucklope', category=category2)
    item12 = Item(name='Scrape', category=category2)
    item13 = Item(name='Markers', category=category2)
    item14 = Item(name='Overhead Machine', category=category2)

    # Create items for Category 3
    item15 = Item(name='Climbers', category=category3)
    item16 = Item(name='Belts', category=category3)
    item17 = Item(name='Espression', category=category3)
    item18 = Item(name='Spellaton Machine', category=category3)
    item19 = Item(name='Optical Fiber Identifier', category=category3)

    # Create items for Category 4
    item20 = Item(name='Splitter Sizes 1*2', category=category4)
    item21 = Item(name='Splitter Sizes 1*4', category=category4)
    item22 = Item(name='Splitter Sizes 1*8', category=category4)
    item23 = Item(name='Splitter Sizes *16', category=category4)
    item24 = Item(name='Splitter Sizes *32', category=category4)

    # Add items to the session
    db.session.add_all([item1, item2, item3, item4, item5, item6,
                        item7, item8, item9, item10, item11, item12, item13, item14,
                        item15, item16, item17, item18, item19,
                        item20, item21, item22, item23, item24])

    # Commit the session to the database
    db.session.commit()

# Call the init_db function to initialize the database with categories and items
