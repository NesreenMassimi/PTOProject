
from django.urls import path
from . import views

login = views.LoginView.as_view({

    'post':'create'



})

users = views.UserView.as_view({


    'get':'retrieve',
    'post':'create'


})

users_details = views.UserDetailsView.as_view({

    'get':'retrieve'


})

urlpatterns = [path('login/',login,name="login user"),
               path('users',users,name="get all users"),
               path('users',users,name="create new user"),
               path('users/<int:pk>',users_details,name = "get user by id ")
               ]