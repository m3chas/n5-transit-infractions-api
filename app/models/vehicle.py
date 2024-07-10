from app.extensions import db

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    license_plate = db.Column(db.String(10), unique=True, nullable=False)
    brand = db.Column(db.String(50), nullable=False)
    color = db.Column(db.String(50), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('person.id'), nullable=False)
