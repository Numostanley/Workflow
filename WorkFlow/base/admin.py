from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Automation)
admin.site.register(EmailList)
admin.site.register(Emails)
admin.site.register(User)

