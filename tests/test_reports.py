import unittest
from app import create_app, db
from app.models import Person, Vehicle, Infraction, Officer
from flask_jwt_extended import create_access_token
import json
from datetime import datetime
from werkzeug.security import generate_password_hash

class ReportApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

        # Set initial data for testing purposes
        self.person = Person(name="John Doe", email="john.doe@example.com")
        db.session.add(self.person)
        db.session.commit()

        self.vehicle = Vehicle(license_plate="ABC123", brand="Toyota", color="Red", owner_id=self.person.id)
        db.session.add(self.vehicle)
        db.session.commit()

        self.officer = Officer(
            name="Jane Smith",
            badge_number="12345",
            api_key=create_access_token(identity='12345')
        )
        db.session.add(self.officer)
        db.session.commit()

        self.infraction = Infraction(
            license_plate="ABC123", 
            timestamp=datetime.fromisoformat("2024-07-06T10:00:00"), 
            comments="Speeding", 
            officer_id=self.officer.id
        )
        db.session.add(self.infraction)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_generate_report(self):
        response = self.client().get(
            '/api/generar_informe?email=john.doe@example.com',
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['comments'], "Speeding")
        self.assertEqual(data[0]['license_plate'], "ABC123")

if __name__ == "__main__":
    unittest.main()
