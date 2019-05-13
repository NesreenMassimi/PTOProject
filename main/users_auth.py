from rest_framework import viewsets, status
from main.models import User
from sqlalchemy.orm.exc import NoResultFound
from passlib.hash import bcrypt
from django.utils.timezone import now
import sqlalchemy.orm
from rest_framework.response import Response
from sqlalchemy import create_engine

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


def logout(request):
    try:
        del request.session['user_id']
    except KeyError:
        pass
    return Response(status.HTTP_200_OK)


def is_logged(request):

    if 'user_id' in request.session:
        return True
    return False
