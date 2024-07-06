from datetime import datetime
from app.extensions import db

class Infraction(db.Model):
    __tablename__ = 'infraction'
    id = db.Column(db.Integer, primary_key=True)
    license_plate = db.Column(db.String(10), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    comments = db.Column(db.String(200), nullable=False)
    officer_id = db.Column(db.Integer, db.ForeignKey('officer.id'), nullable=False)
