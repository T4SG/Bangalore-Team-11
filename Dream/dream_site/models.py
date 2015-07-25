from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Mentor(models.Model):
    mentor_id = models.AutoField( primary_key = True )
    name = models.CharField( max_length = 254 )
    age = models.IntegerField( max_length = 2 )
    native_city = models.CharField( max_length = 254 )
    current_city = models.CharField( max_length = 254 )
    
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
    
    phone_number = models.CharField( max_length = 20 )
    email = models.CharField( max_length = 254 )
    company = models.CharField( max_length = 254 )
    area = models.CharField( max_length = 254 )                           # Area lived in, example : Kormangala, Indiranagar, Whitefield
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    username = models.CharField( max_length = 254 )
    password = models.CharField( max_length = 254 )
    
