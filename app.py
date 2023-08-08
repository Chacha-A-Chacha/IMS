#!/src/bin/env python3

from flask import Flask
from flask_assets import Environment, Bundle

app = Flask(__name__)
assets = Environment(app)

# Bundling src/main.css files into dist/main.css'
# css = Bundle('src/main.css', output='dist/main.css', filters='postcss')
tailwind_css_bundle = Bundle(
    "/static/src/main.css",      # Replace with the actual path to your Tailwind CSS file
    filters="postcss",           # Use PostCSS to process the CSS
    output="/static/css/output.css"    # Output file for the processed CSS
)

# Add the CSS bundle to the assets environment
assets.register("main_css", tailwind_css_bundle)

if __name__ == "__main__":
    app.run(debug=True)
    