from flask import Blueprint, request, jsonify
from app.models import Person, Vehicle, Infraction
from app.schemas.infraction import InfractionSchema
from app import db

bp = Blueprint('reports', __name__, url_prefix='/api')

@bp.route('/generar_informe', methods=['GET'])
def generar_informe():
    email = request.args.get('email')
    person = Person.query.filter_by(email=email).first()
    if not person:
        return jsonify({"error": "Person not found"}), 404
    
    vehicles = Vehicle.query.filter_by(owner_id=person.id).all()
    infractions = Infraction.query.filter(Infraction.license_plate.in_([v.license_plate for v in vehicles])).all()
    infraction_schema = InfractionSchema(many=True)
    return jsonify(infraction_schema.dump(infractions)), 200
