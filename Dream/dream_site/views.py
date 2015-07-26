from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.

def index(request):
    return HttpResponse("Dream Site Index Page")
    
class new_mentor( request ):
    if request.method == "GET":
        print("GOT GET")
        return HttpResponse("Okay")
    elif request.method == "POST":
        print('GOT POST')
        print("request.form.items()")
        return HttpResponse("Okay")
    

