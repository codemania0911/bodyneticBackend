from ssl import create_default_context
from django.db import models
from django.utils import timezone

# Create your models here.
class UserData(models.Model):
    class Meta:
        db_table = 'userdb_tb'
    fullName = models.CharField(max_length=32, blank=True)
    email = models.CharField(max_length=32, blank=True)
    password = models.CharField(max_length=32, blank=True)
    isVerified = models.BooleanField(default=False)
    verification_code = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    isDeleted = models.BooleanField(default=False)    
    
class Profile(models.Model):
    class Meta:
        db_table = 'profile_tb'  
    user_id = models.ForeignKey("UserData", on_delete = models.CASCADE, db_column="post_id")  
    gender = models.CharField(max_length=   32, blank=True) # Man, Woman, Transgender, None, NoRespond
    dob = models.DateField()
    height = models.FloatField(blank=True   )
    weight = models.FloatField(blank=True)
    target_weight = models.FloatField(blank=True)
    pain_parts = models.IntegerField(blank=True)
    daily_task = models.IntegerField(blank= True )
    fitness_goal = models.IntegerField(blank= True )
    favourite_type_excercise = models.IntegerField(blank= True )
    equipment = models.IntegerField(blank= True)
    created_at = models.DateTimeField(auto_now_add = True)
    isDeleted = models.BooleanField(default=False)    

