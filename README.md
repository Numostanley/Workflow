# Workflow
This is a test environment for a workflow automation project

With the objective being to create a workflow engine that automates specific tasks, which will be executed based on certain triggers and conditions, i've written a programme to simulate this workflow based on the requirements in the documentation provided.

The workflow engine i've written can be used to create automations which can be triggered when a subscriber Opts-in to a specific email list. The automation actions could be set to either send an email to the subscriber or add a tag to the subscriber.

Below is a simple demonstration of my workflow, which is written in python programming language and the Django rest framework.

First, the project can be run using the -$ python manage.py runserver- command from the root directory in the command line. 
The dependencies used in this project can be installed directly using the pip install -r requirements.txt command

Next we'll go to the url route that will be used to create our specific automation. Which is http://127.0.0.1:8000/create-authomation

From this API route, we'll pass in the details needed to create the Automation. Which will look like this;

![Screenshot (20)](https://user-images.githubusercontent.com/90499278/185233904-10bbb796-b9e5-4631-a9b7-df6e5f92ec59.png)

Once the post request has been sent successfully, we'll get the following response;

![Screenshot (21)](https://user-images.githubusercontent.com/90499278/185234147-ecfc880a-bd1f-4868-b8cd-b9b47bd98661.png)


This shows that the automation named "My_automation2" has been created. 

This automation is been triggered when a subscriber opts in to an email list (List2) as shown, and it executes the "Send_email" action.

To verify, lets opt in to an email

![Screenshot (23)](https://user-images.githubusercontent.com/90499278/185234764-6d74d30c-c5ce-41a1-aa81-a4dc6cfdd487.png)

Once the post request is been sent successfully, we get the following response;

![Screenshot (24)](https://user-images.githubusercontent.com/90499278/185235048-b47e45f2-8fae-4a34-ba01-139fa349738e.png)

And from our terminal (second to last line), we can see that the automation was triggered, and an email was sent to the subscriber

![Screenshot (24b)](https://user-images.githubusercontent.com/90499278/185235199-7f5e3304-d678-49cf-8720-48770ed73ee2.png)

Next, we'll create an automation that adds a tag to a subscriber through the url route http://127.0.0.1:8000/opt-in.

![Screenshot (25)](https://user-images.githubusercontent.com/90499278/185235405-2d150498-04df-414d-acb0-b5777cc322f9.png)

Once the post request is sent, our automation is created; 

![Screenshot (26)](https://user-images.githubusercontent.com/90499278/185235618-556134c0-f093-424b-b4d3-6ecd233e7507.png)

Now lets Opt in to another email list (List1) as shown;

![Screenshot (27)](https://user-images.githubusercontent.com/90499278/185235917-2c8ca3f4-4bdf-4af5-8d8e-4bc683f26eab.png)

Once the post request is been sent successfully, we get the following response;

![Screenshot (28)](https://user-images.githubusercontent.com/90499278/185236050-a9cf15f8-6871-4ac4-8c30-a443d4dbe1ed.png)


And from our terminal (second to last line),  we can see that the automation was triggered, and the tag "Business" was added to the subscriber;


![Screenshot (28b)](https://user-images.githubusercontent.com/90499278/185236252-dac84060-4f70-4605-a1f9-3bcce2aae657.png)


So we've successfully created two different automations that performs different tasks and are triggered by specific actions.














