# Generated by Django 3.1.7 on 2021-03-15 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gradebook', '0004_auto_20210315_1329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentsubjectrecordbook',
            name='close_date',
        ),
    ]
