#!/src/bin/env python3

from flask import Flask
from flask_assets import Environment
from assets import tailwind_css_bundle

app = Flask(__name__)
assets = Environment(app)   # Initialize Flask-Assets environment


# Register the Tailwind CSS bundle
assets.register("main_css", tailwind_css_bundle)


if __name__ == "__main__":
    app.run(debug=True)
    