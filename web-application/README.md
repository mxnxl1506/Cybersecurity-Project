# Web Application with Flask

This project is a simple web application implemented using Flask for user authentication.

## Features
- Basic user authentication with username and password.
- RESTful API endpoint for user login.

## Usage
1. Install required dependencies: `pip install Flask`
2. Run the application: `python app.py`
3. Send POST requests to `http://localhost:5000/login` with JSON payload: `{"username": "admin", "password": "password123"}`

## Security Considerations
- Use secure storage for user credentials in production.
- Implement HTTPS for secure communication.

For more details, refer to the [app.py](./app.py) script.
