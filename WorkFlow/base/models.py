from django.db import models
from django.contrib.auth.models import AbstractUser
from django_fsm import transition, FSMField

import jsonfield
# Create your models here.

class User(AbstractUser):
    pass

class Tags(models.Model):
    name = models.CharField(default=None, max_length=20)
    
    def __str__(self):
        return self.name



class Emails(models.Model):
    email = models.EmailField(unique=True, null=True)
    tags = models.ManyToManyField(
        Tags, related_name='Tags', blank=True)
    
    def __str__(self):
        return self.email



class EmailList(models.Model):
    name = models.CharField(max_length=200)
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    description = models.TextField(null=True, blank=True)
    subscribers = models.ManyToManyField(
        Emails, related_name='subscribers', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Email List'
        
    def __str__(self):
        return self.name
 
 
STATES = (
    ('Running', 'Running'),
    ('Stopped', 'Stopped'),
    ('Not-published', 'Not-published')
)   

class Automation(models.Model):
    
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=20, default=None, unique=True )
    created = models.DateTimeField(auto_now_add=True)
    Trigger = models.CharField(max_length=20, default=None)
    Trigger_details = jsonfield.JSONField(default=None)
    Action = models.CharField(max_length=20, default=None)
    Action_details = jsonfield.JSONField(default=None)
    Condition = models.CharField(max_length=20, default=None, null=True)
    Condition_details = jsonfield.JSONField(default=None, null=True)
    state = FSMField(default='Not-published',
                     choices=STATES, protected=True)
    
    
    def __str__(self):
        return self.name
    
    @transition(field=state, source='Not-published', target='Running')
    def change_state_to_running(self):
        return "State changed to running."
    
    @transition(field=state, source='Running', target='Stopped')
    def change_state_from_running_to_stopped(self):
        return "State changed to stopped."


