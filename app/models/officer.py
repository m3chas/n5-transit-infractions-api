from app.extensions import db

class Officer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    badge_number = db.Column(db.String(50), unique=True, nullable=False)
    api_key = db.Column(db.Text, unique=True, nullable=False)

    def __repr__(self):
        return f'<Officer {self.name}>'
