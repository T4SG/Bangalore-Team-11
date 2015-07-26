import hashlib
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

        l2  = request.POST['secondary-language']
        ad  = request.POST['address']
        gen = request.POST['gender']
        eml = request.POST['form-email']
        com = request.POST['company']
        ncy = request.POST['form-native-city']
        l1  = request.POST['primary-language']
        pw = hashlib.md5()
        pw  = pw.update( request.POST['password'] )
        n1  = request.POST['form-first-name']
        l3  = request.POST['other-language']
        pno = request.POST['phone-number'] 
        unm = request.POST['user-name']
        h4  = request.POST['hobby1']
        h1  = request.POST['hobby2']
        h2  = request.POST['hobby3']
        h3  = request.POST['hobby4']
        unm = request.POST['form-last-name']
        are = request.POST['area']
        col = request.POST['college_degree']
        iag = request.POST['age']
        ccy = request.POST['form-current-city']
        Mentor.objects.create(  name = ( n1 + " " + n2 ), 
                                native_city  = ncy, 
                                address = ad, 
                                gender = gen, 
                                email = eml, 
                                primary_language = l1, 
                                secondary_language = l2, 
                                other_languages = l3, 
                                company = com, 
                                phone_number = pno, 
                                password = pw, 
                                hobby_1 = h1, 
                                hobby_2 = h2, 
                                hobby_3 = h3, 
                                hobby_4 = h4, 
                                area = are, 
                                college_degree = col, 
                                age = iag, 
                                current_city = ccy 
                              )
        return HttpResponse("Okay")
    

@csrf_exempt
def new_mentee( request ):
    if request.method == "GET":
        print("GOT GET")
        return HttpResponse("Okay")
    elif request.method == "POST":
#        print('GOT POST')
#        for i in request.POST:
#            print(i)
        l2  = request.POST['secondary-language']
		age = request.POST['age']
        ad  = request.POST['address']
        gen = request.POST['gender']
        eml = request.POST['form-email']
       # com = request.POST['company']
		clg = request.POST['college']
        ncy = request.POST['form-native-city']
		ccy = request.POST['form-current-city']
        l1  = request.POST['primary-language']
		h1 = request.POST['hobby1']
		h2 = request.POST['hobby2']
		h3 = request.POST['hobby3']
		h4 = request.POST['hobby4']
		pw = hashlib.md5();
        pw  = pw.update(request.POST['password'])
		ar = request.POST['area']
        n1  = request.POST['form-first-name']
        l3  = request.POST['other-language']
        pno = request.POST['phone-number']
        unm = request.POST['user-name']
        n2  = request.POST['form-last-name']
        Mentee.objects.create(  name = ( n1 + " " + n2 ), 
                                age = iae, 
                                native_city  = ncy,
                                current_city = ccy,
								gender = gen, 
								primary_language = l1, 
								secondary_language = l2,
								other_languages = l3,
								college_degree = clg ,
								hobby_1 = h1,
								hobby_2 = h2,
								hobby_3 = h3,
								hobby_4 = h4,
								college = clg, 
								phone_number = pno, 
								area = ar,
								address = ad,
    							email = eml,
    							username = unm, 
    							password = pw
    					     )
        return HttpResponse("Okay")

