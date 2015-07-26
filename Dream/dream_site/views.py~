import hashlib
from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.views.decorators.csrf import csrf_exempt
from dream_site.models import Mentor, Mentee, Team, Meeting, Goal
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
        #pw = hashlib.md5()
        #pw  = pw.update( request.POST['password'].encode('UTF-8') )
        pw  = request.POST['password']
        n1  = request.POST['form-first-name']
        l3  = request.POST['other-language']
        pno = request.POST['phone-number'] 
        unm = request.POST['user-name']
        h4  = request.POST['hobby1']
        h1  = request.POST['hobby2']
        h2  = request.POST['hobby3']
        h3  = request.POST['hobby4']
        n2 = request.POST['form-last-name']
        are = request.POST['area']
        col = request.POST['college_degree']
        iag = request.POST.get( 'age', False )
        #iag = request.POST['age']
        ccy = request.POST.get( 'form-current-city', False )
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
        iag = request.POST.get( 'age', False )
        #iag = request.POST['age']
        ad  = request.POST['address']
        gen = request.POST['gender']
        eml = request.POST['form-email']
       # com = request.POST['company']
        clg = request.POST['college']
        ncy = request.POST['form-native-city']
        ccy = request.POST[ 'form-current-city' ]
        l1  = request.POST['primary-language']
        h1 = request.POST['hobby1']
        h2 = request.POST['hobby2']
        h3 = request.POST['hobby3']
        h4 = request.POST['hobby4']
        #pw = hashlib.md5();
        #pw  = pw.update( ( request.POST['password'] ).encode('UTF-8') )
        pw  = request.POST['password']        
        ar = request.POST['area']
        n1  = request.POST['form-first-name']
        l3  = request.POST['other-language']
        pno = request.POST['phone-number']
        unm = request.POST['user-name']
        n2  = request.POST['form-last-name']
        Mentee.objects.create(  name = ( n1 + " " + n2 ), 
                                age = iag, 
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






@csrf_exempt
def mentor_login( request ):
    if request.method == "GET":
        print("GOT GET")
        return HttpResponse("Okay")
    elif request.method == "POST":
        if request.POST['username']:
            print("hi")

@csrf_exempt
def mentee_login( request ):
    if request.method == "GET":
        print("GOT GET")
        return HttpResponse("Okay")
    elif request.method == "POST":
        if request.POST['username']:
            print("hi")





@csrf_exempt
def mentor_debug( request ):
    if request.method == "GET":
        print("GOT GET")
        return HttpResponse("Okay")
    elif request.method == "POST":

        print(request.POST['secondary-language'])
        print(request.POST['address'])
        print(request.POST['gender'])
        print(request.POST['form-email'])
        print(request.POST['company'])
        print(request.POST['form-native-city'])
        print(request.POST['primary-language'])
        #pw = hashlib.md5()
        #pw  = pw.update( request.POST['password'].encode('UTF-8') )
        print(request.POST['password'])
        print(request.POST['form-first-name'])
        print(request.POST['other-language'])
        print(request.POST['phone-number'])
        print(request.POST['user-name'])
        print(request.POST['hobby1'])
        print(request.POST['hobby2'])
        print(request.POST['hobby3'])
        print(request.POST['hobby4'])
        print(request.POST['form-last-name'])
        print(request.POST['area'])
        print(request.POST['college_degree'])
        print(request.POST['age'])
        #iag = request.POST['age']
        print(request.POST[ 'form-current-city'])
        return HttpResponse("Okay")
        
def mentor_page( request, mentor_id_in ):
    obj = Mentor.objects.get( pk = mentor_id_in )
    return HttpResponse("200 Ok")
        
        
def mentee_page( request, mentee_id_in ):
    obj = Mentee.objects.get( mentee_id = mentee_id_in )
    html_page = """<!DOCTYPE html>
<html lang="en">

    <head>

        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Admin page</title>

        <!-- CSS -->
        <link rel="stylesheet" href="http://fonts.googleapis.com/css?family=Roboto:400,100,300,500">
        <link rel="stylesheet" href="assets/bootstrap/css/bootstrap.min.css">
        <link rel="stylesheet" href="assets/font-awesome/css/font-awesome.min.css">
		<link rel="stylesheet" href="assets/css/form-elements.css">
        <link rel="stylesheet" href="assets/css/style.css">

        <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
        <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
        <!--[if lt IE 9]>
            <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
            <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
        <![endif]-->

        <!-- Favicon and touch icons -->
        <link rel="shortcut icon" href="assets/ico/favicon.png">
        <link rel="apple-touch-icon-precomposed" sizes="144x144" href="assets/ico/apple-touch-icon-144-precomposed.png">
        <link rel="apple-touch-icon-precomposed" sizes="114x114" href="assets/ico/apple-touch-icon-114-precomposed.png">
        <link rel="apple-touch-icon-precomposed" sizes="72x72" href="assets/ico/apple-touch-icon-72-precomposed.png">
        <link rel="apple-touch-icon-precomposed" href="assets/ico/apple-touch-icon-57-precomposed.png">

    </head>

    <body>
<nav class="navbar navbar-inverse navbar-fixed-top">
  <div class="container-fluid">
    <div>
      <ul class="nav navbar-nav">
        <li class="active"><a href="index.html">Home</a></li>
      </ul>
    </div>
  </div>
</nav>
        <!-- Top content -->
        <div class="top-content">
        	
            <div class="inner-bg">
                <div class="container">
                    <div class="row">
                        <div class="col-sm-8 col-sm-offset-2 text">
                            <h1><strong>Dream School Foundation</strong> <br>Welcome !!</h1>
                            <div class="description">
                            	<p>
	                            	<h3>YOUR MENTEE IS</h3><br /> 
                            	</p>
                            </div>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-sm-6 col-sm-offset-3 form-box">
                        	<div class="form-top">
           

<h6>Name:</h6>
<label id= %s ></label><br />
<h6>Profile:</h6>
<label id= %s ></label><br />
<h6>Gender:</h6>
<label id= %s ></label><br />

Meet The mentee : <input type="text" name="meeting" placeholder="enter date" />
<br/>
<input type="submit" name="datesubmit" value="submit"><br/>
<br/>
<h5> RATE THE MENTEE </h5><br />
<form method="POST" action="">
<h5>Communication skills:</h5>
<input type="text" name="Communicationskills" ><br />
<h5>Academics:</h5>
<input type="text" name="Academics" ><br />
<h5>Extracurricular Activities:</h5>
<input type="text" name="ExtracurricularActivities" ><br />
<h5>Next Meeting Date:</h5>
<input type="text" name="NextMeetingDate" ><br /><br/>
<input type="button" name="Submit" value="Submit Ratings" ><br />
<br/> 

</form>
		                    </div>
                        </div>
                    </div>
                    
                        </div>
                    </div>
                </div>
            </div>
            
        </div>


        <!-- Javascript -->
        <script src="assets/js/jquery-1.11.1.min.js"></script>
        <script src="assets/bootstrap/js/bootstrap.min.js"></script>
        <script src="assets/js/jquery.backstretch.min.js"></script>
        <script src="assets/js/scripts.js"></script>
        
        <!--[if lt IE 10]>
            <script src="assets/js/placeholder.js"></script>
        <![endif]-->

    </body>

</html>"""%(obj.name, obj.college_degree, obj.gender)
    return HttpResponse( html_page )
