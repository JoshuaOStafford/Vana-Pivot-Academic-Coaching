# Generated by Django 2.0.6 on 2018-07-26 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='classgrade',
            name='session_number',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='habitscore',
            name='session_number',
            field=models.PositiveIntegerField(default=0),
        ),
    ]