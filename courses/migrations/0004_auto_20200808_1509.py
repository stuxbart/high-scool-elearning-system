# Generated by Django 3.1 on 2020-08-08 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_membership'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='membership',
            table='courses_membership_courses',
        ),
    ]
