# Generated by Django 4.1.7 on 2023-03-20 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0002_alter_event_day_alter_event_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='day',
            field=models.DateField(verbose_name='Dzień'),
        ),
    ]
