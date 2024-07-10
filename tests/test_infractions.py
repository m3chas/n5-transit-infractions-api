import unittest
from app import create_app, db
from app.models import Infraction, Vehicle, Officer, Person
import json
from flask_jwt_extended import create_access_token
from datetime import datetime
from werkzeug.security import generate_password_hash

class InfractionApiTestCase(unittest.TestCase):

    def setUp(self):
        """Set up test variables and create test app."""
        self.app = create_app(config_name='testing')
        self.client = self.app.test_client
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

        # Add test data
        self.person = Person(name='Jane Doe', email='jane.doe@example.com')
        db.session.add(self.person)
        db.session.commit()

        self.vehicle = Vehicle(license_plate='ABC123', brand='Toyota', color='Red', owner_id=self.person.id)
        db.session.add(self.vehicle)
        db.session.commit()

        # Create officer and generate token for authentication
        self.officer = Officer(
            name='John Doe',
            badge_number='12345',
            api_key=create_access_token(identity='12345')
        )
        db.session.add(self.officer)
        db.session.commit()

        self.token = 'Bearer ' + self.officer.api_key

    def tearDown(self):
        """Tear down test variables."""
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_create_infraction(self):
        """Test creating an infraction via API."""
        infraction_data = {
            "license_plate": "ABC123",
            "timestamp": datetime.fromisoformat("2024-07-06T10:00:00"),
            "comments": "Speeding"
        }

        response = self.client().post(
            '/api/cargar_infraccion',
            headers={'Authorization': self.token},
            data=json.dumps(infraction_data, default=str),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 201)
        self.assertIn('Infraction created successfully', str(response.data))

        # Verify infraction in database
        infraction = Infraction.query.filter_by(license_plate='ABC123').first()
        self.assertIsNotNone(infraction)
        self.assertEqual(infraction.comments, "Speeding")
        self.assertEqual(infraction.officer_id, self.officer.id)

if __name__ == "__main__":
    unittest.main()
