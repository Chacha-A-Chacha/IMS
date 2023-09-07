#!/src/bin/env python3
from app import create_app

# Create the Flask app using the create_app function from the app package
app = create_app('development')

if __name__ == '__main__':
    # Run the Flask app
    app.run()
