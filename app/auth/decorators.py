# app/auth/decorators.py
from functools import wraps
from flask import request, jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from app.models import Officer

def officer_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        current_user = get_jwt_identity()
        
        officer = Officer.query.filter_by(badge_number=current_user).first()
        if not officer:
            return {"error": "Invalid token"}, 403
        
        # Attach the officer object to the request context
        request.officer = officer
        return fn(*args, **kwargs)
    
    return wrapper
