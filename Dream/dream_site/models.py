from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Mentor(models.Model):
    mentor_id
    name
    age
    native_city
    current_city
    
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
    rating = models.DecimalField( MinValueValidator(0), MaxValueValidator(5) )
    username
    password
    
