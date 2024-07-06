from flask import Blueprint, request, jsonify
from app import db
from app.models import Infraction, Vehicle, Officer
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime

bp = Blueprint('infractions', __name__, url_prefix='/api')

@bp.route('/cargar_infraccion', methods=['POST'])
@jwt_required()
def cargar_infraccion():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No input data provided"}), 400

    license_plate = data.get('placa_patente')
    timestamp_str = data.get('timestamp')
    comments = data.get('comentarios')

    if not license_plate or not timestamp_str or not comments:
        return jsonify({"error": "Missing required fields"}), 422

    vehicle = Vehicle.query.filter_by(license_plate=license_plate).first()
    if not vehicle:
        return jsonify({"error": "Vehicle not found"}), 404

    try:
        timestamp = datetime.fromisoformat(timestamp_str)
    except ValueError:
        return jsonify({"error": "Invalid timestamp format"}), 422

    officer_id = get_jwt_identity()
    officer = Officer.query.filter_by(id=officer_id).first()
    if not officer:
        return jsonify({"error": "Officer not found"}), 404

    infraction = Infraction(
        license_plate=license_plate,
        timestamp=timestamp,
        comments=comments,
        officer_id=officer.id
    )
    db.session.add(infraction)
    db.session.commit()

    return jsonify({"message": "Infraction created successfully"}), 200
