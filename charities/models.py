from django.db import models
from accounts.models import User

class Benefactor(models.Model):
    user = models.OneToOneField(User)
    experience = models.SmallIntegerField(choices=(
        (0 , 'mobtadi'),
        (1 , 'motevaset'),
        (2 , 'motekhases')
    ) , default=0)
    free_time_per_week = models.PositiveSmallIntegerField(default=0)

class Charity(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=50)
    reg_number = models.CharField(max_length=10)
    


class Task(models.Model):
    assigned_benefactor = models.ForeignKey(Benefactor , null=True , on_delete=models.SET_NULL)
    charity = models.ForeignKey(Charity)
    age_limit_from = models.IntegerField()
    age_limit_to = models.IntegerField()
    date = models.DateField(null=True , blank=True)
    description = models.TextField()
    gender_limit = models.CharField(max_length=1 , blank=True , null=True , choices=(
        ('M' , 'M'),
        ('F' , 'F')
    ))
    state = models.CharField(max_length=1 , choices=(
        ('A' , 'Assigned'),
        ('W' , 'Waiting'),
        ('P' , 'Pending'),
        ('D' , 'Done')
    ) , default='P')
    title = models.CharField(max_length=60)