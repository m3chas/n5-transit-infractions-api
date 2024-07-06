from marshmallow import Schema, fields

class InfractionSchema(Schema):
    id = fields.Int(dump_only=True)
    license_plate = fields.Str(required=True)
    timestamp = fields.DateTime(required=True)
    comments = fields.Str()
    officer_id = fields.Int(required=True)
    officer = fields.Nested("OfficerSchema")
    vehicle = fields.Nested("VehicleSchema")
