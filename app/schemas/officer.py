from marshmallow import Schema, fields

class OfficerSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    badge_number = fields.Str(required=True)
