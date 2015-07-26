from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):
    return HttpResponse("Dream Site Index Page")

@csrf_exempt
def new_mentor( request ):
    if request.method == "GET":
        print("GOT GET")
        return HttpResponse("Okay")
    elif request.method == "POST":
        print('GOT POST')
        for i in request.form.items():
            print(i)
        return HttpResponse("Okay")
    

