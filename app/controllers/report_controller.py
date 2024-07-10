from app.models import Person, Vehicle, Infraction

class ReportController:
    @staticmethod
    def generate_report(email):
        person = Person.query.filter_by(email=email).first()
        if not person:
            return None
        
        vehicles = Vehicle.query.filter_by(owner_id=person.id).all()
        infractions = Infraction.query.filter(Infraction.license_plate.in_([v.license_plate for v in vehicles])).all()
        return infractions
