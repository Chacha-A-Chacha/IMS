#!/src/bin/env python3

# from flask import Flask
# from flask_assets import Environment
# from assets import tailwind_css_bundle
#
# app = Flask(__name__)
# assets = Environment(app)   # Initialize Flask-Assets environment
#
# app.config.from_object('config.Config')  # Load configuration from config.py
#
# db = SQLAlchemy(app)
# mail = Mail(app)
#
# # Register the Tailwind CSS bundle
# assets.register("main_css", tailwind_css_bundle)

from app import create_app

# Create the Flask app using the create_app function from the app package
app = create_app()

if __name__ == '__main__':
    # Run the Flask app
    app.run()
