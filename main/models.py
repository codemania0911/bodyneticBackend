from ssl import create_default_context
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from .manager import UserManager

# Create your models here.
class UserData(models.Model):
    class Meta:
        db_table = 'userdb_tb'
    fullName = models.CharField(max_length=32, blank=True)
    email = models.CharField(max_length=32, blank=True)
    password = models.CharField(max_length=32, blank=True)
    existProfile = models.BooleanField(default=False)
    isVerified = models.BooleanField(default=False)
    verification_code = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    isDeleted = models.BooleanField(default=False)    
    
class User(AbstractUser):
    username = None
    email = models.EmailField( unique=True)
    is_verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=6 , null=True, blank=True)
    last_login_time = models.DateTimeField(null=True, blank=True)
    last_logout_time = models.DateTimeField(null=True, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()
    def name(self):
        return self.first_name + ' ' + self.last_name
    def __str__(self):
        return self.email
    
class Profile(models.Model):
    class Meta:
        db_table = 'profile_tb'  
    user_id = models.ForeignKey("UserData", on_delete = models.CASCADE, db_column="post_id")  
    gender = models.IntegerField(blank= True )
    dob = models.DateField()
    height = models.FloatField(blank=True   )
    weight = models.FloatField(blank=True)
    target_weight = models.FloatField(blank=True)
    pain_parts = models.CharField(max_length=   255, blank=True) 
    daily_task = models.IntegerField(blank= True )
    fitness_goal = models.CharField(max_length=   255, blank=True) 
    favourite_type_excercise = models.CharField(max_length=   255, blank=True) 
    equipment = models.IntegerField(blank= True)
    created_at = models.DateTimeField(auto_now_add = True)
    isDeleted = models.BooleanField(default=False)    

