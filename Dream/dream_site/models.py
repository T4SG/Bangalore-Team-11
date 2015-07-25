from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Mentor(models.Model):
    mentor_id =     models.AutoField( primary_key = True )
    name =          models.CharField( default = '', max_length = 254 )
    age =           models.IntegerField( default = 0 )
    native_city =   models.CharField( default = '',max_length = 254 )
    current_city =  models.CharField( default = '', max_length = 254 )
    languages =     models.CharField( default = '', max_length = 254 )
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
    
    phone_number =      models.CharField( default = '', max_length = 20 )
    email =             models.CharField( default = '', max_length = 254 )
    company =           models.CharField( default = '', max_length = 254 )
    phone_number =      models.CharField( default = '', max_length = 20 )
    address =           models.CharField( default = '', max_length = 254 )
    area =              models.CharField( default = '', max_length = 254 )                           # Area lived in, example : Kormangala, Indiranagar, Whitefield
    rating =            models.IntegerField(default = 0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    college_degree =    models.CharField( default = '', max_length = 254 )
    username =          models.CharField( default = '', max_length = 254 )
    password =          models.CharField( default = '', max_length = 254 )
    
    
class Mentee(models.Model):
    mentee_id =     models.AutoField( primary_key = True )
    name =          models.CharField( default = '', max_length = 254 )
    age =           models.IntegerField( default = 0  )
    native_city =   models.CharField( default = '', max_length = 254 )
    current_city =  models.CharField( default = '', max_length = 254 )
    languages =     models.CharField( default = '', max_length = 254 )
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
                              
    college =           models.CharField( default = '', max_length = 254 )
    phone_number =      models.CharField( default = '', max_length = 20 )
    email =             models.CharField( default = '', max_length = 254 )
    area =              models.CharField( default = '', max_length = 254 )                           # Area lived in, example : Kormangala, Indiranagar, Whitefield    
    address =           models.CharField( default = '', max_length = 20 )
    email =             models.CharField( default = '', max_length = 254 )
    college_degree =    models.CharField( default = '', max_length = 254 )
    username =          models.CharField( default = '', max_length = 254 )
    password =          models.CharField( default = '', max_length = 254 )
    
    
class Admin(models.Model):
    admin_id = models.AutoField( primary_key = True )
    username = models.CharField( default = '', max_length = 254 )
    password = models.CharField( default = '', max_length = 254 )
    
    
class Team(models.Model):
    team_id =                       models.AutoField( primary_key = True )
    mentor_id =                     models.ForeignKey( Mentor )
    mentee_id =                     models.ForeignKey( Mentee )
    message_exchange_frequency =    models.PositiveSmallIntegerField( default = 0 )  # Frequency of message exchanges between Mentor and Mentee
    mentor_response_time =          models.PositiveSmallIntegerField( default = 0  )        # Average response time in between messages sent by Mentor
    mentee_response_time =          models.PositiveSmallIntegerField( default = 0  )        # Average response time in between messages sent by Mentee
    
    
