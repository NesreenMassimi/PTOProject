from .imports import *


class RecordView(viewsets.ModelViewSet):
    def create(self, request, *args, **kwargs):
        pass
    def retrieve(self, request, *args, **kwargs):
        pass

class RecordDetailsView(viewsets.ModelViewSet):

    def update(self, request, *args, **kwargs):
        pass
    def retrieve(self, request, *args, **kwargs):
        pass

class RecordApprovalView(viewsets.ModelViewSet):

    def update(self, request, *args, **kwargs):
        pass