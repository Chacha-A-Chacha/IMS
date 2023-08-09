#!/src/bin/env python3

from flask import Blueprint, render_template

# Create a Blueprint for your routes
inventory_bp = Blueprint("inventory", __name__)

# Define route handlers using the blueprint


@inventory_bp.route("/")
def index():
    return render_template("index.html")


@inventory_bp.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@inventory_bp.route("/add_item")
def add_item():
    return render_template("add_item.html")

# Define more routes as needed
# ...

# Register the blueprint in your main app script (app.py)
# Example: app.register_blueprint(inventory_bp, url_prefix="/inventory")
