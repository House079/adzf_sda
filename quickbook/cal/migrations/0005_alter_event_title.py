# Generated by Django 4.1.7 on 2023-03-25 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0004_alter_event_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(default='', max_length=200, verbose_name='Tytuł'),
            preserve_default=False,
        ),
    ]
