from django.db import models
from django.conf import settings
from django.db import models
from datetime import datetime
from ..service import service

from ..oauth import models as model
from ..property import models as model

class Agent(models.Model):
    user            = models.ForeignKey(model.UserModel, on_delete=models.CASCADE)
    first_name      = models.CharField(max_length=200, verbose_name='first name')
    last_name       = models.CharField(max_length=200, verbose_name='last name')
    photo           = models.ImageField(upload_to=service.upload_avatar_path,
                                        verbose_name='realtor photo')
    description     = models.TextField(blank=True, verbose_name='description')
    phone           = models.CharField(max_length=20, verbose_name='phone number')
    # social_networks = models.ManyToManyField('SocialNetwork')
    hire_date       = models.DateTimeField(default=datetime.now,blank=True)
    created_at      = models.DateTimeField(editable=False, verbose_name='created at')
    updated_at      = models.DateTimeField(editable=False, verbose_name='updated at')


    def __str__(self):
        return self.first_name
    
class Language(models.Model):
    language        = models.CharField(max_length=50)

class Nation(models.Model):
    nation          = models.CharField(max_length=50)

class Feedback(models.Model):
    user            = models.ForeignKey(model.UserModel, on_delete=models.CASCADE)
    property        = models.ForeignKey(model.Property, on_delete=models.CASCADE)




'''
class SocialNetwork(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    url = models.URLField()
  
    email = models.CharField(max_length=20)
    skype = models.CharField(max_length=30)
    facebook = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100)
    


    def __str__(self):
        return self.name
'''