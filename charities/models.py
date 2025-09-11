from django.db import models
from django.conf import settings

class Benefactor(models.Model):
    experience_choices=(
        (0,'مبتدی'),
        (1,'متوسط'),
        (2,'متخصص'),
    )

    user=models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    experience=models.SmallIntegerField(choices=experience_choices , default=0)
    free_time_per_week=models.PositiveSmallIntegerField(default=0)


class Charity(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL , on_delete=models.CASCADE)
    name=models.CharField(null=True , blank=True , max_length=50)
    reg_number=models.CharField(max_length=10)


class Task(models.Model):
    gender_choices=(
        ('F', 'Female'),
        ('M', 'Male'),
    )

    state_choices=(
        ('P' , 'Pending'),
        ('W' , 'Waiting'),
        ('A' , 'Assigned'),
        ('D', 'Done'),

    )
    assigned_benefactor=models.ForeignKey(Benefactor ,blank=True, null=True ,  on_delete=models.SET_NULL)
    charity=models.ForeignKey(Charity , on_delete=models.CASCADE)
    age_limit_from=models.IntegerField(blank=True , null=True)
    age_limit_to=models.IntegerField(blank=True , null=True)
    date=models.DateField(blank=True , null=True)
    description=models.TextField(blank=True , null=True)
    gender_limit=models.CharField(max_length=1 , choices=gender_choices , blank=True , null=True)
    state=models.CharField(max_length=1 , choices=state_choices , default='P')
    title=models.CharField(max_length=60)
