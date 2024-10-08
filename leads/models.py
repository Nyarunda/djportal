from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

class Lead(models.Model):
    
    SOURCE_CHOICES = (
        ('YouTube', 'YouTube'),
        ('Google','Google'),
        ('Newsletter','Newsletter'),
    )

    first_name = models.CharField(max_length=80,blank=False)
    last_name = models.CharField(max_length=80)
    phoned = models.BooleanField(default=False)
    source = models.CharField(choices=SOURCE_CHOICES,max_length=100)
    picture = models.ImageField(blank=True,null=True)
    files = models.FileField()
    Agent = models.ForeignKey("Agent", on_delete=models.SET_NULL,null=True)

class Agent(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phoned = models.BooleanField(default=False)