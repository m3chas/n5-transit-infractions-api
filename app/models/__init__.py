from app.extensions import db

# Import the models to register them with SQLAlchemy
from .person import Person
from .vehicle import Vehicle
from .officer import Officer
from .infraction import Infraction
