from django.urls import path
from .views import *
urlpatterns = [
    path('',Viewhome),
    path('verify/<str:userId>/<str:token>/', verifyUser,name='verify'),
]
