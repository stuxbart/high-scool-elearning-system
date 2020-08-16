# Generated by Django 3.1 on 2020-08-08 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_membership'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='courses',
            field=models.ManyToManyField(blank=True, related_name='participants', through='courses.Membership', to='courses.Course'),
        ),
    ]