# IMS
Inventory Management System





[Flask + TailwindCSS + Flask Assets](https://dev.to/ffpaiki/flask-tailwindcss-flask-assets-51mo#:~:text=Continuing%20from%20the%20previous%20article%20%22Getting%20Started%20with,easy%E2%80%A6%20you%20just%20need%20to%20use%20Flask-Assets%20package.)

[Flask-Assets](https://flask-assets.readthedocs.io/en/latest/) -- Documentation


inventory_app/
|-- app/
|   |-- static/
|   |   |-- css/
|   |   |   |-- main.css
|   |   |-- js/
|   |   |   |-- script.js
|   |   |-- images/
|   |-- templates/
|   |   |-- base.html
|   |   |-- login.html
|   |   |-- register.html
|   |   |-- team_select.html
|   |   |-- team_create.html
|   |   |-- inventory.html
|   |   |-- error.html
|-- migrations/
|-- models.py
|-- routes.py
|-- config.py
|-- run.py
|-- requirements.txt
|-- .env



$env:FLASK_APP = "app:create_app('development')"  # Set the Flask app and configuration
flask run
