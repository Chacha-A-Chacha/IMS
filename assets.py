#!/src/bin/env python3

from flask_assets import Bundle

# Create a CSS bundle for Tailwind CSS
# css = Bundle('src/main.css', output='dist/main.css', filters='postcss')
tailwind_css_bundle = Bundle(
    "path/to/tailwind.css",  # Replace with the actual path to your Tailwind CSS file
    filters="postcss",  # Use PostCSS to process the CSS
    output="gen/tailwind.css"  # Output file for the processed CSS
)

# Define other asset bundles for your inventory app if needed
# For example, JavaScript bundles, images, etc.
