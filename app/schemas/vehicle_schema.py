from marshmallow import Schema, fields

class VehicleSchema(Schema):
    id = fields.Int(dump_only=True)
    license_plate = fields.Str(required=True)
    brand = fields.Str(required=True)
    color = fields.Str(required=True)
    owner_id = fields.Int(required=True)
