from rest_framework import viewsets

from .imports import *

engine = create_engine("mysql://root:16001700@localhost/PTO_system")
Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()


class UserView(viewsets.ModelViewSet):

    def retrieve(self, request, *args, **kwargs):
        result = []
        accounts = session.query(User).all()
        user_schema = UserSchema()
        for us in accounts:
            result.append(user_schema.dump(us).data)
        return Response(result, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):

        try:
            session.add(account)
            session.new
            session.commit()
        except:
            session.rollback()
            raise

        finally:
            session.close()

        return Response(status=status.HTTP_204_NO_CONTENT)

class UserDetailsView(viewsets.ModelViewSet):

    def retrieve(self, request, *args, **kwargs):
        pass
    def update(self, request, *args, **kwargs):
        pass
    def destroy(self, request, *args, **kwargs):
        pass


