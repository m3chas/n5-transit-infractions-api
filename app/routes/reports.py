from flask import Blueprint, request, jsonify
from app import db
from app.models import Infraction, Vehicle, Person
from app.schemas.infraction import InfractionSchema

bp = Blueprint('reports', __name__, url_prefix='/api')

@bp.route('/generar_informe', methods=['GET'])
def generar_informe():
    email = request.args.get('email')
    if not email:
        return jsonify({"error": "Email parameter is required"}), 400

    person = Person.query.filter_by(email=email).first()
    if not person:
        return jsonify({"error": "Person not found"}), 404

    vehicles = Vehicle.query.filter_by(owner_id=person.id).all()
    infractions = Infraction.query.filter(Infraction.license_plate.in_([v.license_plate for v in vehicles])).all()

    infraction_schema = InfractionSchema(many=True)
    result = infraction_schema.dump(infractions)

    return jsonify({'infractions': result}), 200
