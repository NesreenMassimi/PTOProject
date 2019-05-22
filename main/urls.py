
from django.urls import path
from .records_apis import *
from .team_api import *

login = LoginView.as_view({

    'post':'create'



})

users = UserView.as_view({


    'get':'retrieve',
    'post':'create'


})

users_details = UserDetailsView.as_view({

    'get':'retrieve'


})

records = RecordView.as_view({

    'get':'retrieve',
    'post':'create'


})

records_details = RecordDetailsView.as_view({
    'put':'update',
    'get':'retrieve'


})

records_approval = RecordApprovalView.as_view({

    'put':'update'



})

teams = TeamView.as_view({

  'post':'create'



})

teams_details = TeamDetailsView.as_view({

    'delete':'destroy',
    'put':'update'

})



urlpatterns = [path('login/',login,name="login user"),
               path('users',users,name="get all users"),
               path('users',users,name="create new user"),
               path('users/<int:pk>',users_details,name = "get user by id "),
               path('users/<int:pk2>/records/<int:pk>' , records_details,name= "specific user records"),
               path('users/<int:pk>/records',records , name = "user records"),
               path('users/<int:pk2>/records/<int:pk>/status', records_approval,name="approve record"),




               ]