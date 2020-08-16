# Generated by Django 3.1 on 2020-08-08 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_membership'),
        ('accounts', '0003_auto_20200808_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='enrolled_courses',
            field=models.ManyToManyField(related_name='participants', through='courses.Membership', to='courses.Course'),
        ),
    ]
