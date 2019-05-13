from django.shortcuts import render

# Create your views here.
from datetime import date
import sqlalchemy.orm
from django.utils.timezone import now
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from sqlalchemy import create_engine, delete
from sqlalchemy.orm.exc import NoResultFound
from .serializers import *
from passlib.hash import bcrypt
from rest_framework import viewsets
from main.models import User
from django.http import Http404


engine = create_engine("mysql://root:16001700@localhost/PTO_system")
Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()


class LoginView(viewsets.ModelViewSet):
    def create(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            account = session.query(User).filter_by(email=email).one()
            if account.email == email:
                if bcrypt.verify(password, account.password):
                    request.session['user_id'] = account.id
                    account.last_login = now()
                    return Response(status=status.HTTP_200_OK)
            return Response(status=status.HTTP_418_WRONG_CREDENTIALS)
        except NoResultFound:
            return Response("details : this email doesnt belong to any account ", status=status.HTTP_404_NOT_FOUND)


class UserView(viewsets.ModelViewSet):

    def retrieve(self, request, *args, **kwargs):
        result = []
        accounts = session.query(User).all()
        user_schema = UserSchema()
        for us in accounts:
            result.append(user_schema.dump(us).data)
        return Response(result, status=status.HTTP_200_OK)




