from app.extensions import db

class Officer(db.Model):
    __tablename__ = 'officer'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    infractions = db.relationship('Infraction', backref='officer', lazy=True)
