from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from app.extensions import db
from app.models.person import Person
from app.models.vehicle import Vehicle
from app.models.officer import Officer
from flask_jwt_extended import create_access_token, create_refresh_token
import uuid

admin = Admin(name='Admin Panel', template_mode='bootstrap3')

def generate_api_key(badge_number):
    return create_access_token(identity=badge_number)

class PersonAdmin(ModelView):
    column_list = ('name', 'email')

class VehicleAdmin(ModelView):
    column_list = ('license_plate', 'brand', 'color', 'owner_id')

class OfficerAdmin(ModelView):
    column_list = ('name', 'badge_number', 'api_key')
    form_columns = ('name', 'badge_number')

    def on_model_change(self, form, model, is_created):
        model.api_key = generate_api_key(model.badge_number)

# Add administrative views here
admin.add_view(PersonAdmin(Person, db.session))
admin.add_view(VehicleAdmin(Vehicle, db.session))
admin.add_view(OfficerAdmin(Officer, db.session))
