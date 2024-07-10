from flask import Blueprint, request
from flask_restful import Api, Resource
from marshmallow import ValidationError
from app.schemas.infraction_schema import InfractionSchema
from app.controllers.infraction_controller import InfractionController
from app.models import Vehicle
from app.auth.decorators import officer_required

bp = Blueprint('infractions', __name__, url_prefix='/api')
api = Api(bp)

infraction_schema = InfractionSchema()

class InfractionResource(Resource):
    @officer_required
    def post(self):
        data = request.get_json()
        try:
            validated_data = infraction_schema.load(data)
        except ValidationError as err:
            return {"errors": err.messages}, 422

        vehicle = Vehicle.query.filter_by(license_plate=validated_data['license_plate']).first()
        if not vehicle:
            return {"error": "Vehicle not found"}, 404
        
        infraction = InfractionController.create_infraction(validated_data, request.officer.id)
        return {"message": "Infraction created successfully", "data": infraction_schema.dump(infraction)}, 201

api.add_resource(InfractionResource, '/cargar_infraccion')
