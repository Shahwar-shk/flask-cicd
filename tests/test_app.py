# tests/test_app.py
import unittest
from app import app  # Import the app object from app.py

class TestFlaskApp(unittest.TestCase):

    def test_home(self):
        # Test the home route
        with app.test_client() as client:
            response = client.get('/')
            self.assertEqual(response.status_code, 200)  # Ensure status is 200
            self.assertIn(b'Hello from Flask!', response.data)  # Check if 'Hello from Flask!' appears

if __name__ == '__main__':
    unittest.main()


