from django.shortcuts import render

# Create your views here.
from .imports import *

engine = create_engine("mysql://root:16001700@localhost/PTO_system")
Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()


class LoginView(viewsets.ModelViewSet):
    def create(self, request, *args, **kwargs):
        login(request)


class RecordView(viewsets.ModelViewSet):
    def create(self, request, *args, **kwargs):
        add_record(request,*args,**kwargs)

    def retrieve(self, request, *args, **kwargs):
        get_records_for_user(request,*args,**kwargs)


class RecordDetailsView(viewsets.ModelViewSet):

    def update(self, request, *args, **kwargs):
        update_record(request,*args,**kwargs)

    def retrieve(self, request, *args, **kwargs):
        get_record(request,*args,**kwargs)


class UserView(viewsets.ModelViewSet):

    def retrieve(self, request, *args, **kwargs):
        get_users(request,*args,**kwargs)


    def create(self, request, *args, **kwargs):
        create_new_user(request,*args,**kwargs)


class UserDetailsView(viewsets.ModelViewSet):

    def retrieve(self, request, *args, **kwargs):
        get_user_by_id(request,*args,**kwargs)

    def update(self, request, *args, **kwargs):
        update_user(request,*args,**kwargs)

    def destroy(self, request, *args, **kwargs):
        delete_user(request,*args,**kwargs)

class TeamView(viewsets.ModelViewSet):

    def create(self, request, *args, **kwargs):
        add_team(request,*args,**kwargs)

class TeamDetailsView(viewsets.ModelViewSet):

    def update(self, request, *args, **kwargs):
        update_team(request,*args,**kwargs)

    def destroy(self, request, *args, **kwargs):
        delete_team(request,*args,*kwargs)


class TeamMemberView(viewsets.ModelViewSet):

    def create(self, request, *args, **kwargs):
        add_team_member(request,*args,*kwargs)


class TeamMemberDetailsView(viewsets.ModelViewSet):

    def update(self, request, *args, **kwargs):
        update_team_member(request,*args,**kwargs)

    def destroy(self, request, *args, **kwargs):
        delete_team_member(request,*args,**kwargs)





