# Generated by Django 4.1.7 on 2023-03-17 12:31

from django.db import migrations, models
import django.db.models.deletion
import django.views.generic.edit


class Migration(migrations.Migration):

    dependencies = [
        ('prices', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreateEvent',
            fields=[
                ('eventtype_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='prices.eventtype')),
            ],
            bases=('prices.eventtype', django.views.generic.edit.CreateView),
        ),
        migrations.AlterModelManagers(
            name='eventtype',
            managers=[
            ],
        ),
        migrations.AlterModelManagers(
            name='eventtypeslist',
            managers=[
            ],
        ),
    ]
