from .imports import *


class TeamView(viewsets.ModelViewSet):

    def create(self, request, *args, **kwargs):
        pass


class TeamDetailsView(viewsets.ModelViewSet):

    def update(self, request, *args, **kwargs):
        pass

    def destroy(self, request, *args, **kwargs):
        pass


class TeamMemberView(viewsets.ModelViewSet):

    def create(self, request, *args, **kwargs):
        pass


class TeamMemberDetailsView(viewsets.ModelViewSet):

    def update(self, request, *args, **kwargs):
        pass
    def destroy(self, request, *args, **kwargs):
        pass