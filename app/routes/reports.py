from flask import Blueprint, request
from flask_restful import Api, Resource
from app.schemas.infraction_schema import InfractionSchema
from app.controllers.report_controller import ReportController

bp = Blueprint('reports', __name__, url_prefix='/api')
api = Api(bp)

infraction_schema = InfractionSchema(many=True)

class ReportResource(Resource):
    def get(self):
        email = request.args.get('email')
        infractions = ReportController.generate_report(email)
        if not infractions:
            return {"error": "No infractions found"}, 404
        
        return infraction_schema.dump(infractions), 200

api.add_resource(ReportResource, '/generar_informe')
