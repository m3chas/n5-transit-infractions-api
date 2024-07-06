from flask import Blueprint, request, jsonify
from app.models import Officer
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token

auth = Blueprint('auth', __name__, url_prefix='/api/auth')

@auth.route('', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    
    officer = Officer.query.filter_by(email=email).first()
    if officer and check_password_hash(officer.password, password):
        access_token = create_access_token(identity=officer.id)
        return jsonify(access_token=access_token), 200
    return jsonify({"msg": "Bad email or password"}), 401
