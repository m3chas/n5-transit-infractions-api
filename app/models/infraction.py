from datetime import datetime
from app.extensions import db

class Infraction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    license_plate = db.Column(db.String(10), db.ForeignKey('vehicle.license_plate'), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    comments = db.Column(db.Text, nullable=True)
    officer_id = db.Column(db.Integer, db.ForeignKey('officer.id'), nullable=False)
    officer = db.relationship('Officer')
    vehicle = db.relationship('Vehicle')
