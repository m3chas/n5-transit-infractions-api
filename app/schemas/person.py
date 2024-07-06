from marshmallow import Schema, fields

class PersonSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    vehicles = fields.List(fields.Nested(lambda: VehicleSchema(exclude=("owner",))))
