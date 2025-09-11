from django.contrib.auth.models import AbstractUser
from django.db import models
class User(AbstractUser):

    gender_choices=(
        ('F', 'Female'),
        ('M', 'Male'),
    )
    email=models.EmailField(null=True, blank=True)
    first_name=models.CharField(max_length=150 , blank=True, null=True)
    address=models.TextField(blank=True , null=True)
    age=models.PositiveSmallIntegerField(blank=True , null=True)
    description=models.TextField(blank=True , null=True)
    gender=models.CharField(max_length=1 , choices=gender_choices , blank=True ,null=True)
    is_active=models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    phone=models.CharField(max_length=15 , blank=True , null=True)


    
