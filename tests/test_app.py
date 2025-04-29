# tests/test_app.py
from app import app

def test_home():
    # Test the main home route
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200  # Ensure it returns a 200 OK status
        assert b'Hello from Flask!' in response.data  # Check if the correct text is returned
