from django.conf.urls import url
from django.urls import path
from user1 import views


app_name='user1'
urlpatterns = [
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
 ]
