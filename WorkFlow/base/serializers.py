from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from base.models import *



class AutomationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Automation
        fields = '__all__'
        