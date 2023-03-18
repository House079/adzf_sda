# Generated by Django 4.1.7 on 2023-03-17 10:24

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import django.views.generic.list


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('for_client', models.BooleanField(default=True)),
                ('for_all', models.BooleanField(default=True)),
                ('event_name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('duration', models.DurationField()),
            ],
            managers=[
                ('client', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='EventTypesList',
            fields=[
                ('eventtype_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='prices.eventtype')),
            ],
            bases=('prices.eventtype', django.views.generic.list.ListView),
            managers=[
                ('client', django.db.models.manager.Manager()),
            ],
        ),
    ]
