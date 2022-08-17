from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from .models import *
from .serializers import *
import pickle


# Create your views here.
def index(request):
    return HttpResponse('Welcome')

class ActionAutomation:
    def __init__(self):
        self.automation = dict()
        
    def register(self, automation, action):
        self.automation[automation.name] = action
        
    def unregister(self, automation):
        del self.automation[automation.name]
        
    def perform_action(self, automation, **kwargs):
        action = self.automation[automation.name]
        return action(kwargs)
    
def save_object(obj, filename):
    with open(filename, 'wb') as outp:
        pickle.dump(obj, outp, pickle.HIGHEST_PROTOCOL)
        




@api_view(['GET', 'POST'])
def Create_Automation(request):
    
    if request.method == 'POST':
        
        authomation = Automation.objects.create(
            host = request.user,
            name = request.data['name'],
            Trigger = request.data['Trigger'],
            Trigger_details = request.data['Trigger_details'],
            Action = request.data['Action'],
            Action_details = request.data['Action_details'],
            
        )
        
        
        print(authomation)
        if authomation.Action == 'Send_email':
            
            with open('ActionAutomation.pkl', 'rb') as ActionAutomation_file:
                automate = pickle.load(ActionAutomation_file)
                
            automate.register(automation=authomation, action=Send_Email)
            
            save_object(automate, 'ActionAutomation.pkl')
            
            print(automate.automation)
            
        elif authomation.Action == 'Add_tag':
            
            with open('ActionAutomation.pkl', 'rb') as ActionAutomation_file:
                automate = pickle.load(ActionAutomation_file)
                
            automate.register(automation=authomation, action=Add_Tag)
            
            save_object(automate, 'ActionAutomation.pkl')
            
            print(automate.automation)
            
        serializer = AutomationSerializer(authomation)
        
        authomation.change_state_to_running()
        authomation.save()
            
        return Response(serializer.data)
    
    else:
        return Response('''Parse in automation details in the json format
                            {"name": "", "Trigger_name": "",
                                "Trigger_details": "{"Email_List": " "}",
                                    "Action_name": "" , "Action_details": "{"Email_List": " ", "Tag": " "}"
                                        }''')



        

def Send_Email(**kwargs):
    """_summary_ This function sends an email to the subscriber

    Args:
        email (str): _description_
    """
    
    email = kwargs['email']
    
    print(f'Email sent to {email}')
    
    
    
def Add_Tag(**kwargs):
    """_summary_ This funtion adds tag to the email

    Args:
        email (str): _description_ this is the email to add tag to.
        tag (str): _description_ this is the tag to be added to the email.
    """
    
    email = kwargs['email']
    tag = kwargs['tag']
    
    try:
        tags = Tags.objects.get(
            name = tag
        )
    except:
        tags = Tags.objects.create(
            name = tag
        )
        
    emails = Emails.objects.get(email= email)
    
    emails.tags.add(tags)
    
    print(f'{tags} tag added to {emails}')
    
    return emails


@api_view(['GET', 'POST'])
def OptIn_EmailList(request):
    
    if request.method == 'POST':
        
        try:
            email = Emails.objects.get(email = request.data['email'])
        except:
            email = Emails.objects.create(email = request.data['email'])
            
        
        try:
            email_list = EmailList.objects.get(name = request.data['email_list'])
            
            email_list.subscribers.add(email)
            
            automations = Automation.objects.filter(Trigger='Opt_IN', Trigger_details__exact={'Email_List': email_list.name})

            with open('ActionAutomation.pkl', 'rb') as ActionAutomation_file:
                automate = pickle.load(ActionAutomation_file)
             
            print(automate.automation.keys())
            
            for automation in automations:
                
                for name in automate.automation.keys():
                    if name == automation.name:
                        perform_action = automate.automation[name]
                        perform_action(email= email, tag=automation.Action_details['Tag'] )
                        
            return Response(f'Your email {email}, was successfully added to {email_list}')
            
        except:
            return Response("There's no existing email list for your input", status=status.HTTP_404_NOT_FOUND)
        
    else:
        return Response('''Parse in your email and email list you wish to subscribe to in this JSON format
                            {"email": " ", "email_list": " "}''' )
        
        
        

