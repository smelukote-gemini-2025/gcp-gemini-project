# app.py

from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the home page ('/')
@app.route('/')
def hello_world():
    """
    This function will be executed when a user navigates to the root URL.
    It returns a simple "Hello, World!" message.
    """
    return 'Hello, World from Flask!'

# This block ensures the application runs only when the script is executed directly
if __name__ == '__main__':
    # Run the Flask application in debug mode
    # debug=True allows for automatic reloading on code changes
    # and provides a debugger for development.
    app.run(debug=True, host='0.0.0.0', port=8090)