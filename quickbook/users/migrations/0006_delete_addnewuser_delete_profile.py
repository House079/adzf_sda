# Generated by Django 4.1.7 on 2023-03-18 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_profile_position'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AddNewUser',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
