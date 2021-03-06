# Generated by Django 3.1 on 2020-08-21 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0007_auto_20200818_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(),
        ),
        migrations.CreateModel(
            name='CalendarShareToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=50)),
                ('active', models.BooleanField(default=False)),
                ('calendar', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cal.calendar')),
            ],
        ),
    ]
