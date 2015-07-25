from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime
# Create your models here.

class Mentor(models.Model):
    mentor_id =     models.AutoField( primary_key = True )
    name =          models.CharField( default = '', max_length = 254 )
    age =           models.IntegerField( validators=[MinValueValidator(0), MaxValueValidator(5)])
    native_city =   models.CharField( default = '',max_length = 254 )
    current_city =  models.CharField( default = '', max_length = 254 )
    hobbies =       models.CharField( default = '', max_length = 254 )
    
    # Module to Determine Gender
    M = 'Male'
    F = 'Female'
    GENDER_CHOICES = (
        (M,'Male'), 
        (F,'Female' ),
    )
    gender = models.CharField( max_length = 6, 
                              choices = GENDER_CHOICES,
                              default = M )

    A = 'Assamese'
    B = 'Bengali'
    G = 'Gujarati'
    H = 'Hindi'
    K = 'Kannada'
    E = 'English'
    M = 'Marathi'
    P = 'Punjabi'
    S = 'Sanskrit'
    Ta = 'Tamil'
    U = 'Urdu'
    Te = 'Telugu'                          
    LANGUAGE_CHOICES = (
                    (A,'Assamese'), 
                    (B,'Bengali' ),
                    (G,'Gujarati'), 
                    (H,'Hindi' ),
                    (K,'Kannada'), 
                    (M,'Marathi' ),
                    (P,'Punjabi'), 
                    (S,'Sanskrit' ),
                    (Ta,'Tamil'), 
                    (U,'Urdu' ),
                    (Te,'Telugu'),
                    (E,'English'),
    )
    primary_language =      models.CharField( max_length = 20,choices = LANGUAGE_CHOICES, default = E )                          
    secondary_language =    models.CharField( max_length = 20,choices = LANGUAGE_CHOICES, default = E )
    other_languages =       models.CharField( default = '', max_length = 254 )


    # Module to Determine College Degree
    CSE =   'Computer Science Engineering'
    ME =    'Mechanical Engineering'
    EC =    'Electronics Engineering'
    EEE =   'Electrical Engineering'
    BT =    'Biotechnology'
    TE =    'Telecommunications Engineering'
    PH =    'Physics Honours'
    CE =    'Chemistry Honours'
    EY =	'Economics'
    FIN =   'Finance'
    AC =    'Accounting'
    MED =   'Medicine'
    HH =    'History Honours'
    SH =    'Sociology Honours'
    EE =    'English Honours'
    COURSE_CHOICES = (
        (CSE,   'Computer Science Engineering'), 
        (ME,    'Mechanical Engineering'),
        (EC,    'Electronics Engineering'),
        (EEE,   'Electrical Engineering'),
        (BT,    'Biotechnology'),
        (TE,    'Telecommunications Engineering'),
        (PH,    'Physics Honours'),
        (CE,    'Chemistry Honours'),
        (EY,    'Economics'),
        (FIN,   'Finance'),
        (AC,    'Accounting'),
        (MED,   'Medicine'),
        (HH,    'History Honours'),
        (SH,    'Sociology Honours'),
        (EE,    'English Honours'),
    )
    college_degree = models.CharField( max_length = 50,
                                      choices = COURSE_CHOICES,
                                      default = CSE )
    
    H1 = 'Reading'
    H2 = 'Sports'
    H3 = 'Politics'
    H4 = 'Computers'
    H5 = 'Geography'
    H6 = 'Wildlife'
    H7 = 'Dance'
    H8 = 'Drawing'
    H9 = 'Acting'
    H10 = 'Cooking'
    H11 = 'Writing'
    H12 = 'Video Games'

    HOBBY_CHOICES = (
        (H1,'Reading'), 
        (H2,'Sports' ),
        (H3,'Politics'), 
        (H4,'Computers' ),
        (H5,'Geography'), 
        (H6,'Wildlife' ),
        (H7,'Dance'), 
        (H8,'Drawing' ),
        (H9,'Acting'), 
        (H10,'Cooking' ),
        (H11,'Writing'),
        (H12,'Video Games')
    )
    hobby = models.CharField( max_length = 20,choices = HOBBY_CHOICES, default = H1 )
    
    phone_number =      models.CharField( default = '', max_length = 20 )
    email =             models.CharField( default = '', max_length = 254 )
    company =           models.CharField( default = '', max_length = 254 )
    phone_number =      models.CharField( default = '', max_length = 20 )
    address =           models.CharField( default = '', max_length = 254 )
    area =              models.CharField( default = '', max_length = 254 )                           # Area lived in, example : Kormangala, Indiranagar, Whitefield
    rating_communication =  models.IntegerField(default = 0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    rating_academics =      models.IntegerField(default = 0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    rating_cocurricular =   models.IntegerField(default = 0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    rating_overall =        models.IntegerField(default = 0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    
    number_of_ratings = models.IntegerField(default = 0)
    
    username =          models.CharField( default = '', max_length = 254 )
    password =          models.CharField( default = '', max_length = 254 )

#####################################################################################################################################    
    
class Mentee(models.Model):
    mentee_id =     models.AutoField( primary_key = True )
    name =          models.CharField( default = '', max_length = 254 )
    age =           models.IntegerField( validators=[MinValueValidator(0), MaxValueValidator(5)])
    native_city =   models.CharField( default = '', max_length = 254 )
    current_city =  models.CharField( default = '', max_length = 254 )
    hobbies =       models.CharField( default = '', max_length = 254 )
    
    # Module to Determine Gender
    M = 'Male'
    F = 'Female'
    GENDER_CHOICES = (
        (M,'Male'), 
        (F,'Female' ),
    )
    gender = models.CharField( max_length = 6, 
                              choices = GENDER_CHOICES,
                              default = M )
                              
    A = 'Assamese'
    B = 'Bengali'
    G = 'Gujarati'
    H = 'Hindi'
    K = 'Kannada'
    E = 'English'
    M = 'Marathi'
    P = 'Punjabi'
    S = 'Sanskrit'
    Ta = 'Tamil'
    U = 'Urdu'
    Te = 'Telugu'                          
    LANGUAGE_CHOICES = (
                    (A,'Assamese'), 
                    (B,'Bengali' ),
                    (G,'Gujarati'), 
                    (H,'Hindi' ),
                    (K,'Kannada'), 
                    (M,'Marathi' ),
                    (P,'Punjabi'), 
                    (S,'Sanskrit' ),
                    (Ta,'Tamil'), 
                    (U,'Urdu' ),
                    (Te,'Telugu'),
                    (E,'English'),
    )
    primary_language =      models.CharField( max_length = 20,choices = LANGUAGE_CHOICES, default = E )                          
    secondary_language =    models.CharField( max_length = 20,choices = LANGUAGE_CHOICES, default = E )
    other_languages =       models.CharField( default = '', max_length = 254 )
                                  
    # Module to Determine College Degree
    CSE =   'Computer Science Engineering'
    ME =    'Mechanical Engineering'
    EC =    'Electronics Engineering'
    EEE =   'Electrical Engineering'
    BT =    'Biotechnology'
    TE =    'Telecommunications Engineering'
    PH =    'Physics Honours'
    CE =    'Chemistry Honours'
    EY =	'Economics'
    FIN =   'Finance'
    AC =    'Accounting'
    MED =   'Medicine'
    HH =    'History Honours'
    SH =    'Sociology Honours'
    EE =    'English Honours'
    COURSE_CHOICES = (
        (CSE,   'Computer Science Engineering'), 
        (ME,    'Mechanical Engineering'),
        (EC,    'Electronics Engineering'),
        (EEE,   'Electrical Engineering'),
        (BT,    'Biotechnology'),
        (TE,    'Telecommunications Engineering'),
        (PH,    'Physics Honours'),
        (CE,    'Chemistry Honours'),
        (EY,    'Economics'),
        (FIN,   'Finance'),
        (AC,    'Accounting'),
        (MED,   'Medicine'),
        (HH,    'History Honours'),
        (SH,    'Sociology Honours'),
        (EE,    'English Honours'),
    )
    college_degree = models.CharField( max_length = 50,
                                      choices = COURSE_CHOICES,
                                      default = CSE )

    H1 = 'Reading'
    H2 = 'Sports'
    H3 = 'Politics'
    H4 = 'Computers'
    H5 = 'Geography'
    H6 = 'Wildlife'
    H7 = 'Dance'
    H8 = 'Drawing'
    H9 = 'Acting'
    H10 = 'Cooking'
    H11 = 'Writing'
    H12 = 'Video Games'

    HOBBY_CHOICES = (
        (H1,'Reading'), 
        (H2,'Sports' ),
        (H3,'Politics'), 
        (H4,'Computers' ),
        (H5,'Geography'), 
        (H6,'Wildlife' ),
        (H7,'Dance'), 
        (H8,'Drawing' ),
        (H9,'Acting'), 
        (H10,'Cooking' ),
        (H11,'Writing'),
        (H12,'Video Games')
    )
    hobby = models.CharField( max_length = 20,choices = HOBBY_CHOICES, default = H1 )
                              
    rating =            models.IntegerField(default = 0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    number_of_ratings = models.IntegerField(default = 0)
    college =           models.CharField( default = '', max_length = 254 )
    phone_number =      models.CharField( default = '', max_length = 20 )
    email =             models.CharField( default = '', max_length = 254 )
    area =              models.CharField( default = '', max_length = 254 )                           # Area lived in, example : Kormangala, Indiranagar, Whitefield    
    address =           models.CharField( default = '', max_length = 20 )
    email =             models.CharField( default = '', max_length = 254 )
    #college_degree =    models.CharField( default = '', max_length = 254 )
    username =          models.CharField( default = '', max_length = 254 )
    password =          models.CharField( default = '', max_length = 254 )

#####################################################################################################################################    
    
class Admin(models.Model):
    admin_id = models.AutoField( primary_key = True )
    username = models.CharField( default = '', max_length = 254 )
    password = models.CharField( default = '', max_length = 254 )

#####################################################################################################################################    
    
class Team(models.Model):
    team_id =                       models.AutoField( primary_key = True )
    mentor_id =                     models.ForeignKey( Mentor )
    mentee_id =                     models.ForeignKey( Mentee )
    team_since =                    models.DateTimeField(default = datetime.now(), blank = True)
    message_exchange_frequency =    models.PositiveSmallIntegerField( default = 0 )  # Frequency of message exchanges between Mentor and Mentee
    mentor_response_time =          models.PositiveSmallIntegerField( default = 0  )        # Average response time in between messages sent by Mentor
    mentee_response_time =          models.PositiveSmallIntegerField( default = 0  )        # Average response time in between messages sent by Mentee

#####################################################################################################################################
    
class Meetings(models.Model):
    team_id =                   models.ForeignKey( Team )
    meeting_id =                models.AutoField( primary_key = True )    
    mentor_meeting_rating =     models.IntegerField(default = 0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    mentee_meeting_rating =     models.IntegerField(default = 0, validators=[MinValueValidator(0), MaxValueValidator(5)])   
    meeting_date = models.DateTimeField(default = datetime.now() ,blank = True)
    TEL = 'Telephone'
    ONL = 'Online'
    F2F = 'Face to Face'
    MEETING_METHODS = (
        (TEL,'Telephone'), 
        (ONL,'Online' ),
        (F2F,'Face to Face'),
    )
    meeting = models.CharField( max_length = 15, 
                              choices = MEETING_METHODS,
                              default = F2F )
                              
#####################################################################################################################################                              
                              
class Goals(models.Model):
    team_id =       models.ForeignKey( Team )
    goal_id =       models.AutoField( primary_key = True )
    goal_name =     models.CharField( default = '', max_length = 254 )
    goal_achieved = models.IntegerField(default = 0, validators=[MinValueValidator(0), MaxValueValidator(5)])   
    goal_date =     models.DateTimeField(default = datetime.now(), blank = True)
