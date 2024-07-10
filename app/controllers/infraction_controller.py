from app.models import Infraction
from app import db

class InfractionController:
    @staticmethod
    def create_infraction(data, officer_id):
        infraction = Infraction(
            license_plate=data['license_plate'],
            timestamp=data['timestamp'],
            comments=data['comments'],
            officer_id=officer_id
        )
        db.session.add(infraction)
        db.session.commit()
        return infraction
