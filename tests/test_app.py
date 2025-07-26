# test_app.py

from flask.testing import FlaskClient
import pytest
from app import app # Import the Flask app instance from your app.py

@pytest.fixture
def client():
    """
    This fixture provides a test client for your Flask application.
    It sets up the app for testing by disabling debug mode and handling context.
    """
    app.config['TESTING'] = True # Enable testing mode
    with app.test_client() as client:
        yield client # Yield the client to the test functions

def test_hello_world(client: FlaskClient):
    """
    Tests that the home page ('/') returns the correct 'Hello, World!' message
    and a 200 OK status code.
    """
    response = client.get('/') # Make a GET request to the root URL
    assert response.status_code == 200 # Check if the status code is 200 OK
    assert b'Hello, World from Flask!' in response.data # Check if the response data contains the expected message
