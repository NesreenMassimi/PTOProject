
from marshmallow_sqlalchemy import ModelSchema
from .models import User



class UserSchema(ModelSchema):
    fields = ('email','hiring_date','phone_number','ID','role_id','password','created','updated','last_login','name')

    class Meta :
        model = User




