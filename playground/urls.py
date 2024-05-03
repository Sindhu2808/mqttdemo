from django.urls import path
from . import views
from .views import *

urlpatterns =[
    path('hello/',views.say_hello),   
    path('mqtt-publish/', views.mqtt_publish, name='mqtt_publish'),    

]
