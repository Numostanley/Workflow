# Generated by Django 4.0.5 on 2022-08-16 23:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_automation_action_details_automation_condition_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='automation',
            name='host',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
