from django.shortcuts import render
from django.http import  HttpResponse
from rest_framework.response import Response
from . models import *
from django.views.decorators.csrf import csrf_exempt
import paho.mqtt.client as mqtt
from django.views import View
from .mqtt_handler import publish_message_to_topic

def say_hello(request):
    return render(request, "hello.html")

def mqtt_publish(request):
    publish_message_to_topic("demo/one", "Hello, MQTT!")
    return HttpResponse("Message published to MQTT topic")