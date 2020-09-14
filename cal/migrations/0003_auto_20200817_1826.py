# Generated by Django 3.1 on 2020-08-17 16:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cal', '0002_calendar_overview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendar',
            name='subscribers',
            field=models.ManyToManyField(blank=True, related_name='calendars', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='event',
            name='guests',
            field=models.ManyToManyField(blank=True, related_name='as_guest_events', through='cal.Participation', to=settings.AUTH_USER_MODEL),
        ),
    ]
