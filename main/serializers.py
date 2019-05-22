
from marshmallow_sqlalchemy import ModelSchema

from main.models import User
from .models import *

class UserSchema(ModelSchema):

    class Meta :
        model = User


class RecordScema(ModelSchema):
    class Meta :
        model = Record




