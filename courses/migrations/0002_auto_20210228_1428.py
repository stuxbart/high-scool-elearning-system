# Generated by Django 3.1.7 on 2021-02-28 13:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='participants',
            field=models.ManyToManyField(blank=True, related_name='courses', through='courses.Membership', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='CourseAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('can_add_participants', models.BooleanField(default=False)),
                ('can_add_content', models.BooleanField(default=False)),
                ('can_remove_participants', models.BooleanField(default=False)),
                ('can_remove_content', models.BooleanField(default=False)),
                ('can_edit_course', models.BooleanField(default=False)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='admins',
            field=models.ManyToManyField(blank=True, related_name='admin_courses', through='courses.CourseAdmin', to=settings.AUTH_USER_MODEL),
        ),
    ]