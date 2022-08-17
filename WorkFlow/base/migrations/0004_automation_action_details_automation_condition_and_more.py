# Generated by Django 4.0.5 on 2022-08-16 23:08

from django.db import migrations, models
import django_fsm
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_emails_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='automation',
            name='Action_details',
            field=jsonfield.fields.JSONField(default=None),
        ),
        migrations.AddField(
            model_name='automation',
            name='Condition',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='automation',
            name='Condition_details',
            field=jsonfield.fields.JSONField(default=None),
        ),
        migrations.AddField(
            model_name='automation',
            name='Trigger_details',
            field=jsonfield.fields.JSONField(default=None),
        ),
        migrations.AddField(
            model_name='automation',
            name='state',
            field=django_fsm.FSMField(choices=[('Running', 'Running'), ('Stopped', 'Stopped'), ('Not published', 'Not published')], default='Not published', max_length=50, protected=True),
        ),
    ]
