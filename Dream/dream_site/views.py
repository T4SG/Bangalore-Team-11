from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.views.decorators.csrf import csrf_exempt
import dream_site.models
# Create your views here.

def index(request):
    return HttpResponse("Dream Site Index Page")

@csrf_exempt
def new_mentor( request ):
    if request.method == "GET":
        print("GOT GET")
        return HttpResponse("Okay")
    elif request.method == "POST":
#        print('GOT POST')
#        for i in request.POST:
#            print(i)
        l2  = request.POST['secondary-language']
        ad  = request.POST['address']
        gen = request.POST['gender']
        eml = request.POST['form-email']
        com = request.POST['company']
        ncy = request.POST['form-native-city']
        l1  = request.POST['primary-language']
        pw  = request.POST['password']
        n1  = request.POST['form-first-name']
        l3  = request.POST['other-language']
        pno = request.POST['phone-number']
        unm = request.POST['user-name']
        n2  = request.POST['form-last-name']
        Mentor.objects.create( name = ( n1 + " " + n2 ), age =  , native_city  = ncy, address = ad, gender = gen, email = eml, primary_language = l1, secondary_language = l2, other_languages = l3, company = com, phone )
        return HttpResponse("Okay")
    

